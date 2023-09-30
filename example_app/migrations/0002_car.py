# Generated by Django 4.2.5 on 2023-09-29 23:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(choices=[('Toyota', 'Toyota'), ('Honda', 'Honda'), ('Ford', 'Ford'), ('Chevrolet', 'Chevrolet'), ('BMW', 'BMW'), ('Mercedes', 'Mercedes'), ('Acura', 'Acura'), ('Nissan', 'Nissan')], max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField(max_length=4, validators=[django.core.validators.MinLengthValidator(4)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('mileage', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
