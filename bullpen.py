import Main

print("bullpen !!!")
for year in range(2000, 2020):
    xxx = Main.kabuka_class()
    kabuka_data = xxx.kabuka("https://kabuoji3.com/stock/6501/{}/".format(str(year)))
print("FINISH !!!!!")
