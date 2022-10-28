# Generated by Django 2.1.15 on 2022-10-28 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0004_auto_20221028_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('choose no to say', 'choose not to say')], default='choose gender', max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='nationality',
            field=models.CharField(default='your country', max_length=200),
        ),
    ]
