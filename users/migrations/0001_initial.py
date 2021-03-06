# Generated by Django 2.2.14 on 2020-09-26 08:51

import cloudinary_storage.storage
from django.db import migrations, models
import django.db.models.deletion
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=100, verbose_name='Title')),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='books/pdfs/', validators=[users.validators.validate_file_extension])),
                ('cover', models.ImageField(blank=True, null=True, upload_to='books/covers/')),
                ('pub_date', models.DateField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='users.Course')),
            ],
        ),
    ]
