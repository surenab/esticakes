# Generated by Django 2.1.5 on 2019-11-02 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_cake_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cake',
            old_name='price_10inch',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='image6',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='image7',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='image8',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='price_12inch',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='price_8inch',
        ),
    ]