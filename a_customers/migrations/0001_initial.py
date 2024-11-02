# Generated by Django 5.1.2 on 2024-11-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('type', models.CharField(choices=[('LEAD', 'lead'), ('PROSPECT', 'prospect'), ('CUSTOMER', 'customer')], max_length=8)),
                ('date_time_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
