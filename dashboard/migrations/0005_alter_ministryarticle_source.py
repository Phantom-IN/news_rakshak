# Generated by Django 4.2.5 on 2023-09-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_ministryarticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ministryarticle',
            name='source',
            field=models.URLField(),
        ),
    ]
