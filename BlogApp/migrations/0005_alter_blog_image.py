# Generated by Django 4.0.4 on 2022-06-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0004_alter_blog_categoria_delete_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='Confirmar_traferencia'),
        ),
    ]
