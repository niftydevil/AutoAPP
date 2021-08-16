import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

# 新建一个字典参数，用来传参
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'd878c3e7'
desired_caps['appPackage'] = 'com.yitantech.gaigai'
# desired_caps['appActivity'] = 'com.bx.login.login.LoginHomeActivity'
desired_caps['appActivity'] = 'com.bx.splash.SplashActivity'
# 通过访问服务端指定端口，传参，调起客户端APP
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 用户协议与隐私保护，选"同意并继续"
agree1 = driver.find_element_by_id('commit')
if agree1:
    agree1.click()
time.sleep(1)
# 允许"比心"拨打电话和管理通话吗？选"允许"
agree2 = driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button') #id只是根据"permission_allow_button"定位不到元素，需要完整的路径，因为可能不是同一个包里面的页面
if agree2:
    agree2.click()
time.sleep(1)
# 选择手机号登录
driver.find_element_by_id('loginButtonText').click()
time.sleep(1)
# 选择密码登录
driver.find_element_by_id('switchControl').click()
# 输入手机号和验证码
driver.find_element_by_id('phone_et').send_keys('13120200909')
driver.find_element_by_id('password_et').send_keys('123456')
driver.find_element_by_id('login_commit').click()
time.sleep(5)

# 进入APP之后，Google弹框是否要保存密码，选择"保存"
driver.find_element_by_id('android:id/autofill_save_yes').click()

# 首页弹框
popover = driver.find_elements("id", "ivActivityImg")
print(popover)
print(type(popover))
# print(driver.find_element_by_id('ivActivityImg'))
# popover1 = driver.find_element_by_id('ivActivityImg')
# print(driver.find_element_by_id('ivActivityImg'))
# print(popover1.toString())

if driver.find_elements(By.ID, "ivActivityImg"):
    # 首页的弹框，不想进入活动页，就点击页面出弹框以外的任意位置
    action = TouchAction(driver)
    action.tap(x=830, y=2000).perform()
    # 首页的弹框，点击弹框，进入活动页
#     popover1.click()
#     time.sleep(5)
#     # 返回首页
#     driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[2]').click()

# 点击页面底部按钮，跳转到"我的"页面
# driver.find_element_by_xpath('').click()
time.sleep(2)
driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="icon"])[5]').click()






