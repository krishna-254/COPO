# Generated by Django 5.0.3 on 2025-01-23 05:33

import base.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attainment',
            fields=[
                ('name', models.CharField(default=django.utils.timezone.now, max_length=20, primary_key=True, serialize=False)),
                ('IA_1', models.IntegerField()),
                ('IA_2', models.IntegerField()),
                ('Assignment', models.IntegerField()),
                ('ESE', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CourseOutcome',
            fields=[
                ('name', models.CharField(default=django.utils.timezone.now, max_length=20, primary_key=True, serialize=False)),
                ('per1', models.IntegerField()),
                ('per2', models.IntegerField()),
                ('per3', models.IntegerField()),
                ('per4', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('user_type', models.CharField(choices=[('HOD', 'Head of Department'), ('Teaching Professor', 'Teaching Professor'), ('Admin', 'Admin')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CalculateExcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Theory', 'Theory'), ('Practical', 'Practical')], max_length=40)),
                ('semester', models.IntegerField()),
                ('file', models.FileField(upload_to=base.models.get_path)),
                ('attainment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.attainment')),
                ('userId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('courseOutCome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.courseoutcome')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(max_length=10)),
                ('division', models.CharField(default='A', max_length=1)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='base.department')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=20)),
                ('enrollment_id', models.CharField(max_length=20, unique=True)),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='base.class')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('class_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='base.class')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subjects', to='base.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='hod',
            field=models.ForeignKey(limit_choices_to={'user_type': 'HOD'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departments_as_hod', to='base.teacher'),
        ),
    ]
