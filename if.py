height = float(input("请输入身高（米）： "));
weight = float(input("请输入体重（kg）： "));
bmi = (weight/(height * height));
if(bmi < 18.5):
    print("过轻");
elif(bmi < 25):
    print("正常");
elif(bmi < 28):
    print("过重");
elif(bmi < 32):
    print("肥胖");
else:
    print("严重肥胖");
