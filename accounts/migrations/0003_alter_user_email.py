# Generated by Django 4.1 on 2022-12-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_user_groups_user_is_superuser_user_user_permissions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
