# Generated by Django 4.1.7 on 2023-04-09 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_profile_follows_rename_group_blog_following_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
