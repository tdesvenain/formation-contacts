# Generated by Django 2.0.7 on 2018-07-16 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_person_function'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('zipcode', models.CharField(max_length=50, verbose_name='zipcode')),
                ('address', models.CharField(max_length=200, verbose_name='address')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person')),
            ],
        ),
    ]