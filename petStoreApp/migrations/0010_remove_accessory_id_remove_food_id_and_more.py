# Generated by Django 5.0.3 on 2024-05-02 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petStoreApp', '0009_alter_accessory_image_alter_food_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='food',
            name='id',
        ),
        migrations.AddField(
            model_name='accessory',
            name='accessory_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='food',
            name='food_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
