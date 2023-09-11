# Generated by Django 4.1.6 on 2023-08-07 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_remove_user_password1_remove_user_password2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]