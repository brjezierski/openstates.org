# Generated by Django 2.2.10 on 2020-03-25 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("legislative", "0012_billdocument_extras"),
        ("bundles", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bundlebill", old_name="bill_id", new_name="bill"
        ),
        migrations.RenameField(
            model_name="bundlebill", old_name="bundle_id", new_name="bundle"
        ),
        migrations.AlterUniqueTogether(
            name="bundlebill", unique_together={("bundle", "bill")}
        ),
    ]
