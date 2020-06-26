# Generated by Django 2.2.13 on 2020-06-26 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_roomName', to='home.Event')),
            ],
        ),
    ]
