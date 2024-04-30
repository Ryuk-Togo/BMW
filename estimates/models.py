import os
from django.db import models
from django.utils import timezone

# Create your models here.

# 見積書ファイルの配置位置
def estimate_upload_to(instance, filename):
    return os.path.join('uploads', instance.rouph_estimate_name + '/見積書', filename)

# 発注書ファイルの配置位置
def placing_upload_to(instance, filename):
    return os.path.join('uploads', instance.rouph_estimate_name + '/発注書', filename)

class Estimate(models.Model):

    UNIT_CHOICES=(
        ('man_month','人月'),
        ('man_date','人日'),
        ('man_hour','時間'),
    )

    ESTIMATE_TYPE=(
        ('rough','概算'),
        ('formal','正式'),
    )

    rouph_estimate_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="案件名"
    )

    # 見積書
    rouph_estimate_files = models.FileField(
        upload_to=estimate_upload_to,
        blank=True,
        null=True,
        verbose_name="概算見積書"
    )

    # 見積時(予測)
    rouph_estimate_man_hour = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="工数"
    )

    rouph_estimate_unit = models.CharField(
        verbose_name="",
        max_length=20, 
        blank=True,
        null=True,
        choices=UNIT_CHOICES
    )

    rouph_estimate_delivary_date = models.DateField(
        default=timezone.now,
        blank=True,
        null=True,
        verbose_name="納期"
    )

    quotation_deadline = models.DateField(
        blank=True,
        null=True,
        verbose_name="見積提示時期"
    )

    is_stoped = models.BooleanField(
        default=False,
        null=True,
        verbose_name="中止"        
    )

    # 見積書
    estimate_files = models.FileField(
        upload_to=estimate_upload_to,
        blank=True,
        null=True,
        verbose_name="見積書"
    )

    estimate_man_hour = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="工数"        
    )

    estimate_unit = models.CharField(
        verbose_name="",
        max_length=20, 
        blank=True,
        null=True,
        choices=UNIT_CHOICES
    )

    estimate_delivary_date = models.DateField(
        default=timezone.now,
        blank=True,
        null=True,
        verbose_name="納期"
    )

    go_live_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="本稼働日"
    )

    received_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="受注日"
    )

    expected_inspection_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="検収予定日"
    )

    quotation = models.FileField(
        upload_to=placing_upload_to,
        blank=True,
        null=True,
        verbose_name="見積書"
    )

    delivery_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="納品日"
    )

    delevery_receipt = models.FileField(
        upload_to=placing_upload_to,
        blank=True,
        null=True,
        verbose_name="納品書"
    )

    inspection_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="検収日"
    )

    inspection_receipt = models.FileField(
        upload_to=placing_upload_to,
        blank=True,
        null=True,
        verbose_name="検収書"
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="備考"
    )
