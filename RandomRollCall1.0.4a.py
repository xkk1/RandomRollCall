from tkinter import *# 图形界面
from random import sample# 从列表里随机抽取
from random import randint# 生成随机数字
from os import remove# 删除文件
from os.path import exists# 文件、路径是否存在
from tkinter import messagebox# 对话框
from time import sleep# 暂停
# import _thread# 多线程
import threading# 多线程
import gc# 释放垃圾内存
# import tkinter.font as tkFont# 引入字体模块

file = 'Students.txt'
names = []# 读取的姓名
name = ""# 当前抽取的姓名
havenames = []
lj = 0
data = "data.txt"
zh = 90
donghua = False
bbh = "1.0.4"# 版本号



def save():
    try:
        f = open(data,"w")
        f.write(file + "\n" + str(lj) + "\n" + str(zh))
        f.close()
        print("已保存！")
    except:
        try:
            remove(data)
            f = open(data,"w")
            f.write(file + "\n" + str(lj) + "\n" + str(zh))
            f.close()
            print("已保存！(文件为隐藏！)")
        except:
            messagebox.showerror(title = '保存数据失败！',
                            message='保存数据失败！\n请确保数据文件“%s”的属性不为只读！'%data)
        
def save_exit():
    save()
    window.destroy()

def OK():
    global file
    global names
    global havenames
    fil = v1.get()
    # file = v1.get()
    if not exists(fil):
        print(exists(fil))
        messagebox.showerror(title = '未找到文件',
                            message='文件“%s”不存在！'%fil)
    else:
        try:
            """if exists(wjj+"/"+wjj):# 如果数据文件夹在
                return True# 返回真
            elif exists(wjj+".dat"):# 如果数据文件存在
                decdat(wjj)# 直接解压数据文件
                return True
            elif exists(wjj):# 如果数据文件夹存在
                f = open(wjj+"/"+wjj, "w")
                f.write(firststr)
                f.close()
                return False# 返回假
            else:
                mkdir(wjj)
                f = open(wjj+"/"+wjj, "w")
                f.write(firststr)
                f.close()
                return False"""
            """
            f = open(NamesFile,"w")
            f.write("mdzz")
            f.close()"""
            f = open(fil,"r")
            names = f.readlines()
            f.close()
            file = fil
            for i in range(len(names)):# 删掉每行多余的回车
                if i != len(names) - 1:
                    names[i] = names[i][:-1]
                else:
                    if names[i][-1] == "\n":
                        names[i] = names[i][:-1]
            for i in range(len(names)):# 删掉多余的空行（改良版）
                while i < len(names) and names[i] == "":
                    del names[i]
            """
            def del_():# 删掉多余的空行
                for i in range(len(names)):
                    if names[i] == "":
                        del names[i]
                        del_()
                        break
            del_()
            """
            print(names)
            for j in names:
                print(j)
                
            v2.set("当前姓名总数："+str(len(names)))
            v3.set("剩余姓名数："+str(len(names)))
            havenames = []
        except:
            messagebox.showerror(title = '无法打开文件',
                                 message='文件“%s”无法打开！\n请确保文件编码为GB2312'%fil)

def begin():
    global file
    global lj
    global zh
    if not exists(data):
        save()
        print("找不到数据文件！")
    else:
        f = open(data,"r")
        file = f.readline()[:-1]
        v1.set(file)
        try:
            lj = int(f.readline())
            zh = int(f.readline())
            print("读文件“%s”成功！"%data)
        except:
            print("读文件时出错！")
        f.close()
    if exists(file):
        OK()
        print("姓名文件“%s”存在！"%file)
    v1.set(file)
    # v2.set("当前姓名总数：")
    # v3.set("剩余姓名数：")
    v6.set("累计抽取人数：" + str(lj))
    lname["font"] = ('黑体', zh)
    print(zh)

