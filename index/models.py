from django.db import models
from user.models import MyUser
# Create your models here.


class UserInfo(models.Model):
    avatar = models.CharField('头像', max_length=20, default=None)
    name = models.CharField('用户名', max_length=50, default=None)
    birthday = models.DateTimeField('出生日期')
    sex = models.CharField('性别', max_length=10, default=None)
    city = models.CharField('城市', max_length=20, default=None)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class WorkExp(models.Model):
    company = models.CharField('公司', max_length=50, default=None)
    tag = models.CharField('行业标签', max_length=20, default=None)
    department = models.CharField('部门', max_length=50, default=None)
    type = models.CharField('职位类型', max_length=50, default=None)
    position_name = models.CharField('职位名字', max_length=20, default=None)
    start_date = models.DateTimeField('起始时间')
    end_date = models.DateTimeField('终止时间')
    skill = models.CharField('技能', max_length=20, default=None)
    description = models.CharField('工作描述', max_length=500, default=None)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class ProjectExp(models.Model):
    name = models.CharField('项目名称', max_length=50, default=None)
    start_date = models.DateTimeField('起始时间')
    end_date = models.DateTimeField('终止时间')
    url = models.CharField('项目链接', max_length=100, default=None)
    description = models.CharField('项目描述', max_length=500, default=None)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class EducationExp(models.Model):
    school = models.CharField('学校', max_length=50, default=None)
    start_date = models.DateTimeField('起始时间')
    end_date = models.DateTimeField('终止时间')
    education = models.DateTimeField('学历', max_length=50, default=None) ##待改成char
    subject = models.CharField('专业', max_length=50, default=None)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class HuntingIntent(models.Model):
    position = models.CharField('求职意向', max_length=50, default=None)
    position_type = models.CharField('职位类型', max_length=20, default=None)
    city = models.CharField('期望城市', max_length=50, default=None)
    satrt_salary = models.CharField('期望起始薪资', max_length=20, default=None)
    end_salary = models.CharField('期望最高薪资', max_length=20, default=None)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class Resume(models.Model):
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE, default=None)
    work_exp = models.ForeignKey(WorkExp, on_delete=models.CASCADE, default=None)
    project_exp = models.ForeignKey(ProjectExp, on_delete=models.CASCADE, default=None)
    edu_exp = models.ForeignKey(EducationExp, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class OrgInfo(models.Model):

    name = models.CharField('公司名称', max_length=20, default=None, null=True)
    avatar = models.CharField('公司图标', max_length=50,default=None, null=True)
    type = models.CharField('公司类型', max_length=20, default=None, null=True)
    phase = models.CharField('公司所在阶段', max_length=50, default=None, null=True) #A轮
    desc = models.CharField('公司描述', max_length=500, default=None, null=True)
    scale = models.CharField('公司人数',max_length=50, null=True)
    url = models.CharField('公司网站', max_length=20, default=None,null=True)
    phone = models.CharField('联系方式', max_length=20, default=None,null=True)
    city = models.CharField('城市', max_length=20, default=None,null=True)
    email = models.EmailField('公司邮箱',null=True)
    tags = models.CharField('公司标签', max_length=200, default=None,null=True) #绩效奖金 通讯津贴...
    createTime = models.DateTimeField(default=None,null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None,null=True)


class PositionInfo(models.Model):
    type = models.CharField('岗位类型', max_length=20)
    name = models.CharField('职位名称', max_length=20)
    department = models.CharField('所属部门', max_length=20)
    job_catagory = models.CharField('工作性质', max_length=20) #全职，兼职，实习
    start_salary = models.CharField('起始薪资', max_length=20)
    end_salary = models.CharField('最高薪资', max_length=20)
    city = models.CharField('工作城市', max_length=20)

    distinct = models.CharField('区/县', max_length=20, default=None, null=True)

    address = models.CharField('工作地址', max_length=100)
    work_exp = models.CharField('工作经验', max_length=20)
    edu_exp = models.CharField('学历要求', max_length=20)

    tags = models.CharField('职位标签', max_length=200, default=None,null=True)

    desc = models.CharField('职位描述', max_length=400)

    positionAdvantage = models.CharField('职位诱惑', max_length=200, default=None,null=True)
    subwayline = models.CharField('地铁线', max_length=20, default=None,null=True)
    linestaion = models.CharField('地铁线路', max_length=200, default=None,null=True)
    create_datetime = models.DateTimeField('创建时间',default=None,null=True)

    org = models.ForeignKey(OrgInfo, on_delete=models.CASCADE, default='',null=True) #
    resume = models.ManyToManyField(Resume)


class Collection(models.Model):
    position = models.ForeignKey(PositionInfo, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class Dynamic_Position(models.Model):
    dynamic_id = models.AutoField('序号', primary_key=True)
    dynamic_search = models.IntegerField('搜索次数')
    position_info = models.ForeignKey(PositionInfo, on_delete=models.CASCADE, default=None)


class Dynamic_Org(models.Model):
    dynamic_id = models.AutoField('序号', primary_key=True)
    dynamic_search = models.IntegerField('搜索次数')
    org_info = models.ForeignKey(OrgInfo, on_delete=models.CASCADE, default=None)




class PositionResumeStatus(models.Model):
    position = models.ForeignKey(PositionInfo, on_delete=models.CASCADE,default='')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,default='')
    status = models.CharField('状态', max_length=20, default='')


class Province(models.Model):
    province_code = models.CharField('省份代码', max_length=30, default=None,)
    province_name = models.CharField('省份名称', max_length=50, default=None)


class City(models.Model):
    city_code = models.CharField('城市代码', max_length=30, default=None, )
    city_name = models.CharField('城市名称', max_length=50, default=None)
    province_code = models.CharField('省份代码', max_length=30, default=None)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name='所在省份')



class Distinct(models.Model):
    distinct_code = models.CharField('区代码', max_length=30, default=None, )
    distinct_name = models.CharField('区名称', max_length=50, default=None)
    city_code = models.CharField('城市名称', max_length=50, default=None)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='所属城市')


class Job_Label1(models.Model):
    id = models.AutoField('一级标签', primary_key=True)
    name = models.CharField('一级标签名称', max_length=20, default=None)


class Job_Label2(models.Model):
    id = models.AutoField('二级标签', primary_key=True)
    name = models.CharField('二级标签名称', max_length=20, default=None)
    parent = models.ForeignKey(Job_Label1, on_delete=models.CASCADE,verbose_name='父标签ID', default=None)


class Job_Label3(models.Model):
    id = models.AutoField('三级标签', primary_key=True)
    name = models.CharField('三级标签名称', max_length=20, default=None)
    parent = models.ForeignKey(Job_Label2, on_delete=models.CASCADE,verbose_name='父标签ID', default=None)



