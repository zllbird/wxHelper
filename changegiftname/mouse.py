import tkinter
import random
from PIL import Image,ImageTk
from tkinter import ttk

wuya = tkinter.Tk()
wuya.title("今晚要不要写作业？")
wuya.geometry("720x960")


title = ttk.Label(wuya,text= '今天写不写作业？')
title.pack()
bt = ttk.Button(wuya, text='任性不写adfjaokdsjfojaosd')
bt.pack()

btCon = ttk.Button(wuya,text='认真书写')
btCon.pack()

canvas = tkinter.Canvas(wuya, bg='blue', height=405, width=405)
canvas.pack()

img = Image.open("190426-214659.png")


imgresize = img.resize((400,400))
print(img.size, img.mode, img.format)

# photo = ImageTk.PhotoImage(img)
photo = ImageTk.PhotoImage(imgresize)

# imgresize.show()

# image_file = tkinter.PhotoImage(photo)
image = canvas.create_image(0, 0, anchor='nw', image=photo)

# def func(event):
#     ranX = random.randint(1,300)
#     ranY = random.randint(1,200)
#     bt.place(x=ranX, y=ranY)
#     print('鼠标进入按钮')


# 绑定事件，鼠标进入按钮的时候执行func（）函数，在控制台打印：鼠标进入按钮
# bt.bind('<Enter>', func)

# 还有其他的事件
# 只需改变bind中的第一个参数，用以下对应的字符串替换即可
'''
<Button-1>        　  　鼠标左键按下，2表示中键，3表示右键；
    <ButtonPress-1>    　   同上；
    <ButtonRelease-1>　　　 鼠标左键释放；
    <B1-Motion>  　　       按住鼠标左键移动；
    <Double-Button-1>  　　 双击左键；
    <Enter>       　　      鼠标指针进入某一组件区域；
    <Leave>    　　         鼠标指针离开某一组件区域；
    <MouseWheel>  　   　　 滚动滚轮；
    <KeyPress-A> 　　  　　  按下A键，A可用其他键替代；
    <Alt-KeyPress-A>　　　   同时按下alt和A；alt可用ctrl和shift替代；
    <Double-KeyPress-A>　　  快速按两下A；
    <Lock-KeyPress-A>　　　  大写状态下按A；

'''

wuya.mainloop()