# Generated by Django 3.1.5 on 2021-03-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default/default_blog_post_img.png', null=True, upload_to='thumbnails/'),
        ),
    ]
