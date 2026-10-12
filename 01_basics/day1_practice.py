#温度转换:摄氏转华氏
c = float(input("请输入摄氏温度 :"))
f = (c*9/5)+32
print(f"{c} 摄氏度 =“{f} 华氏度")


#BMI 
height = float(input("请输入身高(米): "))
weight = float(input("请输入体重(千克): "))
bmi = weight / (height ** 2)
print(f"您的BMI值为: {bmi:.2f}")