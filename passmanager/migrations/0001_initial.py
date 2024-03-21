# Generated by Django 4.1.7 on 2024-03-21 13:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PassManager",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "social_network",
                    models.CharField(max_length=50, verbose_name="Red Social"),
                ),
                (
                    "username",
                    models.CharField(max_length=150, verbose_name="Nombre de usuario"),
                ),
                (
                    "password",
                    models.CharField(max_length=250, verbose_name="Contraseña"),
                ),
            ],
        ),
    ]
