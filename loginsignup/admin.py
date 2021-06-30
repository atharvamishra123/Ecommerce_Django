from django.contrib import admin

# Register your models here.
from loginsignup.models import CustomUsers


@admin.register(CustomUsers)
class LoginSignUpAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password1']

# admin.site.register(CustomUsers)
