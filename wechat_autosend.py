#coding=utf-8
import itchat,time,random

#定义群号、发送时间和消息
roomname=u'群号'
t=[10,18]
msg=[u'XXX在家休息，一切正常。',u'XXX在商场购物，一切正常。',u'XXX陪老婆逛街，一切正常。',u'XXX在亲戚家聚会，一切正常。']


#登录
itchat.auto_login(enableCmdQR=True)

#获取群username
itchat.get_chatrooms(update=True)
time.sleep(1)#无此暂停会报错
chatroom=itchat.search_chatrooms(name=roomname)[0]['UserName']

#定时发送消息
while True:
    current_time=time.localtime()
    if(((current_time.tm_hour==t[0]) and (current_time.tm_min==0) and (current_time.tm_sec==0)) or ((current_time.tm_hour==t[1]) and (current_time.tm_min==0) and (current_time.tm_sec==0))):
        itchat.send(random.choice(msg),chatroom)
        time.sleep(1)
