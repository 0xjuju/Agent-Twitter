# Generated by Django 5.0.1 on 2024-02-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0009_agent__is_termination_message_agent_human_input_mode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
