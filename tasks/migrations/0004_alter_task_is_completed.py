# Generated by Django 4.1.2 on 2022-10-24 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_alter_task_due_date_alter_task_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="is_completed",
            field=models.BooleanField(editable=False),
        ),
    ]