# Generated by Django 4.0.4 on 2022-06-25 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0034_alter_blog_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogApp.categoria'),
        ),
    ]
