# Generated by Django 4.1.4 on 2023-05-04 05:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(11, 'Should be 11'), django.core.validators.MinValueValidator(1, 'Should be 1')]),
        ),
    ]
