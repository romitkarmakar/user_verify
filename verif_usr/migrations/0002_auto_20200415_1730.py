# Generated by Django 3.0.2 on 2020-04-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verif_usr', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='city_of_recidence',
            new_name='city_of_residence',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='country_of_recidence',
            new_name='country_of_residence',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=30),
        ),
    ]