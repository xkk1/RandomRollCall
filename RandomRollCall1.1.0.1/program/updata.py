from tkinter import * # 图形界面
from tkinter import messagebox # 对话框
from traceback import format_exc #用于精准的获取错误异常
import urllib.request # 用于网上爬取版本信息
import threading # 多线程
from sys import exit
'''t = threading.Thread(target=new, args=(events.x, events.y))
    # 将子线程设置为守护线程，一旦父线程被结束了，子线程也马上跟着结束。
    t.setDaemon(True) 
    t.start()
'''
# json轻量级的数据交换格式
import json
"""
json.dumps(var): 对数据进行编码。
json.loads(var): 对数据进行解码。
json.dump(data, file): 对文件的数据进行编码。
json.load(file): 对文件的数据进行解码。
JSON   -->   Python
object       dict
array        list
string       str
number(int)  int
number(real) float
true         True
false        False
null         None
"""
'''
{
    'verson': [1, 1, 0, 1],
    'url': '',
    'time': '2020-09-14 12:29:12',
    'update-content': '无'
}
'''


url = 'https://xkk1.github.io/program/randomrollcall/update.json'


def compare_version(old_verson, new_verson):
    '''比较版本号大小
    返回True时有新的版本（有新版）
    返回False时版本一样（已是最新版）
    返回None时本机版本比网上版本要新（测试版）'''
    if new_verson[0] > old_verson[0]:# 如果新的版本号比旧的版本号大
        return True
    elif new_verson[0] < old_verson[0]:# 如果旧的版本号比新的版本号大
        return None
    else:
        if new_verson[1] > old_verson[1]:
            return True
        elif new_verson[1] < old_verson[1]:
            return None
        else:
            if new_verson[2] > old_verson[2]:
                return True
            elif new_verson[2] < old_verson[2]:
                return None
            else:
                if new_verson[3] > old_verson[3]:
                    return True
                elif new_verson[3] < old_verson[3]:
                    return None
                else:
                    return False

def show_updata(old_verson):
    try:
        
        response = urllib.request.urlopen(url)
        
        josndata = response.read().decode("utf-8")
        # print(josndata)
        newdata = json.loads(josndata)
        # print(newdata)
        
        root = Tk()
        root.title("随机点名——更新")
        try:# 尝试打开设置图标
            root.iconbitmap('.\\program\\image\\RandomRollCall.ico')
        except:
            pass
        #print(compare_version(old_verson, newdata['verson']) == False)
        boolversion = compare_version(old_verson, newdata['verson'])
        if boolversion == False:
            l = Label(root, 
                text="已是最新版！",    # 标签的文字
                #bg=data['background'],          # 背景颜色
                #fg="red",
                font=('宋体', 24),         # 字体和字体大小
                #width=15, height=2          # 标签长宽
                )
            l.pack(padx=5,pady=5)    # 固定窗口位置
        elif boolversion == True:
            l = Label(root, 
                text="有新版",    # 标签的文字
                #bg=data['background'],          # 背景颜色
                #fg="red",
                font=('宋体', 24),         # 字体和字体大小
                #width=15, height=2          # 标签长宽
                )
            l.pack(padx=5,pady=5)    # 固定窗口位置
            lm = Label(root, 
                text="当前版本：%s.%s.%s.%s\n更新版本：%s.%s.%s.%s\n更新时间：%s\n文件大小：%s\n更新内容：%s\n下载链接：\
" % (old_verson[0], old_verson[1], old_verson[2], old_verson[3],
newdata['verson'][0], newdata['verson'][1], newdata['verson'][2], newdata['verson'][3],
newdata['time'], newdata['size'], newdata['update-content']),    # 标签的文字
                #bg=data['background'],          # 背景颜色
                #fg="red",
                font=('宋体', 12),         # 字体和字体大小
                #width=15, height=2          # 标签长宽
                justify=LEFT,  # 字符串进行左对齐
                )
            lm.pack(padx=5,pady=5)    # 固定窗口位置
            t = Text(root,
                     #width=40,
                     #height=12
                       )
            t.pack()
            # t.delete(0.0, END)
            t.insert(INSERT,newdata['url'][0])
        else: #boolversion == None
            l = Label(root, 
                text="您在使用测试版，正式版更稳定",    # 标签的文字
                #bg=data['background'],          # 背景颜色
                #fg="red",
                font=('宋体', 14),         # 字体和字体大小
                #width=15, height=2          # 标签长宽
                )
            l.pack(padx=5,pady=5)    # 固定窗口位置
            lm = Label(root, 
                text="当前版本：%s.%s.%s.%s\n更新版本：%s.%s.%s.%s\n更新时间：%s\n文件大小：%s\n更新内容：%s\n下载链接：\
" % (old_verson[0], old_verson[1], old_verson[2], old_verson[3],
newdata['verson'][0], newdata['verson'][1], newdata['verson'][2], newdata['verson'][3],
newdata['time'], newdata['size'], newdata['update-content']),    # 标签的文字
                #bg=data['background'],          # 背景颜色
                #fg="red",
                font=('宋体', 12),         # 字体和字体大小
                #width=15, height=2          # 标签长宽
                justify=LEFT,  # 字符串进行左对齐
                )
            lm.pack(padx=5,pady=5)    # 固定窗口位置
            t = Text(root,
                     #width=33,
                     #height=12
                       )
            t.pack()
            # t.delete(0.0, END)
            t.insert(INSERT,newdata['url'][0])
        b = Button(root,
                   text="确定",
                   font=('宋体', 14),        # 字体和字体大小
                   #bg=data['buttonbg'],
                   command=root.destroy,
                   )
        b.pack(padx=5,pady=5)
        
        root.mainloop()
    except:
        messagebox.showerror(
                        title = '更新模块出错',
                        message='更新模块出错！请联系制作者(QQ(小喾苦):3434623263 Q群(随机点名):681032320)\
\n出错信息：%s\n'% (format_exc() ))
        print(format_exc())

def updata(old_verson):
    '''完成更新功能的函数'''
    # global response
    t = threading.Thread(target=show_updata, args=(old_verson, ))
    # 将子线程设置为守护线程，一旦父线程被结束了，子线程也马上跟着结束。
    # t.setDaemon(True) 
    t.start()


if __name__ == "__main__":
    updata([1, 1, 0, 0])
