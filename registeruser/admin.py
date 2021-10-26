from django.contrib import admin
from registeruser.models import AppUser

@admin.register(AppUser)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password']
# Register your models here.
