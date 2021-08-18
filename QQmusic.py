import time
import csv

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://y.qq.com/n/ryqq/songDetail/0006wgUu1hHP0N")
driver.maximize_window()

num = int(input('请输入目标评论数:'))

_single = True
while _single:
    items = driver.find_elements_by_xpath("//li[@class='comment__list_item c_b_normal']")
    print(len(items))
    if len(items) < num:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    else:
        _single = False

info_list = []
for index, item in enumerate(items):
    dic = {}
    try:  # 以防万一,try语句,便于爬虫进行
        headPortraits = item.find_element_by_xpath("./div[1]/a/img").get_attribute('src')
        # 头像图片链接
        name = item.find_element_by_xpath("./div[1]/h4/a").text  # 昵称
        time = item.find_element_by_xpath("./div[1]/div[1]").text  # 评论时间
        content = item.find_element_by_xpath("./div[1]/p/span").text  # 评论内容
        content = content.replace('\n', '')
        # 因为考虑到有的用户评论较长,所以需要将换行符改成空格或者空字符,便于存储

        dic['headPor'] = headPortraits
        dic['name'] = name
        dic['time'] = time
        dic['cont'] = content
        print(index + 1)
        print(dic)
        info_list.append(dic)

    except Exception as e:
        print(e)

head = ['headPor','name','time','cont']
with open('bscxComment.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, head)
    writer.writeheader()
    writer.writerows(info_list)
    print('写入成功')