from django.db import models

# Create your models here.
class MsysVal(models.Model):
    sys_name = models.CharField(
        max_length=256,
        blank=False,
        default=' ',
    )

    item_name1 = models.CharField(
        max_length=256,
        blank=True,
        default=' ',
    )
    
    item_name2 = models.CharField(
        max_length=256,
        blank=True,
        default=' ',
    )
    
    item_name3 = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    
    item_name4 = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    
    item_name5 = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    
    char_value1 = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    
    char_value2 = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    
    char_value3 = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    
    char_value4 = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    
    char_value5 = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    
    char_value6 = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    
    char_value7 = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    
    char_value8 = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    
    char_value9 = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    
    char_value10 = models.CharField(
        max_length=256,
        blank=True,
        default='',
    )
    
    int_value1 = models.IntegerField(
        blank=True,
        default=0,
    )
    
    int_value2 = models.IntegerField(
        blank=True,
        default=0,
    )
    
    int_value3 = models.IntegerField(
        blank=True,
        default=0,
    )
    
    int_value4 = models.IntegerField(
        blank=True,
        default=0,
    )
    
    int_value5 = models.IntegerField(
        blank=True,
        default=0,
    )
    
    int_value6 = models.IntegerField(
        blank=True,
        default=0,
    )
    
    int_value7 = models.IntegerField(
        blank=True,
        default=0,
    )
    
    int_value8 = models.IntegerField(
        blank=True,
        default=0,
    )
    
    int_value9 = models.IntegerField(
        blank=True,
        default=0,
    )
    
    int_value10 = models.IntegerField(
        blank=True,
        default=0,
    )
