# Generated by Django 2.2.6 on 2019-12-06 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0003_carriers_fileuploads'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carriers',
            old_name='fileuploads',
            new_name='profile_pic',
        ),
    ]