def help():
    #showinto （信息提示）
    # 弹出对话框
    messagebox.showinfo(title = '帮助',message="""有事加QQ群:：681032320
使用方法：
1、默认姓名文件为本目录下的“%s”
2、一个人名占一行，不要有空白行
3、点击“随机点名”即可随机点名
4、勾选“不重复点名”后同一个人只会抽到一次
所有人全被抽到后重新开始抽
点“↓复位↓”后重置
(使用Alt + Tab切换窗口)
更新日志：
已修复文件打开闪退bug
已修复当数据文件为隐藏时程序无法关闭的bug
但是要确保数据文件的属性不为只读
增加抽取动画
增加新的抽取方式"""%file)
    # 返回值为：ok

def FW():# 复位
    global havenames
    v3.set("剩余姓名数："+str(len(names)))
    havenames = []

def join():
    global t
    t.join()
    #t.exit()
    del t
    #gc.collect()

def cqdh():# 抽取动画线程
    #####抽取动画#####
    # global donghua
    global lj,havenames
    #donghua = False
    randomnames = []
    if len(names) > 7:
        randomnames = sample(names, 7)# 随机抽取7个名字
    else:
        randomnames = names
    for i in range(len(randomnames)):
        v5.set(randomnames[i])
        sleep((i + 1) / 35)
    # donghua = True
    if not v4.get():# 判断是否选上不重复点名
        # print(v4.get(),"F")
        name = sample(names, 1)[0]# 随机抽取一个名字
        v5.set(name)
        lj += 1
        v6.set("累计抽取人数："+str(lj))
    else:
        #print(v4.get(),"???")
        name = sample(names, 1)[0]# 随机抽取一个名字
        while name in havenames:
            name = sample(names, 1)[0]# 随机抽取一个名字
        v5.set(name)
        lj += 1
        v6.set("累计抽取人数："+str(lj))
        havenames += [name]
        if len(names)-len(havenames) == 0:
            havenames = []
        v3.set("剩余姓名数："+str(len(names)-len(havenames)))
        print(havenames)
    # donghua = False
    bsjdm["text"] = "随机\n点名"
    bkszt.pack()
    # t.join()
    #join()
    print("wanbi!")

def sjdm():
    global name
    global havenames
    global lj
    global donghua
    global t
    if len(names) == 0:
        messagebox.showerror(title = '没有指定姓名文件',
                            message='没有指定姓名文件！\n或姓名文件被删除！\n请先指明姓名文件！')
    else:
        """
        #####抽取动画#####
        randomnames = []
        if len(names) > 7:
            randomnames = sample(names, 7)# 随机抽取7个名字
        else:
            randomnames = names
        for i in range(len(randomnames)):
            v5.set(randomnames[i])
            sleep((i + 1) / 10)
        #####  结束  #####
        """
        #_thread.start_new_thread( cqdh ,())
        if bsjdm["text"] == "随机\n点名":
            try:
                # _thread.start_new_thread( cqdh ,())
                t = threading.Thread(target=cqdh, args=())
                t.start()
                # t.join()
                # donghua = True
                bsjdm["text"] = "正在\n随机\n抽取"
                bkszt.pack_forget()
            except:
                # messagebox.showerror(title = '无法启动线程',
                #                      message='无法启动线程！！！')
                #elif bkszt["text"] == "正在\n随机\n抽取" and donghua:
                '''
                else:
                    donghua = False
                    bsjdm["text"] = "随机\n点名"
                    bkszt.pack()
                try:
                    #_thread.start_new_thread( cqdh, () )
                    _thread.start_new_thread( cqdh ,())
                    donghua = True
                    
                    
                    while donghua:
                        if not v4.get():# 判断是否选上不重复点名
                            # print(v4.get(),"F")
                            name = sample(names, 1)[0]# 随机抽取一个名字
                            v5.set(name)
                            lj += 1
                            v6.set("累计抽取人数："+str(lj))
                        else:
                            #print(v4.get(),"???")
                            name = sample(names, 1)[0]# 随机抽取一个名字
                            while name in havenames:
                                name = sample(names, 1)[0]# 随机抽取一个名字
                            v5.set(name)
                            lj += 1
                            v6.set("累计抽取人数："+str(lj))
                            havenames += [name]
                            if len(names)-len(havenames) == 0:
                                havenames = []
                            v3.set("剩余姓名数："+str(len(names)-len(havenames)))
                            print(havenames)
                        break
                        except:
                '''
                # donghua = True
                print ("Error: 无法启动线程")
                if not v4.get():# 判断是否选上不重复点名
                    # print(v4.get(),"F")
                    name = sample(names, 1)[0]# 随机抽取一个名字
                    v5.set(name)
                    lj += 1
                    v6.set("累计抽取人数："+str(lj))
                else:
                    #print(v4.get(),"???")
                    name = sample(names, 1)[0]# 随机抽取一个名字
                    while name in havenames:
                        name = sample(names, 1)[0]# 随机抽取一个名字
                    v5.set(name)
                    lj += 1
                    v6.set("累计抽取人数："+str(lj))
                    havenames += [name]
                    if len(names)-len(havenames) == 0:
                        havenames = []
                    v3.set("剩余姓名数："+str(len(names)-len(havenames)))
                    print(havenames)

