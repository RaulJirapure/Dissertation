# Generated by Django 4.0.3 on 2022-04-12 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterDegrees', '0004_rename_master_code_masterdegrees_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='credits',
            field=models.IntegerField(default=10),
        ),
    ]