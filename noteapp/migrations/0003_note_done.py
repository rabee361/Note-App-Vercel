# Generated by Django 4.2.5 on 2023-09-08 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0002_alter_note_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]