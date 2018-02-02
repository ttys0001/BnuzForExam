
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup
import time
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


# In[8]:


def checkgpa():
    checkgpaurl = "http://es.bnuz.edu.cn/jwgl/xscjcx.aspx?xh=1702050213&xm=&gnmkdm=N121605"
    headers1= {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Content-Length": "3475",
            "Connection":"keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host":"es.bnuz.edu.cn",
            "Origin": "http://es.bnuz.edu.cn",
            "Referer": url,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            "X-MicrosoftAjax":"Delta=true"
    }
    parameters= {
            "ScriptManager1":"ScriptManager1|Button1",
            "ScriptManager1_HiddenField":";;AjaxControlToolkit, Version=1.0.20229.20821, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:el:c5c982cc-4942-4683-9b48-c2c58277700f:e2e86ef9:1df13a87:af22e781",
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE":"",
            "__VIEWSTATEGENERATOR": "0FF955E6",
            "__VIEWSTATEENCRYPTED": "",
            "ccd_xn_ClientState":"2017-2018:::2017-2018",
            "ccd_xq_ClientState":"1:::1",
            "ddlXN":"2017-2018",
            "ddlXQ":"1",
            "hiddenInputToUpdateATBuffer_CommonToolkitScripts":"1",
            "__ASYNCPOST": "true",
            "Button1": "按学期查询"
    }
    gpacheckpost=s.post(checkgpaurl,data=parameters,headers=headers1)
    return gpacheckpost.content


# In[9]:


def email(content1):
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    
    msg_from=''                                 #发送方邮箱
    passwd=''                                   #填入发送方邮箱的授权码
    msg_to=''                                  #收件人邮箱
    subject = "北师珠正方教务系统成绩查询"                                     #主题
    msg = MIMEText(content1, 'plain', 'utf-8')
    msg['From'] = _format_addr('超级黑客管理员 <%s>' % msg_from)
    msg['To'] = _format_addr('管理员 <%s>' % msg_to)
    msg['Subject'] = Header('北师珠正方教务系统成绩查询', 'utf-8').encode()
    try:
        a = smtplib.SMTP_SSL("smtp.qq.com",465)
        a.login(msg_from, passwd)
        a.sendmail(msg_from, msg_to, msg.as_string())
        print "发送成功"
    except a.SMTPException,e:
        print "发送失败"
    finally:
        a.quit()


# In[10]:


def check(text,state):
    if state == 0:
        if 'gv_xscj_ctl03_hlink_kcxx' in content:
            email(text)
            return 1
        else:
            print("还没有出新的成绩")
            return 0
    else:
        print("已经查询过了")


# In[11]:


while(1):
    global state
    url = 'http://es.bnuz.edu.cn/default2.aspx'
    headers= {
            "Upgrade-Insecure-Requests":"1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    s=requests.Session()
    index=s.get(url,headers=headers)
    soup=BeautifulSoup(index.content,'html5lib')
    value1=soup.find('input',id='__VIEWSTATE')['value']
    value2=soup.find('input',id='__PREVIOUSPAGE')['value']
    value3=soup.find('input',id='__EVENTVALIDATION')['value']
    payload={"__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE":
            value1,
            "__VIEWSTATEGENERATOR": "09394A33",
            "__PREVIOUSPAGE": value2,
            "__EVENTVALIDATION": value3,
            "TextBox1": "" ,
            "TextBox2": "",
            "RadioButtonList1": "学生",
            "Button4_test": ""
        }
    post1=s.post(url,data=payload,headers=headers)
    state=0
    time.sleep(60)
    content = checkgpa()
    state = check(content,state)
    if state == 1:
        break

