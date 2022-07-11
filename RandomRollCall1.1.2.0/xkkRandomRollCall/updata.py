from tkinter import * # 图形界面
from tkinter import messagebox # 对话框
import tkinter.filedialog
import tkinter.scrolledtext
from traceback import format_exc #用于精准的获取错误异常
import urllib.request # 用于网上爬取版本信息
import threading # 多线程
import webbrowser
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
from .get_image import icon_file_path # 图标
from .right_click_menu import SetRightClickMenu # 设置右键菜单


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

def save_txt(information="信息", title="文件名"):
    filename = tkinter.filedialog.asksaveasfilename(
        title='请选择你要保存的地方', filetypes=[('TXT', '*.txt'), ('All Files', '*')],
        initialfile='%s' % title,
        # time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        defaultextension = 'txt',  # 默认文件的扩展名
        )  # 返回文件名--另存为
     # title='Select the diagnostic instrument .exe file', filetypes=[('EXE', '*.exe'), ('All Files', '*')],initialdir='C:\\Windows')
    print(filename)
    #print(filename == '')
    if filename == '':
        return False
    else:
        with open(filename, 'w') as f:
            f.write(information)
            # f.close()
        return True

def show_updata(old_verson, font):
    try:
        
        response = urllib.request.urlopen(url)
        
        josndata = response.read().decode("utf-8")
        # print(josndata)
        newdata = json.loads(josndata)
        # print(newdata)
        
        root = Tk()
        root.title("随机点名——更新")
        try:# 尝试打开设置图标
            root.iconbitmap(icon_file_path)
        except:
            pass
        #print(compare_version(old_verson, newdata['verson']) == False)
        boolversion = compare_version(old_verson, newdata['verson'])
        if boolversion == False:
            l = Label(root, 
                text="已是最新版！",    # 标签的文字
                #bg=data['background'],          # 背景颜色
                fg="green",
                font=(font, 24),         # 字体和字体大小
                #width=15, height=2          # 标签长宽
                )
            l.pack(padx=5,pady=5)    # 固定窗口位置
            lm = Label(root, 
                text="当前、最新版本：%s.%s.%s.%s\n更新时间：%s\n文件大小：%s\n更新内容：%s\n下载链接：\
" % (newdata['verson'][0], newdata['verson'][1], newdata['verson'][2], newdata['verson'][3],
newdata['time'], newdata['size'], newdata['update-content']),    # 标签的文字
                #bg=data['background'],          # 背景颜色
                #fg="red",
                font=(font, 12),         # 字体和字体大小
                #width=15, height=2          # 标签长宽
                justify=LEFT,  # 字符串进行左对齐
                )
            lm.pack(fill=X,padx=5,pady=5)    # 固定窗口位置
        elif boolversion == True:
            l = Label(root, 
                text="有新版",    # 标签的文字
                #bg=data['background'],          # 背景颜色
                fg="red",
                font=(font, 24),         # 字体和字体大小
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
                font=(font, 12),         # 字体和字体大小
                #width=15, height=2          # 标签长宽
                justify=LEFT,  # 字符串进行左对齐
                )
            lm.pack(fill=X,padx=5,pady=5)    # 固定窗口位置
        else: #boolversion == None
            l = Label(root, 
                text="您在使用测试版，正式版更稳定",    # 标签的文字
                #bg=data['background'],          # 背景颜色
                fg="orange",
                font=(font, 24),         # 字体和字体大小
                #width=15, height=2          # 标签长宽
                )
            l.pack(padx=5,pady=5)    # 固定窗口位置
            lm = Label(root, 
                text="当前版本：%s.%s.%s.%s\n更新版本：%s.%s.%s.%s\n更新时间：%s\n文件大小：%s\n更新内容：%s\n下载链接：\
" % (old_verson[0], old_verson[1], old_verson[2], old_verson[3],
newdata['verson'][0], newdata['verson'][1], newdata['verson'][2], newdata['verson'][3],
newdata['time'], newdata['size'], newdata['update-content']),    # 标签的文字
                # bg='Green',          # 背景颜色
                # fg="red",
                font=(font, 12),         # 字体和字体大小
                #width=15, height=2          # 标签长宽
                justify=LEFT,  # 字符串进行左对齐
                )
            lm.pack(fill=X,padx=5,pady=5)    # 固定窗口位置
        t = tkinter.scrolledtext.ScrolledText(root,undo=True
                #width=33,
                #height=12
                )
        t.pack(expand=YES, fill=BOTH)
        # t.delete(0.0, END)
        t.insert(INSERT,newdata['url'][0])
        """
        '''创建一个弹出菜单'''
        menu = Menu(root,
                    tearoff=False,
                    )

        menu.add_command(label="剪切", command=lambda:t.event_generate('<<Cut>>'))
        menu.add_command(label="复制", command=lambda:t.event_generate('<<Copy>>'))
        menu.add_command(label="粘贴", command=lambda:t.event_generate('<<Paste>>'))
        menu.add_command(label="删除", command=lambda:t.event_generate('<<Clear>>'))
        menu.add_command(label="撤销", command=lambda:t.event_generate('<<Undo>>'))
        menu.add_command(label="重做", command=lambda:t.event_generate('<<Redo>>'))
        menu.add_separator()
        menu.add_command(label="打开随机点名官网", command=lambda:webbrowser.open("https://xkk1.github.io/program/randomrollcall/"))
        menu.add_command(label="随机点名官网备用", command=lambda:webbrowser.open("https://xkk2.gitee.io/program/randomrollcall/"))
        menu.add_command(label="作者的个人网站", command=lambda:webbrowser.open("https://xkk1.github.io/"))
        menu.add_command(label="作者的哔哩哔哩", command=lambda:webbrowser.open("https://space.bilibili.com/513689605"))

        def popup(event):
            menu.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单

        t.bind("<Button-3>", popup)                 # 绑定鼠标右键,执行popup函数
        """
        SetRightClickMenu(t)
        
        def copy_to_clipboard():
            """Copy current contents of text_entry to clipboard."""
            root.clipboard_clear()  # Optional.
            # root.clipboard_append(t.get('1.0', END).rstrip())
            root.clipboard_append(newdata['url'][0])
        f= Frame(root)
        f.pack()

        b_copy = Button(f,
                   text="复制内容到剪贴板",
                   font=(font, 14),        # 字体和字体大小
                   #bg=data['buttonbg'],
                   command=copy_to_clipboard,
                   )
        b_copy.pack(side=LEFT, padx=5,pady=5)

        b_close = Button(f,
                   text="关闭",
                   font=(font, 14),        # 字体和字体大小
                   #bg=data['buttonbg'],
                   command=root.destroy,
                   )
        b_close.pack(side=LEFT, padx=5,pady=5)

        b_save = Button(f,
                   text="保存为文本文档(*.txt)",
                   font=(font, 14),        # 字体和字体大小
                   #bg=data['buttonbg'],
                   command=lambda: save_txt(information=newdata['url'][0], title="随机点名最新版本下载地址"),
                   )
        b_save.pack(side=LEFT, padx=5,pady=5)
        
        root.mainloop()
    except:
        messagebox.showerror(
                        title = '更新模块出错',
                        message='更新模块出错！请联系制作者(QQ(小喾苦):3434623263 Q群(随机点名):681032320)\
\n出错信息：%s\n'% (format_exc() ))
        print(format_exc())

def updata(old_verson, font):
    '''完成更新功能的函数'''
    # global response
    t = threading.Thread(target=show_updata, args=(old_verson, font))
    # 将子线程设置为守护线程，一旦父线程被结束了，子线程也马上跟着结束。
    t.setDaemon(True) 
    t.start()


if __name__ == "__main__":
    updata([1, 1, 0, 3])
