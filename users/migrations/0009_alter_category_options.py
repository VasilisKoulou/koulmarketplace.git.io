# Generated by Django 4.2.2 on 2023-09-05 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_skill_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
