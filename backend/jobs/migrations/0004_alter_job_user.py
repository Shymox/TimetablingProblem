# Generated by Django 3.2 on 2021-05-11 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0003_auto_20210511_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL),
        ),
    ]
