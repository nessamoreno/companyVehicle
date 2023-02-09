# Generated by Django 3.2.8 on 2023-02-09 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.IntegerField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField(max_length=10)),
                ('age', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.IntegerField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=6, unique=True)),
                ('veh_typ_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyCar.vehicletype')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('final_date', models.DateTimeField(auto_now_add=True)),
                ('cli_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cli_id', to='companyCar.client')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emp_id', to='companyCar.employee')),
                ('veh_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veh_id', to='companyCar.vehicle')),
            ],
        ),
    ]
