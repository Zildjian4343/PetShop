# Generated by Django 5.0.3 on 2024-05-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petStoreApp', '0019_alter_order_is_completed_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='pet_label',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
