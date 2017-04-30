# 狐享会API

URL: http://0.0.0.0:8101/main/ + ...

## *个人中心*

---

注册:signup/(post)
>phone(11) email password(>6) password2

登录:signin/(post)
>phone(11) password

登出:signout/(get)

忘记密码：forget/(post)
>email

修改密码：change_passwd/（login_required / post）
>old_passwd  password0(>=6)  password1

---

## *楼盘展示*

获取楼盘列表：bulidings/1/ (get)






