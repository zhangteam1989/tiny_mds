# tiny_mds
- 首选创建一个新用户，用来登录Django管理网站，进入manage.py目录下，使用如下命令来进行创建： 

`>>python manage.py createsuperuser`
- 接下来输入用户名称： 

`>>Username(leave bkank to use 'administrator'): root`
- 然后是输入邮箱（QQemail等都可以）： 

`>>Email address：（输入你的邮箱账号）`

- 输入密码（输入密码时不会显示出来，并且长度必须超过八位才行）：
 
`>>Password：******** `

`>>Password(again)：********`

- 当两次密码输入相同且超过八位的时候，就会提示创建超级用户成功： 
`>>Superuser created successfully.`

- 再次运行你的服务，输入账号和密码就可以成功登陆了： 

`>>python manage.py runserver`

# basis_data
基础数据app
# common_module
通用类和工具定义
# inventory
库存app
# repair_order
维修订单app
# user_center
用户中心app
