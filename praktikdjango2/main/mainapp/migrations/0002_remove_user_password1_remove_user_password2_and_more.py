# Generated by Django 4.1.6 on 2023-08-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="password1",
        ),
        migrations.RemoveField(
            model_name="user",
            name="password2",
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=10),
        ),
    ]