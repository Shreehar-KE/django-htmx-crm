# Generated by Django 5.1.2 on 2024-11-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_contacts', '0003_alter_contact_contact_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_id',
            field=models.BigIntegerField(blank=True, editable=False, null=True, unique=True),
        ),
    ]
