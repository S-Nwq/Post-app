# Generated by Django 5.2 on 2025-04-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='got.png', upload_to=''),
        ),
    ]
