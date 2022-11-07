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

class Provinsi(models.Model):
    class Meta:
        verbose_name = 'Provinsi'
        verbose_name_plural = 'Provinsi'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    kode = models.CharField(max_length=2)
    nama = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama