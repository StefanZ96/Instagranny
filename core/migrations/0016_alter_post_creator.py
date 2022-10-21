# Generated by Django 4.1.2 on 2022-10-20 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0015_alter_comments_creator_alter_comments_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
