# Generated by Django 3.1.4 on 2021-05-16 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.JSONField(default=dict)),
                ('updated_by', models.JSONField(default=dict)),
                ('name', models.CharField(max_length=150)),
                ('address', models.TextField()),
                ('logo', models.URLField(null=True)),
                ('rating', models.JSONField(default=dict)),
                ('is_active', models.BooleanField(default=True)),
                ('location', models.TextField(default='https://maps.google.com/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Shop',
                'db_table': 'shops',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='shop',
            index=models.Index(fields=['name'], name='shops_name_0e1209_idx'),
        ),
    ]
