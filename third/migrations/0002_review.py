# Generated by Django 3.2.6 on 2021-09-14 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('third', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField()),
                ('comment', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='third.restaurant')),
            ],
        ),
    ]
