# Generated by Django 4.1.7 on 2023-03-07 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_generate_expiring_links_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('thumbnail_sizes', models.CharField(max_length=100)),
                ('original_link_enabled', models.BooleanField(default=False)),
                ('expiring_link_enabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='account_type',
        ),
        migrations.RemoveField(
            model_name='account',
            name='generate_expiring_links',
        ),
        migrations.RemoveField(
            model_name='account',
            name='include_original_link',
        ),
        migrations.RemoveField(
            model_name='account',
            name='thumbnail_size_200',
        ),
        migrations.RemoveField(
            model_name='account',
            name='thumbnail_size_400',
        ),
        migrations.AddField(
            model_name='account',
            name='account_tier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.accounttier'),
        ),
    ]
