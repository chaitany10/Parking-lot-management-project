# Generated by Django 2.1 on 2019-11-04 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=20)),
                ('firstname', models.CharField(blank=True, max_length=50)),
                ('lastname', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Regular_Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('purchase_date', models.DateField(auto_now=True)),
                ('start_date', models.DateField(auto_now=True)),
                ('pass_cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Numbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_no', models.CharField(max_length=20)),
                ('vehicle_height', models.FloatField(default=1.5)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('cost', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.Regular_Customer')),
                ('duration', models.IntegerField(default=30)),
            ],
        ),
        migrations.AddField(
            model_name='regular_customer',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer'),
        ),
    ]
