# Generated by Django 2.2.4 on 2021-06-01 13:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
