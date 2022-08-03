from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'full_name', 'is_active', 'last_login']
    ordering = ['email']
    search_fields = ['full_name', 'email']
    readonly_fields = ['last_login', 'date_joined']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2')
        }),
    )
    fieldsets = (
        (None, {
            "fields": (
                'email',
                'password',
            ),
        }),
        (_('Personal info'), {
            "fields": ('full_name', )
        }),
        (_('Permissions'), {
            "fields": ('is_staff', 'is_active', 'is_superuser',)
        }),
        (_('Important dates'), {
            "fields": ('last_login', 'date_joined')
        }),
    )


admin.site.register(User, UserAdmin)
