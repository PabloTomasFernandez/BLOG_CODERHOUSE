# Generated by Django 4.0.4 on 2022-06-23 17:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogApp', '0020_alter_blog_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='like',
            field=models.ManyToManyField(related_name='Blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='categoria',
            field=models.CharField(default='Sin categoria', max_length=50),
        ),
    ]