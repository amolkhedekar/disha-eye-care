# Generated by Django 4.0.3 on 2022-04-07 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0003_timeslot_doctortimeslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctortimeslot',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
