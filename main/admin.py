from django.contrib import admin
from .models import Tag, Project, ProjectImage

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    inlines = [] 
    search_fields = ('title', 'description')
    list_filter = ('tags',)
