# Generated by Django 4.1.7 on 2023-09-03 12:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="is_stuff",
            new_name="is_staff",
        ),
    ]
