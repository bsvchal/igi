# Generated by Django 5.0.5 on 2024-05-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_pieceofnews_added_alter_faq_added_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='timezone',
            field=models.CharField(default='UTC', max_length=32),
        ),
    ]
