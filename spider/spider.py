#!usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:shenchen
@file: spider
@time: 2018/11/10
"""

import requests
import random
from lxml import etree
from django.conf import settings
import re
import urllib.request
import urllib.parse
import os
import time
import json
from user.models import *
from index.models import *


USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"
]

header = {'User-Agent': '{0}'.format(random.sample(USER_AGENT_LIST, 1)[0]),
          'Cookie': 'user_trace_token=20181117171047-3f797619-d794-4f03-bd5c-60e1fbf17ae6; LGUID=20181117171048-ac220d29-ea48-11e8-892c-5254005c3644; _ga=GA1.2.756823683.1542445848; _gid=GA1.2.497375058.1542445848; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216720efd5b9123-028f2322ef9974-35667407-1024000-16720efd5bc367%22%2C%22%24device_id%22%3A%2216720efd5b9123-028f2322ef9974-35667407-1024000-16720efd5bc367%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22http%3A%2F%2Flocalhost%3A8000%2Forg_auth%2Fregister01%2F%22%2C%22%24latest_referrer_host%22%3A%22localhost%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; JSESSIONID=ABAAABAAAGGABCB015D3CCCFE065F5482BB7BE2CA273B4C; _gat=1; LGSID=20181117215417-46776a08-ea70-11e8-a493-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DTW8LpTjJDJhubKZvNE4NykmjAqITI3OT2zN1yH2YEzu%26wd%3D%26eqid%3Ded18a41500004b8d000000025bf01d85; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542447390,1542447463,1542447691,1542462857; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; SEARCH_ID=0585e906820943b59c73816727ea1f9c; LGRID=20181117220050-30b04598-ea71-11e8-a496-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542463250',
          'Host': "www.lagou.com",
          'Origin': "https://www.lagou.com",
          'Referer': "https://www.lagou.com/jobs/list_?px=new&city=%E4%B8%8A%E6%B5%B7"
          }

data = {
    'pn': 1,
}


class LaGou:
    def __init__(self, url: str):
        self.page = 1
        self.url = url
        self.all_data = []
        self.cities = ['北京','上海','深圳', '广州', '杭州', '成都', '南京', '武汉', '西安','厦门']
        # self.cities = ['北京']

    def isNone(self, value):
        if not value:
            return ''
        return value

    def get_data_from_url(self):
        for city in self.cities:
            self.url = self.url.format(city)
            for i in range(1, 201):
                data['pn'] = i
                response = requests.post(self.url, headers=header, data=data)
                content = response.content.decode('utf-8')
                if content:
                    json_data = json.loads(content)
                    print(json_data)
                    print('*'*20+str(self.page))
                    self.page+=1
                    self.all_data.append(json_data)
                else:
                    continue

    def save_data_to_database(self):
        self.page = 1
        for page in self.all_data:
            hrInfoMap = page['content']['hrInfoMap']  # {}
            result = page['content']['positionResult']['result']  # []
            for c_o_p in result:
                conpany_user = hrInfoMap[str(c_o_p['positionId'])]
                user = MyUser(id=conpany_user['userId'], is_superuser=0, username=conpany_user['userId'],password='',
                            first_name=self.isNone(conpany_user.get('realName','')),last_name='', email=self.isNone(conpany_user.get('receiveEmail','')), is_staff=0, is_active=1,
                              date_joined='2018-11-11',
                              mobile=self.isNone(conpany_user.get('phone','')),complete='yes', role_id=2
                              )
                user.save()

                path = os.path.join(settings.BASE_DIR, 'spider/static/org_logo/'+str(c_o_p['companyId'])+'.jpg')
                if c_o_p.get('companyLogo',''):
                    jpg_path = 'https://www.lagou.com/' + c_o_p['companyLogo']
                    try:
                        urllib.request.urlretrieve(jpg_path, path)
                    except Exception as e:
                        print(e)
                conpany = OrgInfo(id=c_o_p['companyId'], authed='yes', name=c_o_p['companyFullName'],avatar=c_o_p.get('companyLogo',''),
                                  type=c_o_p['firstType'], phase=self.isNone(c_o_p.get('financeStage','')),
                                  desc='', scale=self.isNone(c_o_p.get('companySize','')), url='', phone='',
                                  city=self.isNone(c_o_p.get('city', '')), email='', tags='', user=user
                                  )
                conpany.save()
                salary = self.isNone(c_o_p.get('salary',''))
                if not salary:
                    start_salary = ''
                    end_salary = ''
                else:
                    split_salary = salary.split('-')
                    start_salary = split_salary[0]
                    end_salary = split_salary[1]
                position = PositionInfo(id=c_o_p['positionId'], type=self.isNone(c_o_p.get('secondType', '')),
                                    name=self.isNone(c_o_p.get('positionName', '')), department='',
                                    job_catagory=self.isNone(c_o_p.get('jobNature','')), start_salary=start_salary,
                                    end_salary=end_salary, city=self.isNone(c_o_p.get('city','')), distinct=self.isNone(c_o_p.get('district','')),
                                    work_exp=self.isNone(c_o_p.get('workYear','')),
                                    edu_exp=self.isNone(c_o_p.get('education','')), address='', positionAdvantage=self.isNone(c_o_p.get('positionAdvantage','')),
                                    subwayline=self.isNone(c_o_p.get('subwayline','')),linestaion=self.isNone(c_o_p.get('linestaion','')),create_datetime=c_o_p.get('createTime',''),
                                    org=conpany
                                    )
                position.save()
                print(c_o_p)
                print('*'*50+str(self.page))
                self.page+=1


