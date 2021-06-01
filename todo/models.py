from django.db import models
from django.utils import timezone

# Create your models here.
# WHERE_DONT_ACTION = (
#     ('1','いつかやる'),
#     ('2','参考資料'),
#     ('3','ごみ箱')
# )

# CATEGORY = {
#     '06':'いつかやる',
#     '07':'参考資料',
#     '08':'ゴミ箱',
#     '02':'プロジェクト',
#     '01':'すぐやる',
#     '05':'他人に任せる',
#     '04':'特定の日にやる',
#     '03':'自分でやる',
# }


COMPLETE = {
    '0': '未完了',
    '1': '報告中',
    '9': '完了',
}

class TTodo(models.Model):
    work_date = models.DateField(
        verbose_name = '作業日時',
        # help_text='作業日を入力してください。',
        blank=True,
        null=True,
    )

    work_time = models.CharField(
        verbose_name='作業時刻',
        max_length=4,
        # help_text='作業時刻を入力してください。',
        blank=True,
        null=True,
    )

    row = models.IntegerField(
        blank=True,
        null=True,
        default=1,
    )

    todo = models.CharField(
        verbose_name='TODO内容',
        max_length=256,
        # help_text='TODOを入力してください。',
        blank=True,
        null=True,
    )

    do_key = models.IntegerField(
        blank=True,
        null=True,
        # help_text='DOは必ず登録してください。'
    )

    complete = models.CharField(
        verbose_name='完了',
        max_length=1,
        blank=True,
        null=True,
    )

    user_id = models.CharField(
        verbose_name='ユーザID',
        max_length=30,
        blank=True,
        null=True,
    )

    create_date = models.DateTimeField(
        verbose_name='登録日時',
        blank=True,
        default=timezone.now,
    )
    create_pg_id = models.CharField(
        max_length=30,
        blank=True,
    )
    create_user_id = models.CharField(
        max_length=30,
        blank=True,
    )
    update_date = models.DateTimeField(
        verbose_name='更新日時',
        blank=True,
        default=timezone.now,
    )
    update_pg_id = models.CharField(
        max_length=30,
        blank=True,
    )
    update_user_id = models.CharField(
        max_length=30,
        blank=True,
    )


class TDo(models.Model):
    delivery_date = models.DateField(
        verbose_name = '納期',
    )

    do = models.CharField(
        verbose_name='DO内容',
        max_length=256,
        null=False,
    )

    complete = models.CharField(
        verbose_name='完了',
        max_length=1,
        blank=True,
        null=True,
    )

    user_id = models.CharField(
        verbose_name='ユーザID',
        max_length=30,
        blank=True,
        null=True,
    )

    create_date = models.DateTimeField(
        verbose_name='登録日時',
        blank=True,
        default=timezone.now,
    )
    create_pg_id = models.CharField(
        max_length=30,
        blank=True,
    )
    create_user_id = models.CharField(
        max_length=30,
        blank=True,
    )
    update_date = models.DateTimeField(
        verbose_name='更新日時',
        blank=True,
        default=timezone.now,
    )
    update_pg_id = models.CharField(
        max_length=30,
        blank=True,
    )
    update_user_id = models.CharField(
        max_length=30,
        blank=True,
    )


