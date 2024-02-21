# Generated by Django 5.0.2 on 2024-02-18 16:24

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('species', models.CharField(choices=[('cat', 'Кошка'), ('dog', 'Собака'), ('other', 'Другое')], max_length=10)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], max_length=10)),
                ('breed', models.CharField(blank=True, choices=[('siamese', 'Сиамская'), ('persian', 'Персидская'), ('labrador', 'Лабрадор'), ('golden_retriever', 'Золотистый ретривер')], max_length=50)),
                ('image', models.ImageField(upload_to='uploads/animal/')),
                ('description', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=150)),
                ('phone', models.CharField(blank=True, default='', max_length=18)),
                ('date', models.DateTimeField(verbose_name=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.animal')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer')),
            ],
        ),
    ]