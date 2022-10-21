# Generated by Django 4.1.2 on 2022-10-21 08:52

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.profilepic.jpg', force_format=None, keep_meta=True, quality=-1, scale=None, size=[720, 720], upload_to='profile_photos'),
        ),
    ]
