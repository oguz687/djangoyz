# Generated by Django 2.1.7 on 2019-03-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tahmin',
            name='metin',
            field=models.TextField(blank=True, help_text='Metin giriniz.'),
        ),
    ]