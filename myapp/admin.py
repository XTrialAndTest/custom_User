from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.
class SuperAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "user_type",
        "date_joined",
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "is_admin",
    )

    search_fields = (
        "email",
        "username",
        "first_name",
        "last_name",
    )
    readonly_fields = (
        "id",
        "date_joined",
        "last_login",
    )


admin.site.register(CustomUser, SuperAdmin)
admin.site.register(Applicant, SuperAdmin)
# admin.site.register(ApplicantProfile, SuperAdmin)
