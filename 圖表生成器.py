from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
#設定基礎視窗
window = Tk()
window.title('Charts factory') # 視窗名稱
window.geometry('190x290+600+150') # 寬x高
#window.minsize(width=500,height=300) # 設定視窗最小值
#window.maxsize(width=700,height=400) #設定視窗最大值
window.resizable(False,False) #設定視窗不可縮放
window.config(background='#666666') # 設定視窗背景顏色
window.attributes('-topmost',True) #視窗置頂，False = 關閉
#set help
def help():
    win= Tk()
    win.title('Help')
    win.geometry('450x300+700+150')
    win.resizable(False,False) #設定視窗不可縮放
    win.config(background='#666666') # 設定視窗背景顏色
    win.attributes('-topmost',True) #視窗置頂，False = 關閉

    lbl_tittle = Label(win,text='圖表生成器說明事項',font=("Arial Bold",30)) #字體和大小
    lbl_tittle.config(bg='#666666',fg='#FCFCFC',width=25,height=2) # 設定參數
    lbl_intro1 = Label(win,text='1.各個輸入窗口解釋 : title:標題 、 label:數據名稱 、',font=("Arial Bold",12))
    lbl_intro2 = Label(win,text='data(x/y):數據(x軸/y軸) 、 color:顏色 、 bins:資料分散程度',font=("Arial Bold",12))
    lbl_intro3 = Label(win,bg='#666666',fg='#FCFCFC')
    lbl_intro4 = Label(win,text='2.有兩個以上的資料之間請使用英文逗號“ , ”' ,font=("Arial Bold",12))
    lbl_intro5 = Label(win,text='Ex : 12,45,53 或 red,green,blue' ,font=("Arial Bold",12))
    lbl_intro1.config(bg='#666666',fg='#FCFCFC')
    lbl_intro2.config(bg='#666666',fg='#FCFCFC')
    lbl_intro4.config(bg='#666666',fg='#FCFCFC')
    lbl_intro5.config(bg='#666666',fg='#FCFCFC')
    lbl_tittle.pack()  
    lbl_intro1.pack()
    lbl_intro2.pack()
    lbl_intro3.pack()
    lbl_intro4.pack()
    lbl_intro5.pack()
    win.mainloop()
    

#set selected title
lbl_selected = Label(text='Chart kinds',font=('Arial Bold',15))
lbl_selected.config(bg='#666666',fg='#FCFCFC',width=10,height=2)
lbl_selected.pack()

#set selected
selected = IntVar()
#set selected_button_1
rad1 = Radiobutton(window,text='圓餅圖', value=1,variable=selected)
rad1.pack(anchor = CENTER, pady= 10, padx = 10)
#set selected_button_2
rad2 = Radiobutton(window,text='長條圖', value=2, variable=selected)
rad2.pack(anchor = CENTER, pady= 10, padx = 10)
#set selected_button_3
rad3 = Radiobutton(window,text='散佈圖', value=3, variable=selected)
rad3.pack(anchor = CENTER, pady= 10, padx = 10)
#set selected_button_4
rad4 = Radiobutton(window,text='直方圖', value=4, variable=selected)
rad4.pack(anchor = CENTER, pady= 10, padx = 10)

