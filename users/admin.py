from django.contrib import admin
from users.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


# Register your models here.
class GrahamAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # This is the case when obj is already created i.e. it's an edit
            return ['user']
        else:
            return []


class DirectorAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # This is the case when obj is already created i.e. it's an edit
            return ['user']
        else:
            return []


class CoordinadorAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # This is the case when obj is already created i.e. it's an edit
            return ['user']
        else:
            return []


class ProfesorAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # This is the case when obj is already created i.e. it's an edit
            return ['user']
        else:
            return []


class PadreDeFamiliaAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # This is the case when obj is already created i.e. it's an edit
            return ['user']
        else:
            return []


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('user_type',)}),
    )


admin.site.register(User, MyUserAdmin)
admin.site.register(Graham, GrahamAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Coordinador, CoordinadorAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(PadreDeFamilia, PadreDeFamiliaAdmin)


