# Generated by Django 4.2.16 on 2024-10-25 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_note"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="note",
            field=models.CharField(max_length=200),
        ),
    ]
