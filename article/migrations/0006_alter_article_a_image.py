# Generated by Django 3.2.5 on 2021-07-12 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_a_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='a_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
