from datetime import datetime

from django.db import models


# 所有类都有的
class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")  # 用于日志

    class Meta:
        abstract = True  # 防止生成表


class Department(BaseModel):
    name = models.CharField(verbose_name="部门名", max_length=50, default='')

    class Meta:
        verbose_name = "部门信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 为了方便之后添加建筑楼
class Building(BaseModel):
    name = models.CharField(verbose_name="建筑楼", max_length=20)  # name + campus must be unique
    campus = models.CharField(verbose_name="所在校区", choices=(
        ("jm", "金明"),
        ("ml", "明伦")), max_length=2, default='')
    desc = models.CharField(verbose_name="描述", max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "建筑楼"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Room(BaseModel):
    name = models.CharField(verbose_name="房间号", max_length=20)
    building = models.ForeignKey(Building, verbose_name="所在建筑楼", on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name="所属部门", on_delete=models.SET_NULL, null=True, blank=True)  # 如果部门被删除, 置为null
    desc = models.CharField(verbose_name="描述", max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "房间号"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
