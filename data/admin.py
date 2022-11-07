from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Testing)
class TestingModel(admin.ModelAdmin):
    search_fields = ('kode', 'nama')
    list_filter = ('kode', 'nama', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'kode', 'nama', 'created_at', 'updated_at', 'user')

@admin.register(Provinsi)
class TestingModel(admin.ModelAdmin):
    search_fields = ('kode', 'nama')
    list_filter = ('kode', 'nama', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'kode', 'nama', 'created_at', 'updated_at', 'user')