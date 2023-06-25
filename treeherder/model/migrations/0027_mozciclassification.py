# Generated by Django 3.1.13 on 2021-12-22 12:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('model', '0026_bugscache_add_dupe_of_and_processed_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='MozciClassification',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                (
                    'result',
                    models.CharField(
                        max_length=7,
                        choices=[('BAD', 'bad'), ('GOOD', 'good'), ('UNKNOWN', 'unknown')],
                    ),
                ),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                (
                    'task_id',
                    models.CharField(
                        max_length=22, validators=[django.core.validators.MinLengthValidator(22)]
                    ),
                ),
                (
                    'push',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.push'),
                ),
            ],
            options={
                'db_table': 'mozci_classification',
            },
        ),
    ]
