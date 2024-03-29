# Generated by Django 2.2.7 on 2019-12-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vendor_Name', models.CharField(max_length=264)),
                ('Vendor_Organisation', models.CharField(max_length=264)),
                ('Vendor_Address', models.CharField(blank=True, max_length=264)),
                ('Vendor_PhoneNo', models.CharField(max_length=264)),
                ('Vendor_Email', models.EmailField(max_length=500)),
                ('Vendor_profile_image', models.ImageField(blank=True, null=True, upload_to='Image/')),
            ],
        ),
    ]
