# Generated by Django 4.0.4 on 2022-06-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0015_categoria_blog_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='categoria',
            field=models.CharField(max_length=50),
        ),
    ]