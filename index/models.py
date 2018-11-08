from django.db import models
from user.models import MyUser
# Create your models here.


class UserInfo(models.Model):
    avatar = models.CharField('头像', max_length=20)
    name = models.CharField('用户名', max_length=50)
    birthday = models.DateTimeField('出生日期')
    sex = models.CharField('性别', max_length=10)
    city = models.CharField('城市', max_length=20)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)


class WorkExp(models.Model):
    company = models.CharField('公司', max_length=50)
    tag = models.CharField('行业标签', max_length=20)
    department = models.CharField('部门', max_length=50)
    type = models.CharField('职位类型', max_length=50)
    position_name = models.CharField('职位名字', max_length=20)
    start_date = models.DateTimeField('起始时间')
    end_date = models.DateTimeField('终止时间')
    skill = models.CharField('技能', max_length=20)
    description = models.CharField('工作描述', max_length=500)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)


class ProjectExp(models.Model):
    name = models.CharField('项目名称', max_length=50)
    start_date = models.DateTimeField('起始时间')
    end_date = models.DateTimeField('终止时间')
    url = models.CharField('项目链接', max_length=100)
    description = models.CharField('项目描述', max_length=500)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default='')


class EducationExp(models.Model):
    school = models.CharField('学校', max_length=50)
    start_date = models.DateTimeField('起始时间')
    end_date = models.DateTimeField('终止时间')
    education = models.DateTimeField('学历', max_length=50)
    subject = models.CharField('专业', max_length=50)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default='')


class HuntingIntent(models.Model):
    position = models.CharField('求职意向', max_length=50)
    position_type = models.CharField('职位类型', max_length=20)
    city = models.CharField('期望城市', max_length=50)
    satrt_salary = models.CharField('期望起始薪资', max_length=20)
    end_salary = models.CharField('期望最高薪资', max_length=20)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default='')


class Resume(models.Model):
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    work_exp = models.ForeignKey(WorkExp, on_delete=models.CASCADE)
    project_exp = models.ForeignKey(ProjectExp, on_delete=models.CASCADE)
    edu_exp = models.ForeignKey(EducationExp, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default='')


class OrgInfo(models.Model):
    pass


class PositionInfo(models.Model):
    pass

