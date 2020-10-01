# Generated by Django 2.2.14 on 2020-09-26 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=50)),
                ('course', models.CharField(choices=[('All Available', 'All Available'), ('Bsc Computer Science', 'Bsc Computer Science'), ('Bsc in Commerce', 'Bsc in Commerce'), ('Bsc Quantity Survey', 'Bsc Quantity Survey')], default='Available Courses', max_length=100)),
                ('location', models.CharField(max_length=30)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
