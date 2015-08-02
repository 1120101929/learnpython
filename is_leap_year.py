#a = int(input("请输入年龄："))
#if(a >= 18):
#    print("adult")
#else:
#    print("teenager")
year = int(input("请输入年份: "));
if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    print("闰年");
else:
    print("非闰年");
