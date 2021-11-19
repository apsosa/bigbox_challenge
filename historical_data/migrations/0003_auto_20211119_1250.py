# encoding: utf8
from django.db import models, migrations
from datetime import date

def load_data(apps, schema_editor):
    PriceHistory = apps.get_model("historical_data", "PriceHistory")

    PriceHistory(date=date(2021,11,19),
         price=1234.00,
         volume=3546,
         total_price=1254,
         ).save()
    PriceHistory(date=date(2021,11,19),
         price=12.15,
         volume=1879,
         total_price=1545,
         ).save()
class Migration(migrations.Migration):

    dependencies = [
        ('historical_data', '0002_auto_20211119_1250'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
