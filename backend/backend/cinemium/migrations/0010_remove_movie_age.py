# Generated by Django 4.1.1 on 2022-12-28 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cinemium", "0009_remove_ticket_userid_movie_age_ticket_user_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="age",
        ),
    ]
