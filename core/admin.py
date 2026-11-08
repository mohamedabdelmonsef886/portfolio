from django.contrib import admin
from .models import ContactMessage, Project
# Register your models here.

# تخصيص شكل عرض الرسائل
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')

# تسجيل المشاريع
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'live_url', 'github_url')
    search_fields = ('title', 'description')
