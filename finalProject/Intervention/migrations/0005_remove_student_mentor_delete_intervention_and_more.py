# Generated by Django 4.1.4 on 2023-02-21 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Intervention', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='mentor',
        ),
        migrations.DeleteModel(
            name='Intervention',
        ),
        migrations.DeleteModel(
            name='Lecturer',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
