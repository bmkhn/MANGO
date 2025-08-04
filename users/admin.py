from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, College
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = User
    list_display = ('email', 'given_name', 'last_name', 'role', 'campus', 'college', 'is_staff')
    list_filter = ('role', 'campus', 'college')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': (
            'given_name', 'middle_initial', 'last_name', 'suffix', 'sex', 'contact_no', 'campus', 'college'
        )}),
        ('Professional', {'fields': (
            'role', 'degree', 'expertise', 'company', 'industry', 'is_expert'
        )}),
        ('Access', {'fields': ('created_by', 'created_at', 'profile_picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role')
        }),
    )
    search_fields = ('email', 'given_name', 'last_name')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(College)
