from django.contrib import admin
from .models import Project, ProjectImage
from django.utils.html import format_html


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'created_at', 'image_preview')
    list_filter = ('featured',)
    search_fields = ('title', 'description')
    inlines = [ProjectImageInline]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height:auto;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Main Image'


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption', 'uploaded_at')

