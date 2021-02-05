from django.db import models

# Create your models here.

def get_upload_dir(instance, filename):
    return 'mailbk/mail/{0}/{1}'.format(instance.todo_id,filename)

class TmpFile(models.Model):
    fileName = models.CharField(
        max_length=256,
        blank=True,
    )

    # attach = models.FileField(
    #     '添付ファイル',
    #     # upload_to='Files/',
    # )

    attach = models.BinaryField(
    )

