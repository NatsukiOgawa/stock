import matplotlib.pyplot as plt
import scraping_methods

if __name__ == '__main__':
    yyy = scraping_methods.kabuoji3_class()
    kabuka_data = yyy.kabuoji3("https://kabuoji3.com/stock/6501/")
    # kabuka_data = yyy.kabuoji3("https://kabuoji3.com/stock/3668/2018/")
    for i in range(len(kabuka_data)):
        print(kabuka_data[i])
    # print("@")
    # print("@")
    # print("@")
    # for i in range(7):
    #     print(kabuka_data[len(kabuka_data)-1][i])
    for i in range(len(kabuka_data)):
        print(kabuka_data[i])

    plt.show()



"""
[yahoo のサイト]
https://info.finance.yahoo.co.jp/history/?code=6501.T&sy=2019&sm=9&sd=9&ey=2019&em=12&ed=8&tm=d
https://info.finance.yahoo.co.jp/history/?code=6501.T&sy=2018&sm=9&sd=9&ey=2019&em=12&ed=8&tm=d
https://info.finance.yahoo.co.jp/history/?code=6501.T&sy=2017&sm=9&sd=9&ey=2019&em=12&ed=8&tm=d
https://info.finance.yahoo.co.jp/history/?code=6501.T&sy=2017&sm=7&sd=9&ey=2019&em=12&ed=8&tm=d

https://info.finance.yahoo.co.jp/history/?code=6501.T&sy=<<始めの年>>&sm=<<始めの月>>&sd=<<始めの日>>&ey=<<終わりの年>>&em=<<終わりの月>>&ed=<終わりの日>&tm=d
"""
