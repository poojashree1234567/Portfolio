# Generated by Django 4.2 on 2024-07-20 18:05

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
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=200)),
                ('skill_percentage', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='porfile')),
                ('timeline_image', models.ImageField(blank=True, null=True, upload_to='timeline')),
                ('profession', models.CharField(blank=True, max_length=200, null=True)),
                ('thread_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('linkdin_url', models.URLField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('degree', models.CharField(blank=True, choices=[('1', 'Masters'), ('2', 'Under Graduate'), ('3', 'Graduate'), ('4', 'Diploma')], max_length=30, null=True)),
                ('country_code', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=12)),
                ('address', models.TextField(blank=True, max_length=100, null=True)),
                ('freelance', models.CharField(blank=True, choices=[('1', 'Avalaible'), ('2', 'Not avalaible')], max_length=20, null=True)),
                ('happy_client', models.IntegerField(blank=True, null=True)),
                ('projects', models.IntegerField(blank=True, null=True)),
                ('hr_of_support', models.IntegerField(blank=True, null=True)),
                ('hard_work', models.IntegerField(blank=True, null=True)),
                ('i_agree', models.BooleanField(blank=True, default=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
