from django.contrib import admin
from .models import Tag, Project, ProjectImage

# Register your models here.

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    inlines = [ProjectImageInline] 
    search_fields = ('title', 'description')
    list_filter = ('tags',)
