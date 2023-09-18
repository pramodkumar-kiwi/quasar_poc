# Generated by Django 4.2.2 on 2023-07-06 12:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_engine', '0001_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openaiconfig',
            name='temperature',
            field=models.FloatField(default=0.3, help_text='Temperature range will be 0 - 1.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
    ]