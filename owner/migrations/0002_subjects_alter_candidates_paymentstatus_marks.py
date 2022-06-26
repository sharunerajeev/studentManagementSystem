# Generated by Django 4.0.5 on 2022-06-15 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubjectName', models.CharField(default=None, max_length=100)),
                ('TotalHour', models.IntegerField(default=None)),
            ],
        ),
        migrations.AlterField(
            model_name='candidates',
            name='PaymentStatus',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attendance', models.IntegerField(default=None)),
                ('AttendancePercentage', models.IntegerField(blank=True, default=None, null=True)),
                ('AttendanceMark', models.IntegerField(blank=True, default=None, null=True)),
                ('Assignment1Mark', models.IntegerField(default=None)),
                ('Assignment2Mark', models.IntegerField(default=None)),
                ('TotalAssignmentMark', models.IntegerField(blank=True, default=None, null=True)),
                ('GdMark', models.IntegerField(default=None)),
                ('CpMark', models.IntegerField(default=None)),
                ('Total', models.IntegerField(blank=True, default=None, null=True)),
                ('StudentId', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='owner.candidates')),
                ('SubjectId', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='owner.subjects')),
            ],
        ),
    ]
