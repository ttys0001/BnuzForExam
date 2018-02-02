# bnuzforexam pyhton脚本成绩更新提示
期末的时候等成绩是不是很痛苦？这个python脚本来解放你。

## 第三方库：requests，BeautifulSoup

## 原理：
### 1.模拟登陆北师珠正方教务系统
### 2.模拟提交post请求，等同于点击查询成绩按钮

## 使用方法：
### 1.修改TextBox1和TextBox2分别为自己的账号密码
### 2.修改email函数中发送方的邮箱和授权码（邮箱需要开启SMTP服务），收件方邮箱
### 3.修改checkgpa函数中checkgpaurl = 'http://es.bnuz.edu.cn/jwgl/xscjcx.aspx?xh=1702050213&xm=&gnmkdm=N121605' 中的1702050213为自己的学号，修改ccd_xn_ClientState和ddlXN为想要查询的学年，修改ccd_xq_ClientState和ddlXQ为想要查询的学期
### 3.修改check函数中的gv_xscj_ctl03_hlink_kcxx，正方的习惯是第一门成绩为02。即没有成绩的时候修改为gv_xscj_ctl02_hlink_kcxx，出了一门或多门成绩就进入教务系统查询成绩页面查看源代码，查看课程最大的数为多少，修改为这个数+1即可。

## PS：
### 可以把python脚本放到云服务器上24小时跑，一旦有了这个成绩核对单就会发邮件。
### 这个脚本适合焦虑症的学霸和学渣们。
