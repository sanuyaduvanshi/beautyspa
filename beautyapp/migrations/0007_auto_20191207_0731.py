# Generated by Django 2.2.6 on 2019-12-07 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0006_auto_20191207_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carriers',
            name='fileupload',
            field=models.FileField(upload_to='resume/pdfs/'),
        ),
    ]