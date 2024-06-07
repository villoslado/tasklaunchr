# Generated by Django 5.0.6 on 2024-06-03 16:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="todoitem",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="todoitems",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="todolist",
            name="user",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="todoslists",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]