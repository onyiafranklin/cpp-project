# Generated by Django 2.1.15 on 2022-11-11 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('employer_firstname', models.CharField(max_length=200)),
                ('employer_lastname', models.CharField(max_length=200)),
                ('organization_name', models.CharField(max_length=200)),
                ('employer_email', models.EmailField(max_length=254)),
                ('employer_profile_picture', models.ImageField(blank=True, default='employer_pic/default-pp.JPG', null=True, upload_to='employer_pic/')),
                ('organization_address', models.TextField(default='no address')),
                ('about', models.TextField(default='short note about self')),
                ('source_link', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]