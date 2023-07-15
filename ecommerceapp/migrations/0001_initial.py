# Generated by Django 4.2.3 on 2023-07-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("desc", models.TextField(max_length=500)),
                ("phonenumber", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_id", models.CharField(max_length=100, unique=True)),
                ("items_json", models.CharField(max_length=5000)),
                ("amount", models.FloatField(default=0)),
                ("name", models.CharField(max_length=90)),
                ("email", models.CharField(max_length=90)),
                ("address1", models.CharField(max_length=200)),
                ("address2", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("zip_code", models.CharField(max_length=100)),
                ("oid", models.CharField(blank=True, max_length=150)),
                ("razorpay_payment_id", models.CharField(blank=True, max_length=100)),
                ("amountpaid", models.CharField(blank=True, max_length=500, null=True)),
                ("paid", models.BooleanField(default=False)),
                ("paymentstatus", models.CharField(blank=True, max_length=20)),
                ("phone", models.CharField(default="", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="OrderUpdate",
            fields=[
                ("update_id", models.AutoField(primary_key=True, serialize=False)),
                ("order_id", models.CharField(max_length=100, unique=True)),
                ("update_desc", models.CharField(max_length=5000)),
                ("delivered", models.BooleanField(default=False)),
                ("timestamp", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=100)),
                ("category", models.CharField(default="", max_length=100)),
                ("subcategory", models.CharField(default="", max_length=50)),
                ("price", models.IntegerField(default=0)),
                ("desc", models.CharField(max_length=300)),
                ("image", models.ImageField(upload_to="images/images")),
            ],
        ),
    ]
