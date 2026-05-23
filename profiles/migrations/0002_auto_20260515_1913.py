from django.db import migrations


def migrate_profiles(apps, schema_editor):
    try:
        OldProfile = apps.get_model("oc_lettings_site", "Profile")
        NewProfile = apps.get_model("profiles", "Profile")

        for old_profile in OldProfile.objects.all():
            NewProfile.objects.create(
                user=old_profile.user,
                favorite_city=old_profile.favorite_city
            )
    except LookupError:
        pass


def reverse_migrate_profiles(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(migrate_profiles, reverse_migrate_profiles),
    ]