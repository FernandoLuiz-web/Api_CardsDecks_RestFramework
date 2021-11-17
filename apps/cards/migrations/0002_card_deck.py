# Generated by Django 3.2.9 on 2021-11-17 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0001_initial'),
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='decks.deck'),
            preserve_default=False,
        ),
    ]
