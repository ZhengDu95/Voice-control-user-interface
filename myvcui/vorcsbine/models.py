# Create your models here.
from django.db import models


# 用户信息表
class User(models.Model):
    # 用户名
    user_name = models.CharField(max_length=30)
    # 用户密码
    user_password = models.CharField(max_length=30)
    # 用户邮箱
    user_email = models.CharField(max_length=30)

    class Meta:
        db_table = 'user'