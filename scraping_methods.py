import matplotlib.pyplot as plt

class kabuoji3_class():
    def kabuoji3(self, url):
        import urllib.request, urllib.error
        from bs4 import BeautifulSoup
        import csv

        self.url = url
        # url = "https://kabuoji3.com/stock/6501/2019/"
        # URLを指定する
        html = urllib.request.urlopen(url)
        # URLを開く
        soup = BeautifulSoup(html, "html.parser")
        # BeautifulSoup で開く
        # HTMLからニュース一覧に使用しているaタグを絞りこんでいく
        aaa = soup.select(".data_contents")
        news_tag = soup.select("td") ###
        # print (news_tag)
        data_list_x = [[0 for i in range(7)] for k in range(int(len(news_tag)/7))]
        num = 0
        for i in range(0, int(len(news_tag) / 7)):
            for k in range(7):
                data_list_x[i][k] = news_tag[num]
                num += 1
        """
        for i in range(int(len(news_tag) / 7)):
            print(data_list_x[i])
        """
        csvlist = [["","ニュースリスト"]]
        num = 0
        for news_txt in news_tag:
            news_txt = news_txt.text
            csvlist.append([num, news_txt])
            num += 1
        # CSVファイルを開く。ファイルがなければ新規作成する。
        f = open("output.csv", "w")
        writecsv = csv.writer(f, lineterminator='\n')
        # 出力
        writecsv.writerows(csvlist)
        # CSVファイルを閉じる。
        f.close()
        for k in range(len(data_list_x)):
            z = data_list_x[k][0]
            # print()
            # print(z)
            z = str(z).replace("<td>", "").replace("</td>", "")
            # print(z)
            data_list_x[k][0] = str(z)
            # print(data_list_x[len(data_list_x)-1][i])
        for k in range(len(data_list_x)):
            for i in range(1, 7):
                z = data_list_x[k][i]
                # print()
                # print(z)
                z = str(z).replace("<td>", "").replace("</td>", "")
                # print(z)
                data_list_x[k][i] = float(z)
                # print(data_list_x[len(data_list_x)-1][i])
        dates = [0 for i in range(len(data_list_x))]
        qqq = [0 for i in range(len(data_list_x))]
        www = [0 for i in range(len(data_list_x))]
        eee = [0 for i in range(len(data_list_x))]
        rrr = [0 for i in range(len(data_list_x))]
        ttt = [0 for i in range(len(data_list_x))]
        yyy = [0 for i in range(len(data_list_x))]
        for i in range(len(data_list_x)):
            qqq[i] = data_list_x[i][1]
            www[i] = data_list_x[i][2]
            eee[i] = data_list_x[i][3]
            rrr[i] = data_list_x[i][4]
            ttt[i] = data_list_x[i][5]
            yyy[i] = data_list_x[i][6]
        plt.plot(range(1, len(data_list_x)+1), qqq, label="Opening Price")
        # plt.plot(range(1, len(data_list_x)+1), www, label="High Price")
        # plt.plot(range(1, len(data_list_x)+1), eee, label="Low Price")
        # plt.plot(range(1, len(data_list_x)+1), rrr, label="Closing Price")
        # plt.plot(range(1, len(data_list_x)+1), ttt, label="出来高")
        # plt.plot(range(1, len(data_list_x)+1), yyy, label="終値調整")
        return data_list_x

class finance_yahoo_class():
    def finance_yahoo(self, url):
        import urllib.request, urllib.error
        from bs4 import BeautifulSoup
        import csv

        self.url = url
        # url = "https://finance_yahoo.com/stock/6501/2019/"
        # URLを指定する
        html = urllib.request.urlopen(url)
        # URLを開く
        soup = BeautifulSoup(html, "html.parser")
        # BeautifulSoup で開く
        # HTMLからニュース一覧に使用しているaタグを絞りこんでいく
        aaa = soup.select(".padT12 marB10 clearFix")
        news_tag = soup.select("td") ###
        # print (news_tag)
        data_list_x = [[0 for i in range(7)] for k in range(int(len(news_tag)/7))]
        num = 0
        for i in range(0, int(len(news_tag) / 7)):
            for k in range(7):
                data_list_x[i][k] = news_tag[num]
                num += 1
        """
        for i in range(int(len(news_tag) / 7)):
            print(data_list_x[i])
        """
        csvlist = [["","ニュースリスト"]]
        num = 0
        for news_txt in news_tag:
            news_txt = news_txt.text
            csvlist.append([num, news_txt])
            num += 1
        # CSVファイルを開く。ファイルがなければ新規作成する。


        print(news_tag)
        print(len(news_tag))
        for i in range(len(news_tag)):
            print(news_tag[i])


        f = open("output.csv", "w")
        writecsv = csv.writer(f, lineterminator='\n')
        # 出力
        writecsv.writerows(csvlist)
        # CSVファイルを閉じる。
        f.close()
        for k in range(len(data_list_x)):
            z = data_list_x[k][0]
            # print()
            # print(z)
            z = str(z).replace("<td>", "").replace("</td>", "")
            # print(z)
            data_list_x[k][0] = str(z)
            # print(data_list_x[len(data_list_x)-1][i])
        for k in range(len(data_list_x)):
            for i in range(1, 7):
                z = data_list_x[k][i]
                # print()
                # print(z)
                z = str(z).replace("<td>", "").replace("</td>", "")
                # print(z)
                data_list_x[k][i] = float(z)
                # print(data_list_x[len(data_list_x)-1][i])
        qqq = [0 for i in range(len(data_list_x))]
        www = [0 for i in range(len(data_list_x))]
        eee = [0 for i in range(len(data_list_x))]
        rrr = [0 for i in range(len(data_list_x))]
        ttt = [0 for i in range(len(data_list_x))]
        yyy = [0 for i in range(len(data_list_x))]
        for i in range(len(data_list_x)):
            qqq[i] = data_list_x[i][1]
            www[i] = data_list_x[i][2]
            eee[i] = data_list_x[i][3]
            rrr[i] = data_list_x[i][4]
            ttt[i] = data_list_x[i][5]
            yyy[i] = data_list_x[i][6]
        plt.plot(range(1, len(data_list_x)+1), qqq, label="Opening Price")
        plt.plot(range(1, len(data_list_x)+1), www, label="High Price")
        plt.plot(range(1, len(data_list_x)+1), eee, label="Low Price")
        plt.plot(range(1, len(data_list_x)+1), rrr, label="Closing Price")
        # plt.plot(range(1, len(data_list_x)+1), ttt, label="出来高")
        # plt.plot(range(1, len(data_list_x)+1), yyy, label="終値調整")
        plt.legend(loc='lower right')
        return data_list_x

