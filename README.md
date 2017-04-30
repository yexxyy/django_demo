# 狐享会API

URL: http://0.0.0.0:8101/main/ + ...

## *个人中心*

#### 注册:signup/(post)
>phone(11) email password(>6) password2

#### 登录:signin/(post)
>phone(11) password

#### 登出:signout/(get)

#### 忘记密码：forget/(post)
>email

#### 修改密码：change_passwd/（login_required / post）
>old_passwd  password0(>=6)  password1

#### 收藏楼盘：set_liked/2/（login_required/post）
>再请求则取消收藏

#### 获取用户收藏：get_user_likes/ （login_required／get）




## *Banner and News*

#### 获取Banners：get_banners／（get）
#### 获取News：get_news／（get）






## *楼盘展示*

#### 分页获取楼盘列表：bulidings/1/ (get)
结果样例：
```
{
  "message": "获取楼盘列表成功",
  "list": [
    {
      "phone": "18280082093",
      "location": "chenghua",
      "title": "我是楼盘标题",
      "recommend_id": 3,
      "price": 23243,
      "detail_url": "links",
      "cover": "/assets/main/56b62f80201d462bada9054ec1117fa3.jpg",
      "id": 2
    }
  ]
}
```

#### 条件筛选楼盘：buildings_condition／（post）(三个参数都不传返回所有数据)
>location : LOCATIONS=(
    ('jinjiang', '锦江'),('qingyangqu','青羊'),('jinniu','金牛'),('wuhou','武侯'),('chenghua','成华'),
    ('gaoxing','高新区'),('gaoxingxiqu','高新西区'),('wenjaing','温江'),('shuangliu','双流'), ('longquanyi','龙泉驿'),
    ('xindu','新都'),('pixian','郫县'),('dujiangyan','都江堰'),('qingbaijiang','青白江'),('pengzhou','彭州'),
    ('pujiang','浦江'),('dayi','大邑'),('xinjin','新津'),('congzhou','崇州'),('qionglai','邛崃'),('jintang','金堂')
)

>area_section:AREA_SECCTIONS=(
    ('one','50㎡以下'), ('two','50-70㎡'), ('three','70-90㎡'), ('four','90-110㎡'), ('five','110-150㎡'), ('six','150-200㎡'), ('seven','200-300㎡'),('eight','300㎡以上'),
)

>price_section:PRICE_SECTIONS=(
    ('one','3000以下'), ('two','3000-5000'), ('three','5000-7000'), ('four','7000-9000'), ('five','9000-11000'), ('size','11000-15000'), ('seven','15000-20000'),('eight','20000以上'),
)





## *活动*

#### 获取活动列表：get_activitys（get）

#### 获取活动收集的用户字段：get_collect_items/1/ （login_required/get）

结果样例：

```

{
  "activity_id": 1,
  "list": [
    {
      "id": 8,
      "name": "手机"
    },
    {
      "id": 9,
      "name": "联系地址"
    }
  ],
  "message": "获取收集字段列表成功"
}
```

#### 活动报名：post_participator_info/（login_required/post）

>name phone age address (全部选填)



