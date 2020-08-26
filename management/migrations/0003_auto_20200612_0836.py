# Generated by Django 3.0.4 on 2020-06-12 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20200605_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField(verbose_name='')),
                ('password', models.CharField(max_length=20)),
                ('profile_picture', models.ImageField(blank=True, upload_to='students_profiles/')),
                ('mobile', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('student_id', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
            },
        ),
        migrations.AlterField(
            model_name='teachermodal',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.ClassRoom')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Student_info')),
            ],
            options={
                'verbose_name': 'Student_class',
                'verbose_name_plural': 'Student_class',
            },
        ),
    ]
