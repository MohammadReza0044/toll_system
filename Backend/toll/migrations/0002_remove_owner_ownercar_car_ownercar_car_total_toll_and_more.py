# Generated by Django 4.1.5 on 2023-01-20 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='ownerCar',
        ),
        migrations.AddField(
            model_name='car',
            name='ownerCar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='toll.owner'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='total_toll',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='lenght',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='car',
            name='load_valume',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='total_toll_paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='road',
            name='geom',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='road',
            name='width',
            field=models.DecimalField(decimal_places=15, max_digits=16),
        ),
    ]
