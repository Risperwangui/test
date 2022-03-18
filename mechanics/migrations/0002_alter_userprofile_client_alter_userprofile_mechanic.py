# Generated by Django 4.0.3 on 2022-03-18 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mechanics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='client',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mechanics.client'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mechanic',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mechanics.mechanic'),
        ),
    ]
