# Generated by Django 4.2.6 on 2023-11-28 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0010_rename_short_description_menuitem_alt_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='price',
        ),
    ]
