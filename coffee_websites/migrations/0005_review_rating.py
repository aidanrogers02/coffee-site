# Generated by Django 4.2.19 on 2025-02-11 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_websites', '0004_review_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5),
            preserve_default=False,
        ),
    ]
