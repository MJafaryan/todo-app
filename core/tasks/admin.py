from django.contrib import admin
from .models import TaskModel


class TaskModelAdmin(admin.ModelAdmin):
    """Admin customization for TaskModel"""

    model = TaskModel

    list_display = ("title", "user", "created_at", "completed",)
    list_filter = ("user", "completed",)
    search_fields = ("user__username", "title",)
    ordering = ("-created_at",)

    fieldsets = (
        (None, {
                "fields": ("title", "completed", "description",),
        }),
        ("Important dates", {
                "fields": ("created_at", "updated_at", "due_date",),
        }),
        ("User information", {
                "fields": ("user",),
        })
    )
    readonly_fields = ("created_at", "updated_at",)


admin.site.register(TaskModel, TaskModelAdmin)
