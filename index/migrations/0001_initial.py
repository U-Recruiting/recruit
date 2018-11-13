# Generated by Django 2.1.2 on 2018-11-13 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_code', models.CharField(default=None, max_length=30, verbose_name='城市代码')),
                ('city_name', models.CharField(default=None, max_length=50, verbose_name='城市名称')),
                ('province_code', models.CharField(default=None, max_length=30, verbose_name='省份代码')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Distinct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distinct_code', models.CharField(default=None, max_length=30, verbose_name='区代码')),
                ('distinct_name', models.CharField(default=None, max_length=50, verbose_name='区名称')),
                ('city_code', models.CharField(default=None, max_length=50, verbose_name='城市名称')),
            ],
        ),
        migrations.CreateModel(
            name='Dynamic_Org',
            fields=[
                ('dynamic_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('dynamic_search', models.IntegerField(verbose_name='搜索次数')),
            ],
        ),
        migrations.CreateModel(
            name='Dynamic_Position',
            fields=[
                ('dynamic_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('dynamic_search', models.IntegerField(verbose_name='搜索次数')),
            ],
        ),
        migrations.CreateModel(
            name='EducationExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(default=None, max_length=50, verbose_name='学校')),
                ('start_date', models.DateTimeField(verbose_name='起始时间')),
                ('end_date', models.DateTimeField(verbose_name='终止时间')),
                ('education', models.DateTimeField(default=None, max_length=50, verbose_name='学历')),
                ('subject', models.CharField(default=None, max_length=50, verbose_name='专业')),
            ],
        ),
        migrations.CreateModel(
            name='HuntingIntent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(default=None, max_length=50, verbose_name='求职意向')),
                ('position_type', models.CharField(default=None, max_length=20, verbose_name='职位类型')),
                ('city', models.CharField(default=None, max_length=50, verbose_name='期望城市')),
                ('satrt_salary', models.CharField(default=None, max_length=20, verbose_name='期望起始薪资')),
                ('end_salary', models.CharField(default=None, max_length=20, verbose_name='期望最高薪资')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Label1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='一级标签')),
                ('name', models.CharField(default=None, max_length=20, verbose_name='一级标签名称')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Label2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='二级标签')),
                ('name', models.CharField(default=None, max_length=20, verbose_name='二级标签名称')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Label3',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='三级标签')),
                ('name', models.CharField(default=None, max_length=20, verbose_name='三级标签名称')),
            ],
        ),
        migrations.CreateModel(
            name='OrgInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=20, null=True, verbose_name='公司名称')),
                ('avatar', models.CharField(default=None, max_length=50, null=True, verbose_name='公司图标')),
                ('type', models.CharField(default=None, max_length=20, null=True, verbose_name='公司类型')),
                ('phase', models.CharField(default=None, max_length=50, null=True, verbose_name='公司所在阶段')),
                ('desc', models.CharField(default=None, max_length=500, null=True, verbose_name='公司描述')),
                ('scale', models.CharField(max_length=50, null=True, verbose_name='公司人数')),
                ('url', models.CharField(default=None, max_length=20, null=True, verbose_name='公司网站')),
                ('phone', models.CharField(default=None, max_length=20, null=True, verbose_name='联系方式')),
                ('city', models.CharField(default=None, max_length=20, null=True, verbose_name='城市')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='公司邮箱')),
                ('tags', models.CharField(default=None, max_length=200, null=True, verbose_name='公司标签')),
                ('createTime', models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PositionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='岗位类型')),
                ('name', models.CharField(max_length=20, verbose_name='职位名称')),
                ('department', models.CharField(max_length=20, verbose_name='所属部门')),
                ('job_catagory', models.CharField(max_length=20, verbose_name='工作性质')),
                ('start_salary', models.CharField(max_length=20, verbose_name='起始薪资')),
                ('end_salary', models.CharField(max_length=20, verbose_name='最高薪资')),
                ('city', models.CharField(max_length=20, verbose_name='工作城市')),
                ('distinct', models.CharField(default=None, max_length=20, null=True, verbose_name='区/县')),
                ('address', models.CharField(max_length=100, verbose_name='工作地址')),
                ('work_exp', models.CharField(max_length=20, verbose_name='工作经验')),
                ('edu_exp', models.CharField(max_length=20, verbose_name='学历要求')),
                ('tags', models.CharField(default=None, max_length=200, null=True, verbose_name='职位标签')),
                ('desc', models.CharField(max_length=400, verbose_name='职位描述')),
                ('positionAdvantage', models.CharField(default=None, max_length=200, null=True, verbose_name='职位诱惑')),
                ('subwayline', models.CharField(default=None, max_length=20, null=True, verbose_name='地铁线')),
                ('linestaion', models.CharField(default=None, max_length=200, null=True, verbose_name='地铁线路')),
                ('create_datetime', models.DateTimeField(default=None, null=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='PositionResumeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=20, verbose_name='状态')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50, verbose_name='项目名称')),
                ('start_date', models.DateTimeField(verbose_name='起始时间')),
                ('end_date', models.DateTimeField(verbose_name='终止时间')),
                ('url', models.CharField(default=None, max_length=100, verbose_name='项目链接')),
                ('description', models.CharField(default=None, max_length=500, verbose_name='项目描述')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_code', models.CharField(default=None, max_length=30, verbose_name='省份代码')),
                ('province_name', models.CharField(default=None, max_length=50, verbose_name='省份名称')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.CharField(default=None, max_length=20, verbose_name='头像')),
                ('name', models.CharField(default=None, max_length=50, verbose_name='用户名')),
                ('birthday', models.DateTimeField(verbose_name='出生日期')),
                ('sex', models.CharField(default=None, max_length=10, verbose_name='性别')),
                ('city', models.CharField(default=None, max_length=20, verbose_name='城市')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default=None, max_length=50, verbose_name='公司')),
                ('tag', models.CharField(default=None, max_length=20, verbose_name='行业标签')),
                ('department', models.CharField(default=None, max_length=50, verbose_name='部门')),
                ('type', models.CharField(default=None, max_length=50, verbose_name='职位类型')),
                ('position_name', models.CharField(default=None, max_length=20, verbose_name='职位名字')),
                ('start_date', models.DateTimeField(verbose_name='起始时间')),
                ('end_date', models.DateTimeField(verbose_name='终止时间')),
                ('skill', models.CharField(default=None, max_length=20, verbose_name='技能')),
                ('description', models.CharField(default=None, max_length=500, verbose_name='工作描述')),
            ],
        ),
    ]
