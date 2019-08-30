from django.db import models
from django.contrib.auth import get_user_model

from apps.departments.models import BaseModel


UserProfile = get_user_model()

status_choices = (
        ('sy', '使用'),
        ('wx', '维修'),
        ('xz', '闲置'))


class Change(BaseModel):
    summit_user = models.ForeignKey(UserProfile, verbose_name="提交审核人", on_delete=models.CASCADE,
                                    related_name="user_asset")  # 加related_name是为了在UserProfile反向查找的时候和manager_id区分开来
    manager = models.ForeignKey(UserProfile, verbose_name="通过审核人", on_delete=models.CASCADE)
    room_id = models.IntegerField(verbose_name="Room_fk", default='')
    asset_number = models.CharField(verbose_name="资产编号_fk", max_length=20, default='')
    comment = models.CharField(verbose_name="提交备注", max_length=254, default='')
    last_change_id = models.IntegerField(verbose_name="上一次的Change_fk", default='')
    date = models.DateTimeField(verbose_name="修改日期")  #
    status = models.CharField(verbose_name="资产状态", choices=status_choices, max_length=2, default='')
    is_approved = models.BooleanField(verbose_name="是否通过审核", default=False)

    class Meta:
        verbose_name = "变更记录"
        verbose_name_plural = verbose_name


class AssetManager(BaseModel):
    manager = models.ForeignKey(UserProfile, verbose_name="设备负责人", on_delete=models.CASCADE)
    change_id = models.IntegerField(verbose_name="Change_fk", default='')
    asset_number = models.CharField(verbose_name="资产编号", max_length=20, default='')
    status = models.CharField(verbose_name="资产状态", choices=status_choices, max_length=2, default='')
    contract_number = models.CharField(verbose_name="合同编号", max_length=254, default='')
    is_abandoned = models.BooleanField(verbose_name="是否报废", default=False)

    class Meta:
        verbose_name = "资产信息"
        verbose_name_plural = verbose_name

