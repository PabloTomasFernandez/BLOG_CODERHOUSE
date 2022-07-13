# Generated by Django 4.0.4 on 2022-06-24 01:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogApp', '0025_alter_blog_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='like',
            field=models.ManyToManyField(null=True, related_name='Blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
