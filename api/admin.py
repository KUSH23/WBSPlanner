from django.contrib import admin
from .models import MGroup, MSGroup

# Register your models here.

class MGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('mgroup_name',)}
    list_display = ('mgroup_name', 'slug')

class MSGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('msgroup_name',)}
    list_display = ('msgroup_name', 'slug')

admin.site.register(MGroup, MGroupAdmin)

admin.site.register(MSGroup, MSGroupAdmin)
