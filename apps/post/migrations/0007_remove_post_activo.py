# Generated by Django 4.2.7 on 2023-12-10 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_post_activo_alter_post_autor_alter_post_imagen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='activo',
        ),
    ]
