# Generated by Django 2.1.5 on 2019-11-02 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='category',
            field=models.CharField(choices=[('Muffins', 'Muffins'), ('Fondant Cakes', 'Fondant Cakes'), ('Cookies', 'Cookies'), ('Cakes', 'Cakes'), ('Desserts', 'Desserts')], default='Cakes', max_length=25, verbose_name='Category'),
        ),
    ]
