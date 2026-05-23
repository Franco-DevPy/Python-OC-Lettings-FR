from django.db import migrations


def migrate_lettings(apps, schema_editor):
    try:
        OldLetting = apps.get_model("oc_lettings_site", "Letting")
        NewLetting = apps.get_model("lettings", "Letting")
        NewAddress = apps.get_model("lettings", "Address")

        for old_letting in OldLetting.objects.all():
            new_address = NewAddress.objects.get(id=old_letting.address.id)
            NewLetting.objects.create(
                id=old_letting.id,
                title=old_letting.title,
                address=new_address
            )
    except LookupError:
        pass


def reverse_migrate_lettings(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0002_auto_20260515_1941"),
    ]

    operations = [
        migrations.RunPython(migrate_lettings, reverse_migrate_lettings),
    ]