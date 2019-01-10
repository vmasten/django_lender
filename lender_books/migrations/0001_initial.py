# Generated by Django 2.1.5 on 2019-01-09 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(upload_to='')),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('year', models.CharField(max_length=4)),
                ('status', models.CharField(choices=[('AV', 'available'), ('CO', 'checked out')], default='AV', max_length=2)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_borrowed', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
