# Generated by Django 5.2.3 on 2025-06-23 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
