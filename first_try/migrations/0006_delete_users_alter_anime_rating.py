# Generated by Django 4.1.2 on 2023-02-27 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_try', '0005_remove_anime_image_anime_images_anime_urls_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AlterField(
            model_name='anime',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]