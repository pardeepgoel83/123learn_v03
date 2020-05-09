from django.contrib import admin

# Register your models here.
from user.models import *


class PermissionAdmin(admin.ModelAdmin):
    fields = ['name', 'desc', 'status']
    list_display = ('name', 'desc', 'status')


admin.site.register(Permission, PermissionAdmin)


class TeamRoleAdmin(admin.ModelAdmin):
    fields = ['name', 'permission', 'status']
    list_display = ('name', 'status')


admin.site.register(TeamRole, TeamRoleAdmin)


class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'username', 'password', 'gender', 'dob', 'team', 'status']
    list_display = ('name', 'username', 'gender', 'dob', 'status')


admin.site.register(User, UserAdmin)
