# Generated by Django 3.2.5 on 2021-07-31 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadingdate', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=30)),
                ('Subject', models.CharField(max_length=30)),
                ('notesfile', models.FileField(null=True, upload_to='')),
                ('filetype', models.CharField(max_length=10)),
                ('description', models.FileField(max_length=200, upload_to='')),
                ('status', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
