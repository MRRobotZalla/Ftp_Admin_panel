# Generated by Django 2.2.6 on 2019-10-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20191002_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='license_key',
            field=models.CharField(default='6Bp6DuXWCuPIMIiyEn1h', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
