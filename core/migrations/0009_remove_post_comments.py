# Generated by Django 4.1.2 on 2022-10-12 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_post_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]
