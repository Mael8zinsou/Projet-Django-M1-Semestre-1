# Generated by Django 5.1.2 on 2024-11-03 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_app", "0001_initial"),
        ("home_app", "0003_file_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="folder",
            name="group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="folders",
                to="auth_app.group",
            ),
        ),
        migrations.AlterField(
            model_name="file",
            name="group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="files",
                to="auth_app.group",
            ),
        ),
    ]
