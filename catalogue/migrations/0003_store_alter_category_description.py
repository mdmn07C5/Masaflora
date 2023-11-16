# Generated by Django 4.2.6 on 2023-11-01 18:29

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_alter_menuitem_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='US')),
                ('opening_hours', models.TimeField()),
                ('closing_hours', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'stores',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]