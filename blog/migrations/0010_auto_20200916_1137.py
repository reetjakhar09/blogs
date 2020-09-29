# Generated by Django 2.2.16 on 2020-09-16 11:37

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200916_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=True, editable=False, populate_from='title'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=True, editable=False, populate_from='title'),
        ),
    ]
