# Generated by Django 4.1.3 on 2022-11-21 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0007_alter_kbji_dasar_hukum_sitc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spesies',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kingdom', models.CharField(max_length=50)),
                ('phylum', models.CharField(max_length=50)),
                ('Class', models.CharField(max_length=50)),
                ('order', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=50)),
                ('genus', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=50)),
                ('dasar_hukum', models.CharField(max_length=60)),
                ('status_data', models.CharField(choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')], max_length=11, verbose_name='Status Data')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Klasifikasi Baku Spesies',
                'verbose_name_plural': 'Klasifikasi Baku Spesies',
            },
        ),
    ]
