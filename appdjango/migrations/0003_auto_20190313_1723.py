# Generated by Django 2.1.7 on 2019-03-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdjango', '0002_auto_20190313_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tahmin',
            name='beklenen',
            field=models.TextField(blank=True, default='ekonomi beklenen'),
        ),
        migrations.AlterField(
            model_name='tahmin',
            name='metin',
            field=models.TextField(blank=True, default='ekonomi metinleri', help_text='Metin giriniz.'),
        ),
        migrations.AlterField(
            model_name='tahmin',
            name='tahmin',
            field=models.TextField(blank=True, default='ekonomi'),
        ),
    ]
