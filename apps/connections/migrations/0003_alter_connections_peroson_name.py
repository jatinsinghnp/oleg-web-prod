# Generated by Django 4.1.4 on 2022-12-24 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "connections",
            "0002_alter_connections_add_note_alter_connections_email_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="connections",
            name="peroson_name",
            field=models.CharField(max_length=500),
        ),
    ]