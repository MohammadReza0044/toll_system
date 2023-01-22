# Generated by Django 4.1.5 on 2023-01-22 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toll', '0002_remove_owner_ownercar_car_ownercar_car_total_toll_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traffic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toll.car')),
                ('road', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toll.road')),
            ],
        ),
    ]