#def choose
def choose():
    def pie():
        a = txt_3.get()
        a = a.split(',')
        b = txt_2.get()
        b = b.split(',')
        c = txt_4.get()
        c = c.split(',')
        d = txt_1.get()

        if (len(a)!=len(b)):
            messagebox.showwarning('error', '資料，顏色和名稱數目需要一致')
        elif (len(a)!=len(c)):
            messagebox.showwarning('error', '資料，顏色和名稱數目需要一致')
        elif (len(b)!=len(c)):
            messagebox.showwarning('error', '資料，顏色和名稱數目需要一致')
        else:
            plt.pie(a,colors=c,labels=b,counterclock=False, shadow=True)
            plt.title(d,fontsize=20)
            plt.show()
            lbl_1.place_forget()
            txt_1.place_forget()
            lbl_2.place_forget()
            txt_2.place_forget()
            lbl_3.place_forget()
            txt_3.place_forget()
            lbl_4.place_forget()
            txt_4.place_forget()
            btn_pie.place_forget()
    def bar():
        lebel= txt_1.get().split(',')
        lebel = list(lebel)
        len_lebel = np.arange(len(lebel))
        data= txt_2.get().split(',')
        data = list(map(int,data))
        if (len(lebel)!=len(data)):
            messagebox.showwarning('error', '資料和名稱數目需要一致')
        else:
            plt.bar(len_lebel,data,color='blue',edgecolor='black')
            plt.xticks(len_lebel,lebel)
            plt.show()
            lbl_1.place_forget()
            lbl_2.place_forget()
            txt_1.place_forget()
            txt_2.place_forget()
            btn_bar.place_forget()
    def scatter():
        data_x = txt_1.get().split(',')
        data_x = list(map(int,data_x))
        data_y = txt_2.get().split(',')
        data_y = list(map(int,data_y))
        if (len(data_x)!=len(data_y)):
            messagebox.showwarning('error','資料數目需要一致')
        else:
            plt.scatter(data_x,data_y)
            plt.show()
            lbl_1.place_forget()
            lbl_2.place_forget()
            txt_1.place_forget()
            txt_2.place_forget()
            btn_scatter.place_forget()
        
    def hist():
        data = txt_1.get().split(',')
        data = list(map(int,data))
        x = txt_2.get()
        x = int(x)
        color = txt_3.get()
        title = txt_4.get()
        lable = txt_5.get()
        plt.hist(data,bins=x,histtype='step',align='mid',color=color,label=lable,edgecolor='black')
        plt.legend(loc=2)
        plt.title(title)
        plt.show()
        lbl_1.place_forget()
        txt_1.place_forget()
        lbl_2.place_forget()
        txt_2.place_forget()
        lbl_3.place_forget()
        txt_3.place_forget()
        lbl_4.place_forget()
        txt_4.place_forget()
        lbl_5.place_forget()
        txt_5.place_forget()
        btn_hist.place_forget()

    c = selected.get()

    if c == 1:
        window1 = Tk()
        window1.title('pie') # 視窗名稱
        window1.geometry('150x350') # 寬x高
        window1.resizable(False,False) #設定視窗不可縮放
        window1.config(background='#666666') # 設定視窗背景顏色
        window1.attributes('-topmost',True) #視窗置頂，False = 關閉

        lbl_1 = Label(window1,text='title',font=('Arial Bold',15))
        lbl_1.config(bg='#666666',fg='#FCFCFC',width=15,height=2)
        txt_1 = Entry(window1,width=15)
        lbl_2 = Label(window1,text= 'label',font=('Arial Bold',15))
        lbl_2.config(bg='#666666',fg='#FCFCFC',width=15,height=2)
        txt_2 = Entry(window1,width=15)
        lbl_3 = Label(window1,text='data',font=("Arial Bold",15))
        lbl_3.config(bg='#666666',fg='#FCFCFC',width=15,height=2)
        txt_3 = Entry(window1,width=15)
        lbl_4 = Label(window1,text='color',font=("Arial Bold",15))
        lbl_4.config(bg='#666666',fg='#FCFCFC',width=15,height=2)
        txt_4 = Entry(window1,width=15)
        btn_pie = Button(window1,text='ok',bg = '#D9FFFF',fg='black',width=6,height=2,command=pie)
        btn_help = Button(window1,text='Help',fg='black',width=3,height=2,command=help)
        lbl_1.pack()
        txt_1.pack()
        lbl_2.pack()
        txt_2.pack()
        lbl_3.pack()
        txt_3.pack()
        lbl_4.pack()
        txt_4.pack()
        btn_pie.pack(side=RIGHT)
        btn_help.pack(side=LEFT)
        
    elif c == 2:
        window2 = Tk()
        window2.title('bar') # 視窗名稱
        window2.geometry('150x230') # 寬x高
        window2.resizable(False,False) #設定視窗不可縮放
        window2.config(background='#666666') # 設定視窗背景顏色
        window2.attributes('-topmost',True) #視窗置頂，False = 關閉

        lbl_1 = Label(window2,text='label',font=('Arial Bold',15))
        lbl_1.config(bg='#666666',fg='#FCFCFC',width=15,height=2)
        txt_1 = Entry(window2,width=15)
        lbl_2 = Label(window2,text= 'data',font=('Arial Bold',15))
        lbl_2.config(bg='#666666',fg='#FCFCFC',width=15,height=2)
        txt_2 = Entry(window2,width=15)
        btn_bar = Button(window2,text='ok',bg = '#D9FFFF',fg='black',width=6,height=2,command=bar)
        btn_help = Button(window2,text='Help',fg='black',width=3,height=2,command=help)
        lbl_1.pack()
        txt_1.pack()
        lbl_2.pack()
        txt_2.pack()
        btn_bar.pack(side=RIGHT)
        btn_help.pack(side=LEFT)
        
    elif c ==3:
        window3 = Tk()
        window3.title('scatter') # 視窗名稱
        window3.geometry('150x230') # 寬x高
        window3.resizable(False,False) #設定視窗不可縮放
        window3.config(background='#666666') # 設定視窗背景顏色
        window3.attributes('-topmost',True) #視窗置頂，False = 關閉

        lbl_1 = Label(window3,text='data_x',font=('Arial Bold',15))
        lbl_1.config(bg='#666666',fg='#FCFCFC',width=15,height=2)
        txt_1 = Entry(window3,width=15)
        lbl_2 = Label(window3,text= 'data_y',font=('Arial Bold',15))
        lbl_2.config(bg='#666666',fg='#FCFCFC',width=15,height=2)
        txt_2 = Entry(window3,width=15)
        btn_scatter = Button(window3,text='ok',bg = '#D9FFFF',fg='black',width=6,height=2,command=scatter)
        btn_help = Button(window3,text='Help',fg='black',width=3,height=2,command=help)
        lbl_1.pack()
        txt_1.pack()
        lbl_2.pack()
        txt_2.pack()
        btn_scatter.pack(side=RIGHT)
        btn_help.pack(side=LEFT)

    if c == 4:
        window4 = Tk()
        window4.title('hist') # 視窗名稱
        window4.geometry('150x400') # 寬x高
        window4.resizable(False,False) #設定視窗不可縮放
        window4.config(background='#666666') # 設定視窗背景顏色
        window4.attributes('-topmost',True) #視窗置頂，False = 關閉

        lbl_1 = Label(window4,text='data',font=('Arial Bold',15))
        lbl_1.config(bg='#666666',fg='#FCFCFC',width=15,height=2)
        txt_1 = Entry(window4,width=15)
        lbl_2 = Label(window4,text= 'bins',font=('Arial Bold',15))
        lbl_2.config(bg='#666666',fg='#FCFCFC',width=15,height=2)
        txt_2 = Entry(window4,width=15)
        lbl_3 = Label(window4,text='color',font=("Arial Bold",15))
        lbl_3.config(bg='#666666',fg='#FCFCFC',width=15,height=2)
        txt_3 = Entry(window4,width=15)
        lbl_4 = Label(window4,text='title',font=("Arial Bold",15))
        lbl_4.config(bg='#666666',fg='#FCFCFC',width=15,height=2)
        txt_4 = Entry(window4,width=15)
        lbl_5 = Label(window4,text='label',font=("Arial Bold",15))
        lbl_5.config(bg='#666666',fg='#FCFCFC',width=15,height=2)
        txt_5 = Entry(window4,width=15)
        btn_hist = Button(window4,text='ok',bg = '#D9FFFF',fg='black',width=6,height=2,command=hist)
        btn_help = Button(window4,text='Help',fg='black',width=3,height=2,command=help)
        lbl_1.pack()
        txt_1.pack()
        lbl_2.pack()
        txt_2.pack()
        lbl_3.pack()
        txt_3.pack()
        lbl_4.pack()
        txt_4.pack()
        lbl_5.pack()
        txt_5.pack()
        btn_hist.pack(side=RIGHT)
        btn_help.pack(side=LEFT)
             
#set check_buttom
ok = Button(text='ok',command=choose)
ok.config(bg='#D9FFFF',fg='black',width=8,height=2)
ok.place(x=58,y=240)

window.mainloop()