def ks():
    zz = len(names)-1
    sj = randint(0,len(names)-1)
    print(names[sj])
    for i in range(sj ,len(names)-1):
        if donghua:
            v5.set(names[i])
            sleep(0.02)
        else:
            break
    while donghua:# 循环显示名字
        if zz == -1:
            zz = len(names)-1
        v5.set(names[zz])
        zz -= 1
        sleep(0.02)

def kszt():
    # global bkszt
    #bkszt = Button(text="暂停")
    #bkszt['text'] = 'Hello'
    '''
    bkszt = Button(f41,# 开始暂停
               text="开始",
               font=('宋体', 20),         # 字体和字体大小
               command=kszt
               ).pack()
    bkszt.text =""
    print(bkszt.text)'''
    
    global donghua
    global lj
    if len(names) == 0:
        messagebox.showerror(title = '没有指定姓名文件',
                            message='没有指定姓名文件！\n或姓名文件被删除！\n请先指明姓名文件！')
    else:
        #if bkszt["text"] == "开始" and not donghua:
        if bkszt["text"] == "开始":
            try:
                _thread.start_new_thread( ks ,())
                donghua = True
                bkszt["text"] = "\n暂停\n"
                bsjdm.pack_forget()
            except:
                messagebox.showerror(title = '无法启动线程',
                                     message='无法启动线程！！！')
        #elif bkszt["text"] == "\n暂停\n" and donghua:
        else:
            donghua = False
            bkszt["text"] = "开始"
            bkszt.pack_forget()
            bsjdm.pack()
            bkszt.pack()
            lj += 1
            v6.set("累计抽取人数："+str(lj))

def ql():
    global lj
    lj = 0
    v6.set("累计抽取人数："+str(lj))

'''
lname = Label(f4, 
        textvariable=v5,
        #text="王小明",    # 标签的文字
        #bg='green',                 # 背景颜色
        #font=ft,
        font=('黑体', 90),         # 字体和字体大小
'''
def jia():
    global zh
    # global ft
    zh += 3
    # lname.font('黑体', zh)
    # ft = tkFont.Font(root=window, family='Fixdsys', size=zh, weight=tkFont.BOLD)
    # font = tuple(['黑体', zh])
    # lname["font"] = font
    lname["font"] = ('黑体', zh)
    print("字号加%i,字号：%i"%(3, zh))

def jian():
    global zh
    # global ft
    if zh > 3:
        zh -= 3
        # lname.size(zh)
        # ft = tkFont.Font(root=window, family='Fixdsys', size=zh, weight=tkFont.BOLD)
        # font = ['黑体', zh]
        # lname["font"] = font
        lname["font"] = ('黑体', zh)
        print("字号减",zh)

