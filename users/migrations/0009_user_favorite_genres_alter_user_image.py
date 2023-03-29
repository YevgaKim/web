# Generated by Django 4.1.2 on 2023-03-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_genres',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/vendor/users_images'),
        ),
    ]
