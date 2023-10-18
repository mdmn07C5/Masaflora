from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse(
            viewname='tacobar:category_list',
            args=[self.slug]
        )
    
    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    category = models.ForeignKey(Category, related_name='menuitem', on_delete=models.CASCADE)
    short_description = models.CharField(max_length=255, blank=True, help_text='Short description or translation if dish name is not in English.')
    full_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/') # temp
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'menuitems'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse(
            viewname='tacobar:menuitem_detail',
            args=[self.slug]
        )
    
    def __str__(self):
        return self.name
    