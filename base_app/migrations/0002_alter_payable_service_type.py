# Generated by Django 4.0.5 on 2022-06-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payable',
            name='service_type',
            field=models.CharField(choices=[('GAS', 'Gas Service'), ('ELE', 'Electric Energy Service'), ('COM', 'TV/Phone/Internet'), ('TLL', 'Toll Service')], max_length=3),
        ),
    ]
