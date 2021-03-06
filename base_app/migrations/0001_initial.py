# Generated by Django 4.0.5 on 2022-06-18 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payable',
            fields=[
                ('bar_code', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('service_type', models.CharField(max_length=15)),
                ('service_description', models.CharField(max_length=30)),
                ('due_date', models.DateField()),
                ('service_cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payment_status', models.CharField(choices=[('PD', 'Paid'), ('PG', 'Pending'), ('IC', 'In Claim')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_method', models.CharField(choices=[('CC', 'Credit Card'), ('DC', 'Debt Card'), ('CS', 'Cash')], max_length=2)),
                ('card_number', models.DecimalField(decimal_places=0, max_digits=16)),
                ('payment_ammount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payment_date', models.DateField()),
                ('bar_code', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='base_app.payable')),
            ],
        ),
    ]
