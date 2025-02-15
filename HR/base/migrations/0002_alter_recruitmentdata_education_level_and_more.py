# Generated by Django 5.0.7 on 2024-07-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitmentdata',
            name='education_level',
            field=models.IntegerField(choices=[(1, 'diploma'), (2, "Bachelor's"), (3, "Master's"), (4, 'PhD')]),
        ),
        migrations.AlterField(
            model_name='recruitmentdata',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')]),
        ),
        migrations.AlterField(
            model_name='recruitmentdata',
            name='recruitment_strategy',
            field=models.IntegerField(choices=[(1, 'Aggressive'), (2, 'Moderate'), (3, 'Conservative')]),
        ),
    ]
