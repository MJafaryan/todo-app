from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel


class UserModelAdmin(UserAdmin):
    """Admin customization for UserModel(custom user) model"""

    model = UserModel

    list_display = ("username", "email", "is_superuser",)
    list_filter = ("is_superuser",)
    search_fields = ("username", "email",)
    ordering = ("username",)

    fieldsets = (
        (None, {
                "fields": ("username", "email", "password",)
            }),
        ("Permissions", {
                "fields": ("is_active", "is_staff", "is_superuser",)
            }),
        ("Group permissions", {
                "fields": ("groups", "user_permissions",)
        }),
        ("Important dates", {
                "fields": ("last_login", "date_joined",)
        }),
    )

    add_fieldsets = (
        (None, {
                "classes": ("wide",),
                "fields": (
                    "username", "email", "password1", "password2",
                    "is_active", "is_staff", "is_superuser",
                    )
            }),
    )


admin.site.register(UserModel, UserModelAdmin)
