import tkinter as tk
import tkinter.scrolledtext
import tkinter.filedialog
import webbrowser
import time
from os import sep
from traceback import format_exc #用于精准的获取错误异常
from .version import bbh # 版本号
from .get_image import icon_file_path # 图标文件路径
from .right_click_menu import SetRightClickMenu # 设置右键菜单


def show_information(information="", title="信息", icon="icon.ico"):
    """显示信息"""
    global information_window
    global information_scrolledtext
    
    def save_txt(information=information, title=title):
        filename = tkinter.filedialog.asksaveasfilename(
            title='请选择你要保存的地方', filetypes=[('TXT', '*.txt'), ('All Files', '*')],
            initialfile='%s' % title,
            # time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            defaultextension = 'txt',  # 默认文件的扩展名
            )  # 返回文件名--另存为
         # title='Select the diagnostic instrument .exe file', filetypes=[('EXE', '*.exe'), ('All Files', '*')],initialdir='C:\\Windows')
        # print(filename)
        # print(filename == '')
        if filename == '':
            return False
        else:
            with open(filename, 'w') as f:
                f.write(information)
                # f.close()
            return True

    try:
        """
        information_window.deiconify()

        information = get_information()
        print(information)
        """
        information_window.deiconify()
        information_window.title(title)
        information_scrolledtext.delete(0.0, tk.END)
        information_scrolledtext.insert(tk.END, information)

    except:
        """
        information = get_information()
        print(information)
        """
        information_window = tk.Tk()
        information_window.title(title)
        try:  # 尝试设置图标
            information_window.iconbitmap(icon)

        except:
            pass

        

        information_scrolledtext = tkinter.scrolledtext.ScrolledText(
            information_window,
            width=70,
            height=30,
            undo=True
            # font=('宋体', 12)
            )  # 滚动文本框（宽，高（这里的高应该是以行数为单位），字体样式）
        # scr.place(x=50, y=50) #滚动文本框在页面的位置
        information_scrolledtext.pack(expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)
 
        information_scrolledtext.insert(tk.INSERT, information)

        """
        '''创建一个弹出菜单'''
        menu = tk.Menu(information_window,
                    tearoff=False,
                    )

        menu.add_command(label="剪切", command=lambda:information_scrolledtext.event_generate('<<Cut>>'))
        menu.add_command(label="复制", command=lambda:information_scrolledtext.event_generate('<<Copy>>'))
        menu.add_command(label="粘贴", command=lambda:information_scrolledtext.event_generate('<<Paste>>'))
        menu.add_command(label="删除", command=lambda:information_scrolledtext.event_generate('<<Clear>>'))
        menu.add_command(label="撤销", command=lambda:information_scrolledtext.event_generate('<<Undo>>'))
        menu.add_command(label="重做", command=lambda:information_scrolledtext.event_generate('<<Redo>>'))
        menu.add_separator()
        menu.add_command(label="打开随机点名官网", command=lambda:webbrowser.open("https://xkk1.github.io/program/randomrollcall/"))
        menu.add_command(label="随机点名官网备用", command=lambda:webbrowser.open("https://xkk2.gitee.io/program/randomrollcall/"))
        menu.add_command(label="作者的个人网站", command=lambda:webbrowser.open("https://xkk1.github.io/"))
        menu.add_command(label="作者的哔哩哔哩", command=lambda:webbrowser.open("https://space.bilibili.com/513689605"))

        def popup(event):
            menu.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单

        information_scrolledtext.bind("<Button-3>", popup)                 # 绑定鼠标右键,执行popup函数
        """
        SetRightClickMenu(information_scrolledtext) # 设置右键菜单
        
        bottom_frame = tk.Frame(information_window)
        bottom_frame.pack()
        
        save_button = tk.Button(
                bottom_frame,
                text="保存为文本文档(*.txt)",
                command=lambda:save_txt(information=information_scrolledtext.get('1.0', tk.END).rstrip()))
        save_button.pack(side=tk.RIGHT, padx=5,pady=5)

        close_button = tk.Button(
                bottom_frame,
                text="关闭",
                command=information_window.destroy)
        close_button.pack(side=tk.RIGHT, padx=5,pady=5)

        def copy_to_clipboard():
            """Copy current contents of text_entry to clipboard."""
            information_window.clipboard_clear()  # Optional.
            information_window.clipboard_append(information_scrolledtext.get('1.0', tk.END).rstrip())
            # root.clipboard_append(newdata['url'][0])
        
        copy_button = tk.Button(
                bottom_frame,
                text="复制内容到剪贴板",
                # font=('宋体', 14),        # 字体和字体大小
                #bg=data['buttonbg'],
                command=copy_to_clipboard,
                )
        copy_button.pack(side=tk.LEFT, padx=5,pady=5)
        
        information_window.mainloop()

