# Generated by Django 2.1.2 on 2024-01-17 03:08

from django.db import migrations, models
import django.utils.timezone
import estimates.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rouph_estimate_name', models.CharField(max_length=256, verbose_name='案件名')),
                ('rouph_estimate_man_hour', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='工数')),
                ('rouph_estimate_unit', models.CharField(choices=[('man_month', '人月'), ('man_date', '人日'), ('man_hour', '時間')], max_length=20)),
                ('rouph_estimate_delivary_date', models.DateField(default=django.utils.timezone.now, verbose_name='納期')),
                ('is_stoped', models.BooleanField(default=False, verbose_name='中止')),
                ('estimate_files', models.FileField(upload_to=estimates.models.estimate_upload_to, verbose_name='見積書')),
                ('estimate_type', models.CharField(choices=[('rough', '概算'), ('formal', '正式')], max_length=20, verbose_name='概算・見積')),
                ('estimate_man_hour', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='工数')),
                ('estimate_unit', models.CharField(choices=[('man_month', '人月'), ('man_date', '人日'), ('man_hour', '時間')], max_length=20)),
                ('estimate_delivary_date', models.DateField(default=django.utils.timezone.now, verbose_name='納期')),
                ('go_live_date', models.DateField(verbose_name='本稼働日')),
                ('received_date', models.DateField(verbose_name='受注日')),
                ('expected_delivery_date', models.DateField(verbose_name='納品予定日')),
                ('expected_inspection_date', models.DateField(verbose_name='検収予定日')),
                ('quotation', models.FileField(upload_to=estimates.models.placing_upload_to, verbose_name='見積書')),
                ('delivery_date', models.DateField(verbose_name='納品日')),
                ('delevery_receipt', models.FileField(upload_to=estimates.models.placing_upload_to, verbose_name='納品書')),
                ('inspection_date', models.DateField(verbose_name='検収日')),
                ('inspection_receipt', models.FileField(upload_to=estimates.models.placing_upload_to, verbose_name='検収書')),
                ('description', models.TextField(verbose_name='備考')),
            ],
        ),
    ]