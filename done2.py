#这是一个将用户输入的英文名（8字符以内）转换成图片
import matplotlib.pyplot as pyplot
import random
import numpy as np
import array
try:
    for i in range(1):#跑1次
        pyplot.figure(num='英文名的图片',figsize=(8,8))  #创建一个名为astronaut的窗口,并设置大小
        a=input("请输入您的英文名(8个字符以内）")
        # a="xxxxxxx"
        b=a.encode()#字符串转字节
        x=[i for i in b]#这是列表，将字节对象转成列表
        #调整列表长度为28*28
        if len(x)<9:
            for i in range(len(x),8):
                x.append(0)   
        n=(28*28)/8
        n=int(n)
        xx=x*n
        xx = np.array(xx)#将列表转一维数组
        im_mask = xx.reshape((28, 28))  # 将一维数组转成二维数组28行28列  原数组不会被修改或者覆盖
        pyplot.imshow(im_mask,pyplot.cm.summer)#图片输出，颜色设置
        pyplot.show()
        print("程序运行成功")
except:
     print("程序遇到错误")  
else:
    print("程序可以")    
finally: 
    print("程序结束")