class setsunan_syusseki_class():
    def setsunan_syusseki(self, url):
        import urllib.request, urllib.error
        from bs4 import BeautifulSoup
        import csv

        self.url = url
        # url = "https://finance_yahoo.com/stock/6501/2019/"
        # URLを指定する
        html = urllib.request.urlopen(url)
        # URLを開く
        soup = BeautifulSoup(html, "html.parser")
        # BeautifulSoup で開く
        # HTMLからニュース一覧に使用しているaタグを絞りこんでいく
        aaa = soup.select(".padT12 marB10 clearFix")
        news_tag = soup.select("td") ###
        # print (news_tag)
        data_list_x = [[0 for i in range(7)] for k in range(int(len(news_tag)/7))]
        num = 0
        for i in range(0, int(len(news_tag) / 7)):
            for k in range(7):
                data_list_x[i][k] = news_tag[num]
                num += 1
        """
        for i in range(int(len(news_tag) / 7)):
            print(data_list_x[i])
        """
        csvlist = [["","ニュースリスト"]]
        num = 0
        for news_txt in news_tag:
            news_txt = news_txt.text
            csvlist.append([num, news_txt])
            num += 1
        # CSVファイルを開く。ファイルがなければ新規作成する。


        print(news_tag)
        print(len(news_tag))
        for i in range(len(news_tag)):
            print(news_tag[i])


        f = open("output.csv", "w")
        writecsv = csv.writer(f, lineterminator='\n')
        # 出力
        writecsv.writerows(csvlist)
        # CSVファイルを閉じる。
        f.close()
        for k in range(len(data_list_x)):
            z = data_list_x[k][0]
            # print()
            # print(z)
            z = str(z).replace("<td>", "").replace("</td>", "")
            # print(z)
            data_list_x[k][0] = str(z)
            # print(data_list_x[len(data_list_x)-1][i])
        for k in range(len(data_list_x)):
            for i in range(1, 7):
                z = data_list_x[k][i]
                # print()
                # print(z)
                z = str(z).replace("<td>", "").replace("</td>", "")
                # print(z)
                data_list_x[k][i] = float(z)
                # print(data_list_x[len(data_list_x)-1][i])
        qqq = [0 for i in range(len(data_list_x))]
        www = [0 for i in range(len(data_list_x))]
        eee = [0 for i in range(len(data_list_x))]
        rrr = [0 for i in range(len(data_list_x))]
        ttt = [0 for i in range(len(data_list_x))]
        yyy = [0 for i in range(len(data_list_x))]
        for i in range(len(data_list_x)):
            qqq[i] = data_list_x[i][1]
            www[i] = data_list_x[i][2]
            eee[i] = data_list_x[i][3]
            rrr[i] = data_list_x[i][4]
            ttt[i] = data_list_x[i][5]
            yyy[i] = data_list_x[i][6]
        plt.plot(range(1, len(data_list_x)+1), qqq, label="Opening Price")
        plt.plot(range(1, len(data_list_x)+1), www, label="High Price")
        plt.plot(range(1, len(data_list_x)+1), eee, label="Low Price")
        plt.plot(range(1, len(data_list_x)+1), rrr, label="Closing Price")
        # plt.plot(range(1, len(data_list_x)+1), ttt, label="出来高")
        # plt.plot(range(1, len(data_list_x)+1), yyy, label="終値調整")
        plt.legend(loc='lower right')
        return data_list_x


import matplotlib.pyplot as plt

if __name__ == '__main__':
    # yyy = finance_yahoo_class()
    # kabuka_data = yyy.finance_yahoo("https://stocks.finance.yahoo.co.jp/stocks/history/?code=6501.T")
    yyy = setsunan_syusseki_class()
    kabuka_data = yyy.setsunan_syusseki("https://stocks.finance.yahoo.co.jp/stocks/history/?code=6501.T")
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
