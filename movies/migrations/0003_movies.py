# Generated by Django 3.0.5 on 2020-04-23 17:08

from django.db import migrations

def create_data(apps, schema_editor):
    Movie = apps.get_model('movies', 'Movie')
    Movie(first_name="Customer 001", last_name="Customer 001", email="customer001@email.com", phone="00000000", address="Customer 000 Address", description= "Customer 001 description").save()

class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200423_1706'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
