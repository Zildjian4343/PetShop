# Generated by Django 5.0.3 on 2024-05-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petStoreApp', '0029_order_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
