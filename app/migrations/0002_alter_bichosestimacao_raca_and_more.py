# Generated by Django 5.2 on 2025-04-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bichosestimacao',
            name='raca',
            field=models.CharField(choices=[('Coruja', 'Coruja'), ('Gato', 'Gato'), ('Leao', 'Leão'), ('Rato', 'Rato')], max_length=20),
        ),
        migrations.AlterField(
            model_name='personagemharrypotter',
            name='casa',
            field=models.CharField(choices=[('Grifinoria', 'Grifinória'), ('Lufa-Lufa', 'Lufa-Lufa'), ('Corvinal', 'Corvinal'), ('Sonserina', 'Sonserina')], max_length=25),
        ),
    ]
