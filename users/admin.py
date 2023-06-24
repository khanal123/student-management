from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Teacher, SessionYearModel, Student

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "is_staff", "is_active", 'user_role')
    list_filter = ("username", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions", 'user_role')}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", 'user_role'
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'gender', 'experience', 'degree']
    list_filter = ['full_name', 'gender', 'experience', 'degree']
    search_fields = ['full_name']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'gender', 'session_year_id', 'phone_no']
    list_filter = ['full_name', 'gender', 'session_year_id', 'phone_no']
    search_fields = ['full_name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(SessionYearModel)
admin.site.register(Student, StudentAdmin)