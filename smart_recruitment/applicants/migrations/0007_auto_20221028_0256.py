# Generated by Django 2.1.15 on 2022-10-28 02:56

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('applicants', '0006_auto_20221028_0250'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
    ]
