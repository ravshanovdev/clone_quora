# Generated by Django 4.2.1 on 2023-07-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0019_alter_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
