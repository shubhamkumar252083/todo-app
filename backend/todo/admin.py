from django.contrib import admin

# Register your models here.

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ["id", "_str_", "description", "completed"]
    search_fields = ["title", "description"]


admin.site.register(Todo, TodoAdmin)
