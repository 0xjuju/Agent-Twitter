# Generated by Django 5.0.1 on 2024-04-18 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0015_alter_agent_max_consecutive_reply_and_more'),
        ('book', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('genre', models.CharField(default='', max_length=255)),
                ('source', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('initial_prompt', models.TextField(blank=True, default='')),
                ('story', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.story')),
                ('training_sources', models.ManyToManyField(to='agents.trainingsource')),
            ],
        ),
    ]