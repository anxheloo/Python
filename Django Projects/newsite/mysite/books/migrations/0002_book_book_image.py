# Generated by Django 4.1.6 on 2023-02-15 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
