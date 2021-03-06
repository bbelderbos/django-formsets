# Generated by Django 3.2.5 on 2021-07-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image_link', models.URLField(blank=True, null=True)),
                ('inserted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
