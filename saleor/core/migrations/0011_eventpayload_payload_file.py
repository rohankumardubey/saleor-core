# Generated by Django 3.2.23 on 2024-03-06 17:10

from django.db import migrations, models

from saleor.core.storages import private_storage


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_drop_vatlayer_tables"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventpayload",
            name="payload_file",
            field=models.FileField(
                null=True, storage=private_storage, upload_to="payloads"
            ),
        ),
        migrations.AlterField(
            model_name="eventpayload",
            name="payload",
            field=models.TextField(default=""),
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE core_eventpayload
            ALTER COLUMN payload
            SET DEFAULT '';
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
