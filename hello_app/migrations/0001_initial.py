# Generated by Django 5.1.5 on 2025-01-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomepageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='homepage_images/')),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
