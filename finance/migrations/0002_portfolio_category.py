# Generated by Django 4.2 on 2023-04-21 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='category',
            field=models.CharField(default='large', max_length=100),
            preserve_default=False,
        ),
    ]
