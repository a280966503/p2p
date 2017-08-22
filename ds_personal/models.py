from django.db import models

class SystemDictionary(models.Model):
    sn=models.CharField(max_length=50)
    title=models.CharField(max_length=50)

class SystemDictionaryItem(models.Model):
    parent=models.ForeignKey(SystemDictionary)
    title=models.CharField(max_length=50)
    sequence=models.IntegerField()

class RealAuth(models.Model):
    realname=models.CharField(max_length=50)
    sex=models.IntegerField()
    birthDate=models.CharField(max_length=50)
    idNumber=models.CharField(max_length=50)
    address=models.CharField(max_length=255)
    state=models.IntegerField()
    image1=models.CharField(max_length=255)
    image2=models.CharField(max_length=255)
    remark=models.CharField(max_length=255,default=None)
    auditTime=models.DateTimeField(default=None)
    applyTime=models.DateTimeField()
    auditor=models.ForeignKey('ds_user.LoginInfo',related_name='auditor_id',default=None)
    applier=models.ForeignKey('ds_user.LoginInfo',related_name='applier_id')


class UserInfo(models.Model):
    version=models.IntegerField()
    bitState=models.BigIntegerField()
    realName=models.CharField(default=None,max_length=30)
    idNumber=models.CharField(default=None,max_length=30)
    phoneNumber=models.CharField(default=None,max_length=30)
    incomeGrade=models.ForeignKey(SystemDictionaryItem,related_name='incomeGrade_id',default=None)
    marriage=models.ForeignKey(SystemDictionaryItem,related_name='marriage_id',default=None)
    kidCount=models.ForeignKey(SystemDictionaryItem,related_name='kidCount_id',default=None)
    educationBackground=models.ForeignKey(SystemDictionaryItem,related_name='educationBackground_id',default=None)
    authScore=models.IntegerField(default=None)
    houseCondition=models.ForeignKey(SystemDictionaryItem,related_name='houseCondition_id',default=None)
    realAuth=models.ForeignKey(RealAuth,default=None)
    email=models.CharField(max_length=255,default=None)



