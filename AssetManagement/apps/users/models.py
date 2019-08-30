from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.departments.models import Department


class UserProfile(AbstractUser):
    number = models.CharField(max_length=15, verbose_name="学号工号", unique=True, default='')
    department = models.ForeignKey(Department, verbose_name="部门", on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(verbose_name="角色", choices=(
        ('ptr', '普通人'),
        ('sam', '设备负责人'),
        ('dam', '部门负责人')), max_length=3, default='ptr')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
