# Generated by Django 4.0.4 on 2022-06-30 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steklohub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='static/media/interer/default.webp', upload_to='static/media/interer')),
            ],
        ),
    ]