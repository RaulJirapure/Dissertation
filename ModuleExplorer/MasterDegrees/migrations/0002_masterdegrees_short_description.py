# Generated by Django 4.0.3 on 2022-04-10 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterDegrees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterdegrees',
            name='short_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
