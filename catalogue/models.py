from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class MenuItemManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super(MenuItemManager, self).get_queryset().filter(is_available=True)


class MenuItem(models.Model):
    store = models.ForeignKey(
        "Store", related_name="menuitem", on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        "Category", related_name="menuitem", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Short description or translation if dish name is not in English.",
    )
    image = models.ImageField(
        upload_to="images/", default="images/default.png", null=True
    )

    slug = models.SlugField(max_length=255)
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    menuitems = MenuItemManager()

    class Meta:
        verbose_name_plural = "menuitems"
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse(
            viewname="catalogue:detail", args=[self.category.slug, self.slug]
        )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255)
    store = models.ForeignKey(
        "Store", related_name="category", on_delete=models.CASCADE
    )
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse(viewname="catalogue:category_list", args=[self.slug])

    def get_menuitems(self):
        return MenuItem.menuitems.filter(category=self.id)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    contact = PhoneNumberField(region="US")
    opening_hours = models.TimeField()
    closing_hours = models.TimeField()

    class Meta:
        verbose_name_plural = "stores"

    def get_absolute_url(self):
        return reverse(viewname="catalogue:store_page", args=[self.slug])

    def get_categories(self):
        return Category.objects.filter(store=self.id)

    def get_menu(self):
        categories = self.get_categories()
        return {
            category: MenuItem.objects.filter(category=category)
            for category in categories
        }

    def __str__(self) -> str:
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    item = models.ManyToManyField(MenuItem, blank=True)
    category = models.ManyToManyField(Category, blank=True)

    class Meta:
        verbose_name_plural = "options"

    def __str__(self) -> str:
        return self.name
