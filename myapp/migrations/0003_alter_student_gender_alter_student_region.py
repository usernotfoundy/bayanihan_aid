# Generated by Django 4.1.7 on 2023-05-02 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_student_delete_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='region',
            field=models.CharField(choices=[('NCR', 'National Capital Region'), ('CAR', 'Cordillera Administrative Region'), ('REGION I', 'Ilocos Region'), ('REGION II', 'Cagayan Valley'), ('REGION III', 'Central Luzon'), ('REGION IV-A', 'Calabarzon'), ('REGION IV-B', 'Mimaropa'), ('REGION V', 'Bicol Region'), ('REGION VI', 'Western Visayas'), ('REGION VII', 'Central Visayas'), ('REGION VIII', 'Eastern Visayas'), ('REGION IX', 'Zamboanga Peninsula'), ('REGION X', 'Northern Mindanao'), ('REGION XI', 'Davao Region'), ('REGION XII', 'SOCCSKSARGEN'), ('CARAGA', 'Caraga'), ('BARMM', 'Bangsamoro Autonomous Region in Muslim Mindanao')], max_length=20),
        ),
    ]
