from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Testing)
class TestingModel(admin.ModelAdmin):
    search_fields = ('kode', 'nama')
    list_filter = ('kode', 'nama', 'created_at', 'updated_at', 'user')
    list_display = ('id', 'kode', 'nama', 'created_at', 'updated_at', 'user')
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()

@admin.register(Alamat)
class AlamatModel(admin.ModelAdmin):
    search_fields = ('nama_prov', 'nama_kabkot', 'nama_kec', 'nama_desa')
    list_filter = ('kode_prov', 'nama_prov', 
        'kode_kabkot', 'nama_kabkot', 
        'kode_kec', 'nama_kec',
        'kode_desa', 'nama_desa',
        'dasar_hukum', 'status_data',
        'created_at', 'updated_at', 'user')
    list_display = ('id', 'nama_prov', 'nama_kabkot', 'nama_kec', 'nama_desa', 'updated_at', 'user')
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()

@admin.register(KodePos)
class KodePosModel(admin.ModelAdmin):
    search_fields = ('kode',)
    list_filter = ('kode', 'dasar_hukum', 'status_data', 'created_at', 'updated_at', 'user')
    raw_id_fields = ('alamat',)
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()