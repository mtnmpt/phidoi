from django.db import models
from django.db import connection
# from django.contrib.auth.models import  User
# class Customer (models.Model):
#     user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False)
#     name = models.CharField(max_length=200,null=True)
#     email = models.CharField(max_length=200,null=True)
#     def __str__(self):
#         return self.name
# class tes1 (models.Model):
#     ID = models.IntegerField(default=0)
#     AccountID = models.IntegerField(default=0)
#     AccountName = models.CharField(max_length= 50)
#     CreateDate = models.DateField()
#     def __str__(self):
#         return self.name

# class test (models.Model):
#     ID = models.BigAutoField(primary_key=True)
#     AccountID = models.IntegerField(default=0)
#     AccountName = models.CharField(max_length= 50)
#     Status = models.IntegerField(default=0,choices=[(0, 'Chưa nhận quà'), (1, 'Đã nhận quà'),(2,'Đang chờ xử lí')])
#     CreateDate = models.DateField()
#     class Meta:
#         db_table = 'test'  # Đặt tên bảng tại đây
#     def __str__(self):
#         return f'{self.AccountID},{self.AccountName},{self.Status},{self.CreateDate}'

class  SPResult(models.Model):
    ID = models.IntegerField(primary_key=True)
    AccountID = models.IntegerField()
    AccountName = models.CharField(max_length=20)
    Status = models.IntegerField()
    CreateDate = models.DateField()
    @staticmethod
    def SP_Test_GetList(account_id, account_name):
        SP_Name = '[dbo].[SP_Test_GetList]'
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC {SP_Name} @param1=%s, @param2=%s", [account_id, account_name])
            results = cursor.fetchall()
        return results

