# Generated by Django 5.0.1 on 2024-02-12 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('username', models.CharField(default='', max_length=255, unique=True)),
                ('user_id', models.BigIntegerField(default=0)),
                ('website', models.URLField(max_length=255)),
                ('linkedin', models.URLField(max_length=255)),
                ('medium', models.URLField(max_length=255)),
            ],
        ),
    ]
