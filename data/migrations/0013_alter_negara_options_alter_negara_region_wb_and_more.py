# Generated by Django 4.1.3 on 2022-12-05 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_remove_iucn_habitat_asal_negara_iucn_habitat_asal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='negara',
            options={'verbose_name': 'Negara', 'verbose_name_plural': 'Negara'},
        ),
        migrations.AlterField(
            model_name='negara',
            name='region_wb',
            field=models.CharField(choices=[('Antarctica', 'Antarctica'), ('East Asia & Pacific', 'East Asia & Pacific'), ('Europe & Central Asia', 'Europe & Central Asia'), ('Latin America & Caribbean', 'Latin America & Caribbean'), ('Middle East & North Africa', 'Middle East & North Africa'), ('North America', 'North America'), ('South Asia', 'South Asia'), ('Sub-Saharan Africa', 'Sub-Saharan Africa')], max_length=30, verbose_name='Region World Bank'),
        ),
        migrations.AlterField(
            model_name='negara',
            name='subregion',
            field=models.CharField(choices=[('Antarctica', 'Antarctica'), ('Australia and New Zealand', 'Australia and New Zealand'), ('Caribbean', 'Caribbean'), ('Central America', 'Central America'), ('Central Asia', 'Central Asia'), ('Eastern Africa', 'Eastern Africa'), ('Eastern Asia', 'Eastern Asia'), ('Eastern Europe', 'Eastern Europe'), ('Melanesia', 'Melanesia'), ('Micronesia', 'Micronesia'), ('Middle Africa', 'Middle Africa'), ('Northern Africa', 'Northern Africa'), ('Northern America', 'Northern America'), ('Northern Europe', 'Northern Europe'), ('Polynesia', 'Polynesia'), ('Seven seas (open ocean)', 'Seven seas (open ocean)'), ('South America', 'South America'), ('South-Eastern Asia', 'South-Eastern Asia'), ('Southern Africa', 'Southern Africa'), ('Southern Asia', 'Southern Asia'), ('Southern Europe', 'Southern Europe'), ('Western Africa', 'Western Africa'), ('Western Asia', 'Western Asia'), ('Western Europe', 'Western Europe')], max_length=30),
        ),
        migrations.AlterField(
            model_name='spesies',
            name='species',
            field=models.CharField(max_length=100),
        ),
    ]
