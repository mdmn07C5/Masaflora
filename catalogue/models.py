from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse(
            viewname='catalogue:category_list',
            args=[self.slug]
        )

    def __str__(self):
        return self.name


class MenuItemManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super(MenuItemManager, self).get_queryset().filter(is_available=True)


class MenuItem(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    category = models.ForeignKey(
        Category, related_name='menuitem', on_delete=models.CASCADE)
    short_description = models.CharField(
        max_length=255, blank=True, help_text='Short description or translation if dish name is not in English.')
    full_description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    menuitems = MenuItemManager()

    class Meta:
        verbose_name_plural = 'menuitems'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse(
            viewname='catalogue:menuitem_detail',
            args=[self.slug]
        )

    def __str__(self):
        return self.name
