# Generated by Django 4.1.7 on 2023-05-02 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_student_appdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='appdate',
            field=models.CharField(max_length=20),
        ),
    ]