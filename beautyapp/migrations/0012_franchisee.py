# Generated by Django 2.2.6 on 2019-12-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0011_auto_20191209_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Franchisee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('mobileno', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=500)),
            ],
        ),
    ]
