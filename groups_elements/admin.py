from django.contrib import admin

from .models import Group, Element


class ElementTabularInline(admin.TabularInline):
    model = Element


class GroupAdmin(admin.ModelAdmin):
    inlines = [ElementTabularInline]

    class Meta:
        model = Group


admin.site.register(Group, GroupAdmin)
admin.site.register(Element)
