# Generated by Django 4.0.4 on 2022-06-24 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0023_blog_snipper_alter_blog_subtitulo_alter_blog_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='snipper',
            new_name='snippet',
        ),
    ]