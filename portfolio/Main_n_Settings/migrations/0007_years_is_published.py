# Generated by Django 5.1.1 on 2024-10-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_n_Settings', '0006_services_skills_years_delete_contacts_main_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='years',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опублікувати'),
        ),
    ]
