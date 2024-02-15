import  xlwt
import re
from xlutils.copy import copy
import xlrd
work = xlrd.open_workbook("index.xls")

workbook = copy(wb=work)
worksheet=workbook.get_sheet(0)
for i in range(246):
    count = 0
    try:
        f = open('merge/' + str(i) + '.txt', 'r').readlines()
        for count, line in enumerate(f):
            pass
        count += 1

        if (count > 100):
            for line in f:
                f1 = open('merge.txt', 'a')
                f1.write(line)
            worksheet.write(i + 1, 4, 1)
    except:
        worksheet.write(i + 1, 4, 0)
        print('okk')
workbook.save("index.xls")


