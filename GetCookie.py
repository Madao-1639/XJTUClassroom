from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

driver_path=os.path.join(os.environ['USERPROFILE'],'/anaconda3/envs/spider/selenium_driver/geckodriver.exe')
def GetCookie(usrname,pwd):
    driver=webdriver.Firefox(executable_path=driver_path)
    driver.get('http://ehall.xjtu.edu.cn/new/index.html?browser=no')
    loginbutton=driver.find_element(by=By.ID,value='ampHasNoLogin')
    loginbutton.click()
    driver.implicitly_wait(3)
    InputUser=driver.find_element(by=By.CLASS_NAME,value='username')
    InputUser.send_keys(usrname)
    InputPwd=driver.find_element(by=By.CLASS_NAME,value='pwd')
    InputPwd.send_keys(pwd)
    loginbutton=driver.find_element(by=By.ID,value='account_login')
    loginbutton.click()
    sleep(3)
    tempButton=driver.find_element(by=By.XPATH,value='//div[@amp-id="allCanUseApps"]')
    tempButton.click()
    sleep(3)
    tempButton=driver.find_element(by=By.XPATH,value='//span[@title="资源中心"]')
    tempButton.click()
    sleep(3)
    ClassButton=driver.find_element(by=By.XPATH,value='//div[@class="amp-category-content-item"]')
    ClassButton.click()
    driver.switch_to.window(driver.window_handles[1])
    raw_cookies=driver.get_cookies()
    driver.quit()

    Cookies_dict={
        '_WEU':'',
        'amp.locale':'',
        'asessionid':'',
        'CASTGC':'',
        'EMAP_LANG':'',
        'JSESSIONID':'',
        'MOD_AMP_AUTH':'',
        'route':'',
        'THEME':''
    }
    for cookie in raw_cookies:
        if cookie['name'] in Cookies_dict.keys():
            Cookies_dict[cookie['name']]=cookie['value']
    Cookies=[key+'='+val for key,val in Cookies_dict.items()]
    with open('Cookies','w') as f:
        f.write(';'.join(Cookies))

if __name__=='__main__':
    username='XXX'
    password='XXX'
    GetCookie(username,password)