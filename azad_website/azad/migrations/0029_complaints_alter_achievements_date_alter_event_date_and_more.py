# Generated by Django 4.2.5 on 2023-10-14 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azad', '0028_alter_achievements_date_alter_azad_boarders_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll_no', models.CharField(max_length=15)),
                ('emails', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=12, null=True)),
                ('room_no', models.CharField(max_length=5)),
                ('complain', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=10)),
                ('review', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='achievements',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 14, 23, 9, 34, 411293)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 14, 23, 9, 34, 411293)),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 14, 23, 9, 34, 411293)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 14, 23, 9, 34, 411293)),
        ),
        migrations.AlterField(
            model_name='para',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 14, 23, 9, 34, 411293)),
        ),
    ]
