# Generated by Django 3.2.5 on 2021-07-13 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_content', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogger_id', to=settings.AUTH_USER_MODEL)),
                ('fans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fans_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]