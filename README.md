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

#### 设置用户信息：set_user_info/ （login_required/post）
>name address gender(男／女) sytles (BUILDING_TYPE) regions (LOCATIONS 取值范围见楼盘API)
weichat

*备注：所有选填项目必须属于给定的取值范围，否则后台无法正确显示*

BUILDING_TYPE=(
    ('普通住宅','普通住宅'), ('花园洋房','花园洋房'), ('别墅','别墅'), ('商铺','商铺'), ('写字楼','写字楼'), ('公寓','公寓）'),
)
#### 获取用户信息：user_info/ (login_required / get)
结果样例：
```
{
  "user_info": {
    "weichat": "wx213433545234",
    "phone": "18280080000",
    "regions": "崇州",
    "name": "叶同学",
    "address": "农村",
    "styles": "写字楼",
    "gender": "男",
    "email": "example@qq.com"
  },
  "message": "获取用户信息成功"
}

```


## *Banner and News*

#### 获取Banners：get_banners／（get）
#### 获取News：get_news／（get）






## *楼盘展示*

#### 分页获取楼盘列表：bulidings/1/ (get)
结果样例：
```
{
  "message": "获取楼盘信息成功",
  "list": [
    {
      "phone": "18280082093",
      "location": "chenghua",
      "title": "我是楼盘标题",
      "recommend_id": 3,
      "price": 23243,
      "detail_url": "links",
      "cover": "/assets/main/56b62f80201d462bada9054ec1117fa3.jpg",
      "id": 2,
      "is_like": true
    },
    {
      "phone": "asdf",
      "location": "gaoxingxiqu",
      "title": "pdf",
      "recommend_id": 2,
      "price": 3,
      "detail_url": "pdf",
      "cover": "/assets/main/87381e9876934e12ad65531426186751.png",
      "id": 1,
      "is_like": false
    }
  ]
}
```

#### 分页条件筛选楼盘：buildings_condition/1/（post）(三个参数都不传返回所有数据，筛选的关键字必须属于以下范围)
>location : LOCATIONS=(
    ('锦江区', '锦江区'),('青羊区','青羊区'),('金牛区','金牛区'),('武侯区','武侯区'),('成华区','成华区'),
    ('高新区','高新区'),('高新西区','高新西区'),('温江','温江'),('双流','双流'), ('龙泉驿','龙泉驿'),
    ('新都','新都'),('郫县','郫县'),('都江堰','都江堰'),('青白江','青白江'),('彭州','彭州'),
    ('浦江','浦江'),('大邑','大邑'),('新津','新津'),('崇州','崇州'),('邛崃','邛崃'),('金堂','金堂')

>area_section:AREA_SECCTIONS=(
    ('50㎡以下','50㎡以下'), ('50-70㎡','50-70㎡'), ('70-90㎡','70-90㎡'), ('90-110㎡','90-110㎡'),
    ('110-150㎡','110-150㎡'), ('150-200㎡','150-200㎡'), ('200-300㎡','200-300㎡'),('300㎡以上','300㎡以上'),
)

>price_section:PRICE_SECTIONS=(
    ('3000以下','3000以下'), ('3000-5000','3000-5000'), ('5000-7000','5000-7000'), ('7000-9000','7000-9000'),
    ('9000-11000','9000-11000'), ('11000-15000','11000-15000'), ('15000-20000','15000-20000'),('20000以上','20000以上'),
)

#### 楼盘搜索：search_building/?q=我是楼盘标题



## *活动*

#### 分页获取活动列表：get_activitys/1/（get ）

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



