# Generated by Django 3.2.5 on 2021-07-31 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
