from django.contrib import admin

from apps.entity.models import CoordinateEntity, Label


@admin.register(CoordinateEntity)
class CoordinateEntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'x', 'y')


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
