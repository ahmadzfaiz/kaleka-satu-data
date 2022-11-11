from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Testing(models.Model):
    class Meta:
        verbose_name = 'Testing Data'
        verbose_name_plural = 'Testing Data'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    kode = models.CharField(max_length=5)
    nama = models.CharField(max_length=30)
    deskripsi = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

class Alamat(models.Model):
    class Meta:
        verbose_name = 'Alamat'
        verbose_name_plural = 'Alamat'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    kode_prov = models.CharField(max_length=2, verbose_name='Kode Provinsi')
    nama_prov = models.CharField(max_length=30, verbose_name='Nama Provinsi', help_text="Tuliskan nama provinsi tanpa imbuhan 'Provinsi', 'Prov.' dsb. Tulisan akan otomatis terkonversi menjadi huruf kapital.")
    kode_kabkot = models.CharField(max_length=4, verbose_name='Kode Kabupaten/Kota')
    nama_kabkot = models.CharField(max_length=30, verbose_name='Nama Kabupaten/Kota', help_text="Tuliskan nama kabupaten tanpa imbuhan 'Kabupaten', 'Kab.' dsb. Untuk nama kota, gunakan imbuhan 'Kota'. Tulisan akan otomatis terkonversi menjadi huruf kapital.")
    kode_kec = models.CharField(max_length=6, verbose_name='Kode Kecamatan')
    nama_kec = models.CharField(max_length=30, verbose_name='Nama Kecamatan', help_text="Tuliskan nama kecamatan tanpa imbuhan 'Kecamatan', 'Kec.' dsb. Tulisan akan otomatis terkonversi menjadi huruf kapital.")
    kode_desa = models.CharField(max_length=10, unique=True, verbose_name='Kode Desa/Kelurahan')
    nama_desa = models.CharField(max_length=30, verbose_name='Nama Desa/Kelurahan', help_text="Tuliskan nama desa tanpa imbuhan 'Desa', 'Ds.' dsb. Untuk nama kelurahan, gunakan imbuhan 'Kel.'. Tulisan akan otomatis terkonversi menjadi huruf kapital.")
    dasar_hukum = models.CharField(max_length=30, verbose_name='Dasar Hukum')
    status_data = models.CharField(max_length=11, verbose_name='Status Data', choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_desa
    
    def save(self, *args, **kwargs):
        self.nama_prov = self.nama_prov.upper()
        self.nama_kabkot = self.nama_kabkot.upper()
        self.nama_kec = self.nama_kec.upper()
        self.nama_desa = self.nama_desa.upper()
        return super(Alamat, self).save(*args, **kwargs)

class KodePos(models.Model):
    class Meta:
        verbose_name = 'Kode Pos'
        verbose_name_plural = 'Kode Pos'
    
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    kode = models.CharField(max_length=5)
    alamat = models.ForeignKey(Alamat, on_delete=models.CASCADE)
    dasar_hukum = models.CharField(max_length=30, verbose_name='Dasar Hukum')
    status_data = models.CharField(max_length=11, verbose_name='Status Data', choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.kode

class KBJI(models.Model):
    class Meta:
        verbose_name = 'Klasifikasi Baku Jabatan'
        verbose_name_plural = 'Klasifikasi Baku Jabatan'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    kode_gol_pokok = models.PositiveSmallIntegerField(verbose_name='Kode Golongan Pokok')
    golongan_pokok = models.CharField(max_length=50, verbose_name='Nama Golongan Pokok', help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.')
    kode_subgol_pokok = models.PositiveSmallIntegerField(verbose_name='Kode Sub-Golongan Pokok')
    subgolongan_pokok = models.CharField(max_length=50, verbose_name='Nama Sub-Golongan Pokok', help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.')
    kode_gol = models.PositiveSmallIntegerField(verbose_name='Kode Golongan')
    golongan = models.CharField(max_length=50, verbose_name='Nama Golongan', help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.')
    kode_subgol = models.PositiveSmallIntegerField(verbose_name='Kode Sub-Golongan')
    subgolongan = models.CharField(max_length=50, verbose_name='Nama Sub-Golongan', help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.')
    kode_jabatan = models.DecimalField(max_digits=6, decimal_places=2, unique=True, verbose_name='Kode Jabatan')
    jabatan = models.CharField(max_length=50, verbose_name='Nama Jabatan', help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.')
    dasar_hukum = models.CharField(max_length=30)
    status_data = models.CharField(max_length=11, verbose_name='Status Data', choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.jabatan

class Profesi(models.Model):
    class Meta:
        verbose_name = 'Profesi'
        verbose_name_plural = 'Profesi'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nama = models.CharField(max_length=50)
    kode_kbji = models.ForeignKey(KBJI, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

class Orang(models.Model):
    class Meta:
        verbose_name = 'Orang'
        verbose_name_plural = 'Orang'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nik = models.PositiveBigIntegerField(verbose_name='Nomor Induk Kependudukan', unique=True)
    nama_lengkap = models.CharField(max_length=50, help_text='Nama sesuai KTP, tidak ditambahkan gelar.')
    jenis_kelamin = models.CharField(max_length=9, choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')])
    tempat_lahir = models.CharField(max_length=30, help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.')
    tanggal_lahir = models.DateField()
    status_kawin = models.CharField(max_length=11, choices=[('Belum Kawin', 'Belum Kawin'), ('Kawin', 'Kawin'), ('Cerai Hidup', 'Cerai Hidup'), ('Cerai Mati', 'Cerai Mati')])
    profesi = models.ManyToManyField(Profesi)
    rt = models.PositiveSmallIntegerField(verbose_name='RT')
    rw = models.PositiveSmallIntegerField(verbose_name='RW')
    alamat = models.ForeignKey(Alamat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_lengkap

    def save(self, *args, **kwargs):
        self.tempat_lahir = self.tempat_lahir.upper()
        return super(Orang, self).save(*args, **kwargs)