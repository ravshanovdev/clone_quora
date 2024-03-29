from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User


# Register your models here.


# class ProfileInline(admin.StackedInline):
#     model = Profile


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'biography', 'profile_pic', 'web_site_url', 'instagram_url',
                    'twitter_url', 'facebook_url', 'pinterest_url',)
    prepopulated_fields = {'slug': ['user']}




