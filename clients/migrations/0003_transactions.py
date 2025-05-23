# Generated by Django 5.0.7 on 2024-08-21 12:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_clientprofile_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_phone', models.CharField(max_length=15)),
                ('order_id', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=15)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mgongwa', to=settings.AUTH_USER_MODEL)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daktari', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
