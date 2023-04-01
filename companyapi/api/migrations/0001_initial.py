# Generated by Django 4.1.7 on 2023-03-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobile Phones', 'Mobile Phones')], max_length=100)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active_models', models.BooleanField(default=True)),
            ],
        ),
    ]
