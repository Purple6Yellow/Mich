# Generated by Django 5.2.1 on 2025-07-01 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chelping', '0002_alter_contact_leeftijd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='leeftijd',
            field=models.CharField(choices=[('5', '5'), ('6', '6'), ('17', '17')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='niveau',
            field=models.CharField(choices=[('0', 'basisschool'), ('1', 'vmbo'), ('2', 'havo'), ('3', 'vwo')], default='onbekend', max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='training',
            field=models.CharField(choices=[('RT', 'Remidial Teaching'), ('LL', 'Leer Leren'), ('NL', 'Nederlands'), ('FA', 'Faalangst training')], default='Onbekend', max_length=30, null=True),
        ),
    ]
