# Generated by Django 5.0.1 on 2024-02-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_rename__llm_config_agent_llm_config'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='llmconfig',
            name='config_list',
        ),
        migrations.AddField(
            model_name='llmconfig',
            name='api_key',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='llmconfig',
            name='model',
            field=models.CharField(default='', max_length=255),
        ),
    ]
