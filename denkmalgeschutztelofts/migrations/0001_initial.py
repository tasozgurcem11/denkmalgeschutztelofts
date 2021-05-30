# Generated by Django 3.1.1 on 2020-11-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='not given!', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kontakt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='not given!', max_length=200)),
                ('telefon', models.CharField(default='not given!', max_length=200)),
                ('vorname', models.CharField(default='not given!', max_length=200)),
                ('nachname', models.CharField(default='not given!', max_length=200)),
                ('nachricht', models.CharField(default='kein nachricht', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('quelle', models.CharField(choices=[('KT', 'Kontakt'), ('KD', 'Kaiser und Dicke'), ('NS', 'Newsletter'), ('AN', 'Angebot')], default='KT', max_length=2)),
            ],
        ),
    ]