if __name__ == "__main__":
    window=Tk()
    window.title("随机点名V%s"%bbh)
    window.resizable(0,0)# 禁止调节窗口大小

    # 创建一个Label
    # 指定字体名称、大小、样式
    # ft = tkFont.Font(root=window, family='Fixdsys', size=zh, weight=tkFont.BOLD)


    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    v4 = IntVar()
    v5 = StringVar()
    v6 = StringVar()

    v1.set("Students.txt")
    v2.set("当前姓名总数：0")
    v3.set("剩余姓名数：0")
    v5.set("")
    v6.set("累计抽取人数：0")

    # begin()
    # print("??????????")

    win = Frame(window)

    f1 = Frame(win)
    l1 = Label(f1, 
        text="姓名文件：",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=LEFT)    # 固定窗口位置
    e1 = Entry(f1,# 姓名文件名输入框
               textvariable=v1,
               width=55# 宽度
               ).pack(side=LEFT)
    bOK = Button(f1,
               text="确定",
               font=('宋体', 12),         # 字体和字体大小
               command=OK
               ).pack(side=RIGHT)

    f1.pack(fill=X)

    f2 = Frame(win)
    l2 = Label(f2, 
        textvariable=v2,
        # text="当前姓名总数：0",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=LEFT)    # 固定窗口位置
    bhelp = Button(f2,
               text="帮助",
               font=('宋体', 12),         # 字体和字体大小
               command=help
               ).pack(side=LEFT)
    bFW = Button(f2,
               text="↓复位↓",
               font=('宋体', 12),         # 字体和字体大小
               command=FW
               ).pack(side=RIGHT)
    f2.pack(fill=X)

    f3 = Frame(win)
    ccf = Checkbutton(f3, 
                       text='不重复点名', 
                       variable=v4, 
                       onvalue=1, 
                       offvalue=0
                       #command=print_selection
                       ).pack(side=LEFT)
    l3 = Label(f3, 
        textvariable=v3,
        text="剩余姓名数：0",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=RIGHT)    # 固定窗口位置
    f3.pack(fill=X)

    f5 = Frame(win)
    bql = Button(f5,
               text="清零",
               font=('宋体', 12),         # 字体和字体大小
               command=ql
               ).pack(side=LEFT)
    l5 = Label(f5, 
        textvariable=v6,
        #text="累计抽取人数：0",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=LEFT)    # 固定窗口位置
    
    bjian = Button(f5,
               text="-",
               font=('宋体', 12),         # 字体和字体大小
               command=jian
               ).pack(side=RIGHT)
    bjia = Button(f5,
               text="+",
               font=('宋体', 12),         # 字体和字体大小
               command=jia
               ).pack(side=RIGHT)
    lzh = Label(f5, 
        text="字号：",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=RIGHT)    # 固定窗口位置
    
    f5.pack(fill=X)


    f4 = Frame(win)
    
    f41 = Frame(f4)
    bsjdm = Button(f41,
               text="随机\n点名",
               font=('宋体', 20),         # 字体和字体大小
               command=sjdm
               )
    bsjdm.pack()# side=LEFT
    bkszt = Button(f41,# 开始暂停
               text="开始",
               font=('宋体', 20),         # 字体和字体大小
               command=kszt
               )
    bkszt.pack()# side=LEFT
    f41.pack(side=LEFT)
    
    l4 = Label(f4, 
        text="被  \n点→\n人→\n名  ",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 22),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=LEFT)    # 固定窗口位置
    lname = Label(f4, 
        textvariable=v5,
        #text="王小明",    # 标签的文字
        #bg='green',                 # 背景颜色
        #font=ft,
        font=('黑体', 90),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    lname.pack(side=LEFT)    # 固定窗口位置
    f4.pack(fill=X)


    win.pack()
    """

    f = Frame(window)

    t = Text(f,
             width=33,
             height=12
               )
    t.pack()

    f.pack(side=LEFT)
    """
    begin()
    window.protocol("WM_DELETE_WINDOW", save_exit)
    window.mainloop()           #循环消息，让窗口活起来
