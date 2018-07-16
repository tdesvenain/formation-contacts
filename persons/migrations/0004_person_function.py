# Generated by Django 2.0.7 on 2018-07-16 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0001_initial'),
        ('persons', '0003_person_displayed'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='function',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='functions.Function'),
        ),
    ]
