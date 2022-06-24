# Generated by Django 4.0.4 on 2022-06-24 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0022_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='snipper',
            field=models.CharField(default='Click link above to read blog....', max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitulo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]