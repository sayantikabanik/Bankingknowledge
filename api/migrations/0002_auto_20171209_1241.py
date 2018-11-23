
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='city',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='branch',
            name='state',
            field=models.CharField(max_length=40),
        ),
    ]
