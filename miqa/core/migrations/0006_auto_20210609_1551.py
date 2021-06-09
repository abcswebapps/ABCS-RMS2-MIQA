# Generated by Django 3.2.3 on 2021-06-09 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210601_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='session',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='experiments',
                to='core.session',
            ),
        ),
        migrations.AlterField(
            model_name='image',
            name='scan',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.scan'
            ),
        ),
        migrations.AlterField(
            model_name='scan',
            name='experiment',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='scans',
                to='core.experiment',
            ),
        ),
    ]
