# Generated by Django 5.1.3 on 2024-12-22 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_note_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="update_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]