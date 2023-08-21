# Generated by Django 4.2.4 on 2023-08-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0002_remove_categorymodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=300, null=True, unique=True),
        ),
    ]
