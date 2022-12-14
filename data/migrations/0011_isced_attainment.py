# Generated by Django 4.1.3 on 2022-11-29 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0010_spesies_nama_indonesia_spesies_nama_inggris_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ISCED_Attainment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kode_level', models.CharField(max_length=1)),
                ('deskripsi_level', models.TextField()),
                ('kode_category', models.CharField(max_length=2)),
                ('deskripsi_category', models.TextField()),
                ('kode_subcategory', models.CharField(max_length=3)),
                ('deskripsi_subcategory', models.TextField()),
                ('dasar_hukum', models.CharField(max_length=120)),
                ('status_data', models.CharField(choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')], max_length=11, verbose_name='Status Data')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Klasifikasi Baku Pendidikan',
                'verbose_name_plural': 'Klasifikasi Baku Pendidikan',
            },
        ),
    ]
