# Generated by Django 4.0.3 on 2022-04-07 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctor_certificate_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default=('Monday', 'Monday'), max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('half_time', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], default=('Morning', 'Morning'), max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorTimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('time_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.timeslot')),
            ],
        ),
    ]
