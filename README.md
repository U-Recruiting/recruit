
#### 后台:
+ 1-user 
    + 用户注册登录
        - 完成,待优化   
+ 2-index 
    + 首页
        - 完成，待优化
+ 3-search 
    + 查询页，根据条件显示岗位信息简介
        - 完成，待优化
+ 4-position 
    + 岗位信息详情页,显示岗位详细信息, 包括岗位所属公司, 在此界面用户投递简历,收藏简历
        - 完成，待优化
    + 企业发布岗位信息
    
+ 5-shoot 
    + 处理投递简历后台流程
        - 完成,待优化
+ 6-mycenter
    + 投递箱
        - 完成,待优化
    + 处理收藏岗位信息后台流程
        - 完成, 待优化
+ 7-org 
    + 企业完善信息,home页
    + 筛选简历
    + 发布职位
+ 8-resume
    + 用户编辑简历


 ### 2018-11-16
 1.调整目录结构
    将原来org里面的内容全部移到了org_auth 
    将原来org_index内容全部移动到了org下面
 2.完成了简历投递，企业查看收到简历情况,并对收到简历进行操作
 
 ### 2018-11-17 01:10:00
 1. 修改register.html 添加jquery
 2。 配置手机发送验证码功能,在user.utils中
 
 123456 :pbkdf2_sha256$120000$StpGvQfO4vjm$yZ39kU/ejql4woM8dhRh1jypOoYoe/zzcgTF2EO2hw4=
 file: enctype="multipart/form-data"
 
 
 {% for position in position_list %}
                        <li class="odd clearfix" style="width: 998px">
                        <div class="hot_pos_left">
                            <div class="mb10">
                                <a href="/position/{{ position.id }}" target="_blank">{{ position.name }}</a>
                                &nbsp;
                                <span class="c9">[{{ position.city }}]</span><span>x天前发布</span>
                            </div>
                            <span><em class="c7" style="color: red;font-size: medium">{{ position.start_salary }}-{{ position.end_salary }}</em></span>
                            <span><em class="c7">{{ position.work_exp }}\{{ position.edu_exp }}</em> </span>
                            <br/>
                            <span><em class="c7">职位诱惑：</em>{{ position.positionAdvantage }}</span>
                            <br/>

                        </div>
                        <div class="hot_pos_right">
                            <div class="apply">
                                <a href="/shoot/{{ position.id }}" target="_blank">投个简历</a>
                            </div>
{#                            <div class="mb10 recompany"><a href="h/c/399.html" target="_blank">节操精选</a></div>#}
                            <span><em class="c7">{{ position.org.type }}\{{ position.org.phase }}\{{ position.org.scale }}</em> </span>
                            <br/>
                            <ul class="comTags reset">
                                <li>移动互联网</li>
                                <li>五险一金</li>
                                <li>扁平管理</li>
                            </ul>
                        </div>

                    </li>
                    {% endfor %}