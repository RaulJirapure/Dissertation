# Generated by Django 4.0.3 on 2022-04-28 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterDegrees', '0006_masterdegrees_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterdegrees',
            name='code',
            field=models.CharField(max_length=200),
        ),
    ]
