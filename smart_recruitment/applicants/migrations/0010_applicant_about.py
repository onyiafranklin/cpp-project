# Generated by Django 2.1.15 on 2022-10-31 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0009_applicant_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='about',
            field=models.TextField(default='short note about self'),
        ),
    ]
