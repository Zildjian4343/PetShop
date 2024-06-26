
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('pet_id', models.IntegerField(primary_key='True', serialize=False)),
                ('pet_name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Bird', 'Bird'), ('Fish', 'Fish')], max_length=100)),
                ('desc', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petStoreApp.pet')),
            ],
        ),
    ]
