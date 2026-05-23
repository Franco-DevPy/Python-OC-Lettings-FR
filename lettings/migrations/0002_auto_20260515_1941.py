from django.db import migrations


def migrate_address(apps, schema_editor):
    try:
        OldAddress = apps.get_model("oc_lettings_site", "Address")
        NewAddress = apps.get_model("lettings", "Address")

        for old_address in OldAddress.objects.all():
            NewAddress.objects.create(
                id=old_address.id,
                number=old_address.number,
                street=old_address.street,
                city=old_address.city,
                state=old_address.state,
                zip_code=old_address.zip_code,
                country_iso_code=old_address.country_iso_code,
            )
    except LookupError:
        pass


def reverse_migrate_address(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(migrate_address, reverse_migrate_address),
    ]