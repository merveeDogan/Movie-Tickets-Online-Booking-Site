# Generated by Django 4.1.1 on 2023-01-02 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cinema",
            fields=[
                ("cinema_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=45)),
                ("district", models.CharField(max_length=45)),
                ("city", models.CharField(max_length=45)),
                ("zip_code", models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                "db_table": "cinema",
            },
        ),
        migrations.CreateModel(
            name="CinemaHall",
            fields=[
                ("cinema_hall_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "hall_size",
                    models.CharField(
                        choices=[("S", "Small"), ("M", "Medium"), ("L", "Large")],
                        max_length=1,
                    ),
                ),
                (
                    "cinema",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cinemium.cinema",
                    ),
                ),
            ],
            options={
                "db_table": "cinema_hall",
            },
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("movie_id", models.AutoField(primary_key=True, serialize=False)),
                ("poster", models.CharField(max_length=45)),
                ("genre", models.CharField(max_length=45)),
                ("date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("actors", models.CharField(max_length=45)),
                ("name", models.CharField(max_length=45)),
                ("director", models.CharField(max_length=45)),
                ("duration", models.CharField(max_length=45)),
                ("language", models.CharField(max_length=45)),
                ("about", models.CharField(max_length=1024)),
                ("score", models.FloatField(blank=True, default=None, null=True)),
                ("in_theatre", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "movie",
            },
        ),
        migrations.CreateModel(
            name="Show",
            fields=[
                ("show_id", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateTimeField(blank=True, null=True)),
                ("show_price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "cinema_hall",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cinemium.cinemahall",
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cinemium.movie"
                    ),
                ),
            ],
            options={
                "db_table": "show",
            },
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                ("ticket_id", models.AutoField(primary_key=True, serialize=False)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("purchase_time", models.DateTimeField(auto_now_add=True)),
                (
                    "show",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cinemium.show"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "ticket",
            },
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                ("payment_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "payment_date",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "ticket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cinemium.ticket",
                    ),
                ),
            ],
            options={
                "db_table": "payment",
            },
        ),
        migrations.CreateModel(
            name="CinemaSeat",
            fields=[
                (
                    "cinema_seat_id",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("booked_shows", models.CharField(default=False, max_length=1000)),
                ("row_no", models.CharField(max_length=45)),
                ("col_no", models.CharField(max_length=45)),
                ("ticket_id", models.CharField(blank=True, max_length=11, null=True)),
                (
                    "cinema_hall",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cinemium.cinemahall",
                    ),
                ),
            ],
            options={
                "db_table": "cinema_seat",
            },
        ),
    ]
