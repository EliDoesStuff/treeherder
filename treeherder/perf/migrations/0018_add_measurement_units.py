# Generated by Django 2.2.4 on 2019-09-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('perf', '0017_assignment_support_for_alert_summaries'),
    ]

    operations = [
        migrations.AddField(
            model_name='performancesignature',
            name='measurement_unit',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
