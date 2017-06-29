# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

heigh_str=input('请输入你的身高')
weight_str=input('请输入你的体重')
height_int=float(heigh_str)
weight_int=float(weight_str)
temp=height_int/weight_int
bim=temp**2
result=''
if bim <= 18.5:
    result='过轻'
elif(bim>18.5 and bim<25):
    result='正常'
elif(bim>25 and bim<28):
    result='过重'
elif(bim>28 and bim<32):
    result='肥胖'
else:
    result='严重肥胖'

print(result)