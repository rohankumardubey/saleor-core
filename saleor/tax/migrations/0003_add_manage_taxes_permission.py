# Generated by Django 3.2.13 on 2022-05-27 13:17

from django.db import migrations
from django.db.models.signals import post_migrate


def assign_permissions(apps, schema_editor):
    def on_migrations_complete(sender=None, **kwargs):
        Permission = apps.get_model("auth", "Permission")
        Group = apps.get_model("auth", "Group")
        ContentType = apps.get_model("contenttypes", "ContentType")

        ct, _ = ContentType.objects.get_or_create(app_label="tax", model="taxclass")
        manage_taxes, _ = Permission.objects.get_or_create(
            name="Manage taxes.", content_type=ct, codename="manage_taxes"
        )

        # Assign MANAGE_TAXES to groups with MANAGE_SETTINGS
        groups = Group.objects.filter(
            permissions__content_type__app_label="site",
            permissions__codename="manage_settings",
        )
        for group in groups:
            group.permissions.add(manage_taxes)

    post_migrate.connect(on_migrations_complete, weak=False)


class Migration(migrations.Migration):

    dependencies = [
        ("tax", "0002_add_default_tax_configs"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="taxclass",
            options={
                "ordering": ("is_default", "name", "pk"),
                "permissions": (("manage_taxes", "Manage taxes."),),
            },
        ),
        migrations.RunPython(assign_permissions, migrations.RunPython.noop),
    ]