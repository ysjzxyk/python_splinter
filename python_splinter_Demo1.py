#!/usr/bin/env python
#coding: UTF-8
'''
  浏览器的驱动如果放在其安装目录下，并配置path后仍然不可行，可将其放在该python文件的根目录下即可解决
'''

from selenium import webdriver
import time
def login():
  dr = webdriver.Chrome()
  #打开登陆163邮箱的网页
  dr.get('http://mail.163.com/')

  #将浏览器窗口最大化
  dr.maximize_window()

  #休息五秒钟等待网页加载完毕
  time.sleep(5)

  #找到邮箱账号登录框对应的iframe

  '''注意：
    （1）如果iframe的id/name属性是唯一、不变的，可以通过可以直接使用driver.switch_to_frame("id/name")来定位到iframe。
    （2）本案例中的163邮箱的iframe的name属性是空，id属性是一个动态变化的，因此，需要另找途径来定位iframe。
        本案例使用iframe的父节点div具有唯一属性的id=loginDiv来定位。
    （3）下面代码中的用户名、密码等信息的name、id等信息可以根据具体的网站进行修改（浏览器中的查看元素进行查看）
  '''
  #由于iframe框架的id
  ele = dr.find_element_by_xpath("//*[@id='loginDiv']/iframe")#根据属性匹配和绝对路径的方式写xpath
  dr.switch_to.frame(ele)


  #找到邮箱账号输入框
  email = dr.find_element_by_name('email')

  #将自己的邮箱地址输入到邮箱账号框中
  email.send_keys('******')

  #找到密码输入框
  password = dr.find_element_by_name('password')

  #输入自己的邮箱密码
  password.send_keys('******')

  #找到登陆按钮
  login_btn = dr.find_element_by_id('dologin')

  #点击登陆按钮
  login_btn.click()

  #等待10秒看是否登陆成功
  time.sleep(10)
  #
  # dr.close()


if __name__ == '__main__':

  login()