def show_help():
    show_information(information=f"""         随机点名V{bbh}帮助信息
QQ群：681032320(随机点名)  QQ:3434623263(小喾苦)
哔哩哔哩：小喾苦   （UID513689605）
官网：https://xkk1.github.io/program/randomrollcall/
备用：https://xkk2.gitee.io/program/randomrollcall/

快速上手：
  1)新建文本文档，写入需随机点名的姓名，一个姓名占一行，保存退出。
  2)进入随机点名，点击左上角的设置，进入设置页面。
  3)点击姓名文件最后的“选择文件”按钮，选择您所保存的姓名文件。
  4)点击设置窗口左下角的保存按钮，回到随机点名主窗口。
  5)现在可以使用随机点名了
      “随机点名”按钮将会随机显示一个姓名
      “开始点名”按钮将开始不断改变地显示已有的名字
      “暂停点名”按钮将暂停“开始点名”

功能：
（1）不重复点名
    每次“随机点名”不会重复点名，并显示当前进度 剩余姓名/总姓名数
    该功能仅在“姓名去重”功能开启下使用
    该功能不能在“开始点名”下使用
（2）记录累计抽取人数
    在程序主窗口左下角显示
    点击清零按钮可清零累计抽取人数
（3）姓名去重
    读取姓名时去除重复的姓名（默认打开）
    设置方法：勾选设置窗口中的“姓名去重”复选框
（3）字号调整
    可调整显示姓名字号大小，字号数字越大，姓名越大（字号最大为500）
    调整方式：
      Ⅰ、程序主页面右下角的“+”“-”按钮
      Ⅱ、程序设置页面的字体大小滑块
（4）颜色调整
    可调整主窗口背景颜色、按钮颜色
    调整方式：设置窗口中的选择颜色按钮
（5）字体调整
    可调整主窗口、设置窗口、更新窗口的部分文字字体
    调整方式：设置窗口中的文字字体下拉菜单
（6）窗口透明度调整
    可调主窗口、设置窗口的透明度，范围0.0~1.0(数越小，透明度越高)
    调整方法：设置窗口中的“主窗口透明度”滑块
（7）窗口置顶
    可使主窗口保持最前
    设置方法：勾选设置窗口的“主窗口置于顶层”的复选框
（8）检查更新
    可检查是否有可用的更新

有问题，找作者
 联系方式：
  邮箱：3434623263@qq.com
  QQ：3434623263
  哔哩哔哩(www.bilibili.com)：
    用户名：小喾苦
    UID：513689605
    空间：https://space.bilibili.com/513689605
  个人网站：
    Github Pages：https://xkk1.github.io/
    Gitee Pages：https://xkk2.gitee.io/

更新日志：
    1、修复读取姓名文件时读取失败的问题
    2、加入文件编码自动识别、选择功能
    3、增加姓名去重功能
    4、增加字体选择功能
    5、增加预览功能
    6、将字体大小最大值改为500
    7、优化了信息显示窗口
    8、优化了检查更新功能
    9、增加右键复制、粘贴等功能
    10、优化了程序报错功能

""",title=f"随机点名V{bbh}帮助信息", icon=icon_file_path)
  
'''# old
def show_help():
    #showinto （信息提示）
    # 弹出对话框
    messagebox.showinfo(
        title = '随机点名——帮助',
        message="""有事加QQ群：681032320(随机点名)  QQ:3434623263(小喾苦)
官网：https://xkk1.github.io/program/randomrollcall/
使用方法：
1、新建一个文本文档(*.txt)，输入姓名，一个人名占一行
(请确保文件编码为“GB2312”)
2、点击主页面左上角设置，点击选择文件
3、找到并选择新建的文件，点击保存
4、点击“随机点名”即可使用
其他：
勾选“不重复点名”后同一个人只会抽到一次
(windows系统可使用Alt + Tab切换窗口)
更新日志：
优化主页面显示 优化更新页面显示""")
    # 返回值为：ok
'''

def show_error():
    info = f"""很抱歉，随机点名程序出BUG了，请您把这个错误信息导出发给我，我会把它变得更好
联系方式：
  邮箱：3434623263@qq.com  
  QQ：3434623263 
  哔哩哔哩：小喾苦 (UID：513689605)

程序：随机点名(RandomRollCall)
版本：{bbh}
制作者：小喾苦
联系方式：
  邮箱：3434623263@qq.com
  QQ：3434623263
  哔哩哔哩(www.bilibili.com)：
    用户名：小喾苦
    UID：513689605
    空间：https://space.bilibili.com/513689605
  个人网站：
    Github Pages：https://xkk1.github.io/
    Gitee Pages：https://xkk2.gitee.io/
时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
错误信息：
{format_exc()}"""
    show_information(information=info ,title=f"随机点名{bbh}错误信息{time.strftime('%Y-%m-%d', time.localtime())}")

def show_encoding_help():
    info = """什么是文件编码，我该如何选择
【如果您搞不懂文件编码，请选“自动”】
编码是信息从一种形式或格式转换为另一种形式的过程。解码，是编码的逆过程。
保存在计算机里的文本文档就先经过一种特殊的编码方式转变为2进制以方便保存。
程序需要读取文本文档内容时需进行解码。
具体可看百度百科编码：https://baike.baidu.com/item/%E7%BC%96%E7%A0%81/80092?fr=aladdin
该程序支持的编码有ANSI、UTF-8、UTF-8-SIG（带有 BOM 的 UTF-8，win7的 UTF-8 就是它）、UTF-16、UTF-16 LE、UTF-16 BE、GB18030、GB2312、BIG5等
win10、win7用户建议使用ANSI编码的姓名文件，具体操作方法如下：
    记事本打开姓名文件，点击菜单栏上的“文件(F)”、\
点击“另存为(A)”，编码选择“ANSI”后点“保存(S)”\n，确认替换“是(Y)”，回到随机点名，在设置里的\
姓名文件编码选择“自动”或“ANSI”就可以了（^_^）
保存时出现错误“用‘***’编码解码文件‘***’失败！”时代表您的姓名文件编码选错了！如果您不知道应该选什么，请选自动！如果问题依旧无法解决，请按照上述操作该姓名文件编码。

"""
    show_information(information=info, title="什么是文件编码，我该如何选择", icon=icon_file_path)

def main():
    show_information(information="我是用来显示信息的！", title="信息", icon=f".{sep}image{sep}RandomRollCall.ico")

if __name__ == "__main__":
    main()
