# Generated by Django 2.2.3 on 2019-08-01 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_keterangan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=15)),
                ('port', models.CharField(max_length=15)),
                ('service', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Keterangan',
        ),
    ]
