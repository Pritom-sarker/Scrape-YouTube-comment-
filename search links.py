from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from   selenium.common.exceptions import TimeoutException
c=0
l=open('link.txt','r')
for link in l:
    c+=1
    driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
    driver.set_window_position(-10000, 0)
    driver.get(str(link))
    import time

    SCROLL_PAUSE_TIME = 0.5


    for i in range(50):  # adjust integer value for need
        # you can change right side number for scroll convenience or destination
        driver.execute_script("window.scrollBy(0, 250)")
        # you can change time integer to float or remove
        time.sleep(1)


    html=driver.page_source.encode("utf-8")
    driver.close()
    file='pages/page{}.html'.format(c)
    f=open(file,'w')
    f.write(str(html))
    f.close()