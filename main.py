from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import  xlwt

from xlutils.copy import copy
import xlrd
work = xlrd.open_workbook("index.xls")

workbook = copy(wb=work)
worksheet=workbook.get_sheet(0)
web = Edge(r"C:\Users\he\PycharmProjects\pythonProject\venv\Scripts\msedgedriver.exe")
w='https://search.douban.com/book/subject_search?search_text=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&cat=1001'
web.get(w)
ind = 205
w='https://search.douban.com/book/subject_search?search_text=%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86&cat=1001&start=0'
web.get(w)
for i in range(6):
    for j in range(15):
        st = "/html/body/div[3]/div[1]/div/div[2]/div[1]/div[1]/div[" + str(j +1) + "]/div/div/div[1]/a"
        div = web.find_element(By.XPATH, st)
        title = div.text
        flag=0
        div.click()
        try:
            bot = web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div[3]/div[4]/a')
            bot.click()
            index = web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div[3]/div[5]').text
            with open(str(ind) + ".txt", "w") as f:
                f.write(index)
            ind=ind+1
        except:
            try:
                bot = web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div[3]/div[3]/a')
                bot.click()
                index = web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div[3]/div[4]')
                with open(str(ind) + ".txt", "w") as f:
                    f.write(index.text)
                ind=ind+1
            except:
                try:
                    bot = web.find_element(By.XPATH,
                                           ' / html / body / div[3] / div[3] / div / div[1] / div[3] / div[4] / a')
                    bot.click()
                    index = web.find_element(By.XPATH,
                                             '/ html / body / div[3] / div[3] / div / div[1] / div[3] / div[5]')
                    with open(str(ind) + ".txt", "w") as f:
                        f.write(index.text)
                    ind=ind+1
                except:
                    print("okk")
                    flag=1
        web.back()
        if (flag == 0):
            s = "/html/body/div[3]/div[1]/div/div[2]/div[1]/div[1]/div[" + str(j + 1) + "]/div/div/div[3]"
            try:
                abs = web.find_element(By.XPATH, s)
            except:
                abs = web.find_element(By.XPATH,
                                       '/html/body/div[3]/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[2]/div')
            worksheet.write(ind, 1, str(ind))
            worksheet.write(ind, 2, title)
            worksheet.write(ind, 3, abs.text)
    t='/ html / body / div[3] / div[1] / div / div[2] / div[1] / div[1] / div[16] / a['+str(13)+']'
    next = web.find_element(By.XPATH, t)
    next.click()
print(ind)
workbook.save("index.xls")