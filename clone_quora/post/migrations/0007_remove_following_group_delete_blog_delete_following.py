# Generated by Django 4.1.7 on 2023-04-24 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0002_remove_profile_following'),
        ('post', '0006_blog_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='following',
            name='group',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Following',
        ),
    ]
