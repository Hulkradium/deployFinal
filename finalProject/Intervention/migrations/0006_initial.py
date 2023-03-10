# Generated by Django 4.1.4 on 2023-02-21 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Intervention', '0005_remove_student_mentor_delete_intervention_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('lect_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('lect_name', models.TextField()),
                ('lect_email', models.TextField()),
                ('department', models.CharField(max_length=3)),
                ('password', models.TextField(default='null')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stud_id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('stud_name', models.TextField()),
                ('stud_phone', models.CharField(max_length=12)),
                ('course', models.CharField(max_length=4)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Intervention.lecturer')),
            ],
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_report', models.DateField()),
                ('description', models.TextField()),
                ('action', models.TextField()),
                ('category', models.TextField()),
                ('int_lect_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Intervention.lecturer')),
                ('int_stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Intervention.student')),
            ],
        ),
    ]
