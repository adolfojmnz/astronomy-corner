# Generated by Django 4.0 on 2021-12-28 16:46

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apod', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('apods', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apod.apod')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, users.models.GetReversedURL),
        ),
    ]