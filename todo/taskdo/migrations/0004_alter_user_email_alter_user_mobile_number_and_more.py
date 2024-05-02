# Generated by Django 4.2.6 on 2023-10-27 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskdo", "0003_user_mobile_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="mobile_number",
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]