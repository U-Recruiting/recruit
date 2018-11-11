from django.db import models
from user.models import MyUser
# Create your models here.


class Job_Label1(models.Model):
    id = models.IntegerField('一级标签', primary_key=True)
    name = models.CharField('一级标签名称', max_length=20)


class Job_Label2(models.Model):
    id = models.IntegerField('二级标签', primary_key=True)
    name = models.CharField('二级标签名称', max_length=20)
    parent = models.ForeignKey(Job_Label1, on_delete=models.CASCADE,verbose_name='父标签ID')


class Job_Label3(models.Model):
    id = models.IntegerField('三级标签', primary_key=True)
    name = models.CharField('三级标签名称', max_length=20)
    parent = models.ForeignKey(Job_Label2, on_delete=models.CASCADE,verbose_name='父标签ID')


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

    name = models.CharField('公司名称', max_length=20)
    avatar = models.CharField('公司图标', max_length=50)
    type = models.CharField('公司类型', max_length=20)
    phase = models.CharField('公司所在阶段', max_length=50) #A轮
    desc = models.CharField('公司描述', max_length=500)
    scale = models.IntegerField('公司人数')
    url = models.CharField('公司网站', max_length=20)
    phone = models.CharField('联系方式', max_length=20)
    city = models.CharField('城市', max_length=20)
    email = models.EmailField('公司邮箱')
    tags = models.CharField('公司标签', max_length=200) #绩效奖金 通讯津贴...
    createTime = models.DateTimeField(default=None)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)


class PositionInfo(models.Model):
    type = models.CharField('岗位类型', max_length=20)
    name = models.CharField('职位名称', max_length=20)
    department = models.CharField('所属部门', max_length=20)
    job_catagory = models.CharField('工作性质', max_length=20) #全职，兼职，实习
    start_salary = models.CharField('起始薪资', max_length=20)
    end_salary = models.CharField('最高薪资', max_length=20)
    city = models.CharField('工作城市', max_length=20)
    distinct = models.CharField('区/县', max_length=20, default=None)
    address = models.CharField('工作地址', max_length=100)
    work_exp = models.CharField('工作经验', max_length=20)
    edu_exp = models.CharField('学历要求', max_length=20)
    tags = models.CharField('职位标签', max_length=200, default=None)
    desc = models.CharField('职位描述', max_length=400)
    positionAdvantage = models.CharField('职位诱惑', max_length=200,default=None)
    subwayline = models.CharField('地铁线', max_length=20,default=None)
    linestaion = models.CharField('地铁线路', max_length=200, default=None)
    org = models.ForeignKey(OrgInfo, on_delete=models.CASCADE, default='') #
    resume = models.ManyToManyField(Resume)


class PositionResumeStatus(models.Model):
    position = models.ForeignKey(PositionInfo, on_delete=models.CASCADE,default='')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,default='')
    status = models.CharField('状态', max_length=20, default='')


