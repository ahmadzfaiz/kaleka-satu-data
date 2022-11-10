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
    fieldsets = [
        ('Provinsi', {'fields': ('kode_prov', 'nama_prov')}),
        ('Kabupaten/Kota', {'fields': ('kode_kabkot', 'nama_kabkot')}),
        ('Kecamatan', {'fields': ('kode_kec', 'nama_kec')}),
        ('Desa/Kelurahan', {'fields': ('kode_desa', 'nama_desa')}),
        ('Metadata', {'fields': ('dasar_hukum', 'status_data')})
    ]

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

@admin.register(KBJI)
class KBJIModel(admin.ModelAdmin):
    search_fields = ('golongan_pokok', 'subgolongan_pokok', 'golongan', 'subgolongan', 'jabatan')
    list_filter = ('kode_gol_pokok', 'kode_subgol_pokok', 'kode_gol', 'kode_subgol', 'kode_jabatan', 'dasar_hukum', 'status_data', 'created_at', 'updated_at', 'user')
    fieldsets = [
        ('Golongan Pokok', {'fields': ('golongan_pokok', 'kode_gol_pokok')}),
        ('Sub-Golongan Pokok', {'fields': ('subgolongan_pokok', 'kode_subgol_pokok')}),
        ('Golongan', {'fields': ('golongan', 'kode_gol')}),
        ('Sub-Golongan', {'fields': ('subgolongan', 'kode_subgol')}),
        ('Jabatan', {'fields': ('jabatan', 'kode_jabatan')}),
        ('Metadata', {'fields': ('dasar_hukum', 'status_data')})
    ]

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()

@admin.register(Profesi)
class ProfesiModel(admin.ModelAdmin):
    search_fields = ('nama',)
    list_filter = ('nama', 'kode_kbji', 'created_at', 'updated_at', 'user')
    raw_id_fields = ('kode_kbji',)
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()

@admin.register(Orang)
class OrangModel(admin.ModelAdmin):
    search_fields = ('nama_lengkap',)
    list_filter = ('nik', 'nama_lengkap', 'jenis_kelamin', 'tempat_lahir', 'tanggal_lahir', 'status_kawin', 'profesi', 'rt', 'rw', 'alamat', 'created_at', 'updated_at', 'user')
    filter_horizontal = ('profesi',)
    raw_id_fields = ('alamat',)
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()