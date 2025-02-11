# Generated by Django 5.1.1 on 2024-09-10 15:22

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название цвета автомобиля')),
            ],
            options={
                'verbose_name': 'Цвет автомобиля',
                'verbose_name_plural': 'Цвета автомобилей',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название страны автомобиля')),
            ],
            options={
                'verbose_name': 'Страна автомобиля',
                'verbose_name_plural': 'Страны автомобилей',
            },
        ),
        migrations.CreateModel(
            name='KppType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название КПП автомобиля')),
            ],
            options={
                'verbose_name': 'Вид КПП автомобиля',
                'verbose_name_plural': 'Виды КПП автомобилей',
            },
        ),
        migrations.CreateModel(
            name='Kuzov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название кузова автомобиля')),
            ],
            options={
                'verbose_name': 'Кузов автомобиля',
                'verbose_name_plural': 'Кузова автомобилей',
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название марки автомобиля')),
            ],
            options={
                'verbose_name': 'Марка автомобиля',
                'verbose_name_plural': 'Марки автомобилей',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название модели автомобиля')),
            ],
            options={
                'verbose_name': 'Модель автомобиля',
                'verbose_name_plural': 'Модели автомобилей',
            },
        ),
        migrations.CreateModel(
            name='Privod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название привода автомобиля')),
            ],
            options={
                'verbose_name': 'Вид привода автомобиля',
                'verbose_name_plural': 'Виды приводов автомобилей',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_date', models.DateField(verbose_name='Дата аукциона')),
                ('auction', models.TextField(verbose_name='Название аукциона')),
                ('year', models.IntegerField(max_length=10, verbose_name='Год автомобиля')),
                ('eng_v', models.IntegerField(max_length=10)),
                ('pw', models.TextField()),
                ('grade', models.TextField()),
                ('mileage', models.IntegerField(max_length=50, verbose_name='Пробег')),
                ('equip', models.TextField()),
                ('rate', models.CharField(max_length=10)),
                ('finish', models.IntegerField(max_length=50)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), size=3, verbose_name='Фотографии')),
                ('true_priv', models.TextField()),
                ('true_color', models.TextField()),
                ('color_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.color', verbose_name='Цвет автомобиля')),
                ('country_id', models.ForeignKey(default='Japan', on_delete=django.db.models.deletion.CASCADE, to='cars.country', verbose_name='Страна автомобиля')),
                ('kpp_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.kpptype', verbose_name='КПП автомобиля')),
                ('kuzov_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.kuzov', verbose_name='Кузов автомобиля')),
                ('mark_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.mark', verbose_name='Марка автомобиля')),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.model', verbose_name='Модель автомобиля')),
                ('priv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.privod', verbose_name='Привод автомобиля')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]
