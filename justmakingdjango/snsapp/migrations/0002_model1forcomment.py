# Generated by Django 4.0.5 on 2022-06-18 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model1forComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('foreign_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='snsapp.model1forupload')),
            ],
        ),
    ]
