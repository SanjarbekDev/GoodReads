# Generated by Django 5.0.3 on 2024-03-19 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="profile_picture",
            field=models.ImageField(default="user-profile.png", upload_to=""),
        ),
    ]
