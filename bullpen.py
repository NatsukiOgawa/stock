import os
import time
import datetime


class file_name_dates_class():
    def file_name_dates(self):
        now = datetime.datetime.now()
        now_id = now
        now_id = str(now_id)

        id = ""
        for i in range(20, 26):
            id += str(now_id[i])
        file_name = now.strftime('%Y' + "年" + '%m' + "月" + '%d' + "日" + '%H' + "時" + '%M' + "分" + '%S' + "秒")
        no_mili = file_name
        file_name += id
        # print(file_name)
        return file_name, no_mili

aaa = file_name_dates_class()
aaa_aaa = aaa.file_name_dates()
# os.system('git add *')
# os.system('git commit -m "test commit"')
os.system('git add *')
os.system('git commit -m "{}"'.format(aaa_aaa[0]))
os.system('git push')
# os.system('git push')
