# Generated by Django 3.1.5 on 2021-01-21 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_usersignupdb_dateofreg'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersignupdb',
            name='dateOfReg',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
