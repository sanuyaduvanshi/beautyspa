# Generated by Django 2.2 on 2019-12-14 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0002_auto_20191214_1902'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addstaff',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beautyapp.Citys'),
        ),
        migrations.AddField(
            model_name='guest',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beautyapp.Citys'),
        ),
    ]