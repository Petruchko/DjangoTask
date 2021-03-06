# Generated by Django 4.0.5 on 2022-06-18 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tripweight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='truck_name',
            field=models.CharField(default=0, max_length=200, null=True, verbose_name='Название самосвала'),
        ),
        migrations.AlterField(
            model_name='truckmodel',
            name='model_name',
            field=models.CharField(default=0, max_length=200, null=True, verbose_name='Модель самосвала'),
        ),
        migrations.AlterField(
            model_name='trucktrip',
            name='model_name',
            field=models.ForeignKey(db_column='Модель', default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='tripweight.truckmodel'),
        ),
    ]
