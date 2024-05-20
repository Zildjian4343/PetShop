# Generated by Django 5.0.3 on 2024-05-02 21:22

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petStoreApp', '0012_remove_food_pet_delete_accessory_delete_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetProducts',
            fields=[
                ('pet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pet_name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Bird', 'Bird'), ('Fish', 'Fish')], max_length=100)),
                ('desc', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='pics')),
            ],
            managers=[
                ('pet', django.db.models.manager.Manager()),
            ],
        ),
    ]