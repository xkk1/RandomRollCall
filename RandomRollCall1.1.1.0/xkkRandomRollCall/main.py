from tkinter import * # 图形界面
from tkinter import messagebox # 对话框
from tkinter import filedialog #文件操作
from sys import exc_info # 用于抛出异常
from traceback import format_exc #用于精准的获取错误异常
from os.path import exists # 文件、路径是否存在
from random import sample # 从列表里随机抽取
from random import randint # 生成随机数字
from random import shuffle # 打乱列表
from tkinter import colorchooser # 用于选择颜色
from tkinter import ttk  # 导入ttk模块，因为下拉菜单控件、分割线在ttk中
from tkinter import font # 字体
from os import sep # 输出操作系统特定的路径分隔符
from sys import exit # 退出
import sys # 系统
import time # 时间
import threading # 多线程

if __name__ == "__main__":
    print("我是随机点名的主要代码文件，大部分功能在这实现\n运行随机点名请运行上一目录中的RandomRollCall.pyw（无控制台窗口）或RandomRollCall.py")
    input("按回车键退出. . .")
    exit()

from .version import * # 版本号
from .jsondata import save_data # 用于保存数据
from .jsondata import read_data # 用于读取数据
from .jsondata import change_data # 用于改变数据
from .updata import updata # 用于文件更新
from .get_coding import file_coding # 用于判断文件编码
from .show_information import show_information # 显示信息
from .show_information import show_help # 显示帮助
from .show_information import show_error # 显示错误
from .show_information import show_encoding_help # “什么是文件编码”
from .get_image import icon_file_path # 随机点名图标路径
from .right_click_menu import SetRightClickMenu # 设置右键菜单


"""
try:
    from .jsondata import * # 用于保存数据
    from .updata import * # 用于文件更新
except:
    from jsondata import * # 用于保存数据
    from updata import * # 用于文件更新
# updata([0,0,0,0])
"""

file = 'names.txt'
names = [] # 读取的姓名
# name = "" # 当前抽取的姓名
background = "#f0f0f0" # 背景色
buttonbg = "#f0f0f0" # 按钮背景色
havenames = []
# lj = 0
# data = "data.txt"
# zh = 90
animation = False # 动画
# donghua = False
# 字体初始化
fonts = ["默认字体"]
# json数据文件名称/地址
json_data_file = 'data.json'
# 初始化数据
data = {
    'cumulative': 0, # 累计人数
    'font': fonts[0],
    'font_size': 100, # 字号
    'file': 'names.txt', # 姓名文件
    'background': "#f0f0f0", # 背景色
    'buttonbg': "#f0f0f0", # 按钮背景色
    '-alpha': 1.0, # 透明度
    '-topmost': False, # 是否置于顶层
    'encoding': "自动", # 文件默认编码
    'unrepeat': True, # 是否姓名去重
    'program_name': 'RandomRollCall', #程序名
    'program_path': sys.argv[0], # 程序路径
    'verson': version, # 版本号
    'author': '小喾苦', # 制作人
    'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), # 时间
    # 'check_code': '', # 校验码
}
data_default = data.copy() # 数据默认值


def choice():
    '''选择姓名文件'''
    global file
    # global names
    '''
    f =filedialog.askopenfile()#返回文件流对象--打开
    if f != None:
        file = f.name # 获取文件名
        names = list(set(f.readlines()))# 读文件 list(set())为查重
        print(file, n)
    '''
    filename = filedialog.askopenfilename(
        title = '打开--请选择包含姓名的TXT文件',
        filetypes=[('TXT', '*.txt'), 
        ('All Files', '*')],
        #initialdir='C:\\Windows'),
        )#返回文件名--打开
    if filename != '':
        file = filename
        vname_file.set(file)
        # print(file)

def save_changes():
    global names
    b = True
    info = """保存设置时出错！\n请您检查您输入的是否合规！姓名文件是否存在！
若您无法解决此问题，您可以复制此信息联系制作者
制作者联系方式：
    QQ：3434623263(人，小喾苦) 681032320(群，随机点名)
    哔哩哔哩：小喾苦  （UID513689605）

以下是可能出错的原因：
"""
    errorinfo = "\n\n详细报错如下：\n"
    global data
    global f21
    global f31
    global havenames
    global encoding_combobox
    try:
        name_file = vname_file.get()
        encoding = encoding_combobox.get()
        if not exists(name_file):
            b = False
            string = '未找到姓名文件,指定的姓名文件“%s”不存在！\n' % name_file
            info += string
            errorinfo += string+"报错：\n程序找不到姓名文件！\n"
        else:
            if encoding == "自动":
                encoding = file_coding(name_file)
            f = open(name_file, 'r', encoding=encoding)
            names = f.readlines()
            f.close()
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
            if var_unrepeat_Checkbutton.get(): # 姓名去重
                names = list(set(names)) # 实现姓名去重功能(会自动排序)
            shuffle(names) # 打乱姓名列表
            # print(names)
            
            data['file'] = name_file
            
            # print(names)
            # for j in names:
            #     print(j)
    except UnicodeDecodeError:
        b = False
        string = (f'用“{encoding_combobox.get()}”编码解码文件“{vname_file.get()}”失败！\n'
                   "您可以换几个文件编码试试，推荐“自动”、“UTF-8”、“UTF-8-SIG”、“GB18030”\n"
                   "win10、win7操作系统的用户可以用记事本打开姓名文件，点击菜单栏上的“文件(F)”、\
点击“另存为(A)”，编码选择“ANSI”后点“保存(S)”\n，确认替换“是(Y)”，回到随机点名，在设置里的\
姓名文件编码选择“自动”或“ANSI”就可以了（^_^）")
        info += string
        errorinfo += string + "报错：\n" + format_exc() +"\n"
    except LookupError:
        b = False
        string = (f'不支持用“{encoding_combobox.get()}”编码解码文件“{vname_file.get()}”失败！\n'
                   "可能是编码拼写错误，请检查编码拼写\n"
                   "win10、win7操作系统的用户可以用记事本打开姓名文件，点击菜单栏上的“文件(F)”、\
点击“另存为(A)”，编码选择“ANSI”后点“保存(S)”\n，确认替换“是(Y)”，回到随机点名，在设置里的\
姓名文件编码选择“自动”或“ANSI”就可以了（^_^）")
        info += string
        errorinfo += string + "报错：\n" + format_exc() +"\n"
    except:
        b = False
        string = '读取文件“%s”失败！\n' % vname_file.get() # , format_exc())
        info += string
        errorinfo += string + "报错：\n" + format_exc() +"\n"
    try:
        f21['bg'] = vbackground.get()
        data['background'] = vbackground.get()
    except:
        b = False
        string = '无效的背景颜色“%s”!\n' % vbackground.get()
        info += string
        errorinfo += string + "报错：\n" + format_exc() +"\n"
    try:
        f31['bg'] = vbuttonbg.get()
        data['buttonbg'] = vbuttonbg.get()
    except:
        b = False
        string = '无效的按钮颜色“%s”!\n' % vbuttonbg.get()
        info += string
        errorinfo += string + "报错：\n" + format_exc() +"\n"
    
    if b:
        data['background'] = vbackground.get()
        data['buttonbg'] = vbuttonbg.get()
        data['font_size'] = int(var_font_size_Scale.get())
        data['-alpha'] = float(var__alpha_Scale.get())
        data['-topmost'] = var__topmost_Checkbutton.get()
        data['unrepeat'] = var_unrepeat_Checkbutton.get()
        data['encoding'] = encoding_combobox.get()
        data['font'] = font_combobox.get()
        havenames = []
        # 保存数据
        save_data(data, json_data_file)
        wset_up.destroy()# 销毁设置窗口
    else:
        # messagebox.showerror(title='数据错误！',message=string)
        show_information(information=info+errorinfo, title="保存设置时出错！", icon=icon_file_path)

def restore_default():
    '''恢复默认'''
    # global data
    global file
    global background
    global buttonbg
    global f21
    global f31
    
    # data = data_default
    file = data_default['file']
    background = data_default['background']
    buttonbg = data_default['buttonbg']
    
    f21['bg'] = data_default['background']
    f31['bg'] = data_default['buttonbg']
    
    vname_file.set(data_default['file'])
    vbackground.set(data_default['background'])
    vbuttonbg.set(data_default['buttonbg'])
    var_font_size_Scale.set(data_default['font_size'])
    var__alpha_Scale.set(str(data_default['-alpha']))
    var__topmost_Checkbutton.set(data_default['-topmost'])
    var_unrepeat_Checkbutton.set(data_default['unrepeat'])
    encoding_combobox.set(data_default['encoding'])
    font_combobox.set(data_default['font'])
    wset_up.wm_attributes("-alpha", data_default['-alpha'])
    preview_name_Label["font"]= (data_default['font'], data_default['font_size'])
    preview_Button["font"]= (data_default['font'], 20)

def first_read():
    '第一次（启动时）读姓名'
    global names
    try:
        name_file = data['file']
        if not exists(name_file):
            pass
        else:
            if data['encoding'] == "自动":
                encoding = file_coding(name_file)
            else:
                encoding = data['encoding']
            f = open(name_file, 'r',encoding=encoding)
            names = f.readlines()
            f.close()
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
            if data['unrepeat']: # 姓名去重
                names = list(set(names)) # 实现姓名去重功能(会自动排序)
            shuffle(names) # 打乱姓名列表
            
            data['file'] = name_file
            
            # print(names)
            # for j in names:
            #     print(j)
    except:
        pass
    
    if names == []: # 如果没有读到任何姓名
        # names = ['孙八', '张三', '吴十', '刘一', '李四', '杨九', '陈二', '赵六', '钱七', '王五']
        # print('暂无姓名！')
        pass

def change_background_color(color):
    '及时改变背景颜色'
    # print('change_background_color')
    global f21
    global preview_name_Label
    global preview_LabelFrame
    try:
        f21['bg'] = color
        preview_name_Label['bg'] = color
        preview_LabelFrame['bg'] = color
    except:
        pass
    return True

def change_buttonbg_color(color):
    '及时改变按钮颜色'
    global f31
    global preview_Button
    try:
        f31['bg'] = color
        preview_Button['bg'] = color
    except:
        pass
    return True

def colorchooser_change_background_color():
    color = colorchooser.askcolor(data['background'])
    #print(color[1])
    if color[1] != None:
        vbackground.set(color[1])

def colorchooser_change_buttonbg_color():
    color = colorchooser.askcolor(data['buttonbg'])
    #print(color[1])
    if color[1] != None:
        vbuttonbg.set(color[1])

def no_repeat_roll_call():
    # global remaining_names_Lable
    if var_no_repeat_roll_call.get():
        reset_Button.pack(side=LEFT)
        remaining_names_Lable.pack(side=LEFT)
    else:
        reset_Button.pack_forget()
        remaining_names_Lable.pack_forget()

def increase_font_size():
    '增加字号'
    global data
    
    if data['font_size'] <= 495:
        lname['font'] = ('黑体', data['font_size']+5)
        data['font_size'] += 5
    # print(data['font_size']) 1-335

def reduce_font_size():
    '减少字号'
    global data
    
    if data['font_size'] > 5:
        lname['font'] = ('黑体', data['font_size']-5)
        data['font_size'] -= 5

def reset():# 复位
    global havenames
    remaining_names_Lable['text'] = "剩余姓名："+str(len(names))+'/'+ str(len(names))
    havenames = []

def extract_animation():
    '抽取动画'
    random_roll_call_Button['state'] = DISABLED   # 禁用
    start_pause_Button['state'] = DISABLED   # 禁用
    # print("抽取动画开始")
    if len(names) > 7:
        randomnames = sample(names, 7) # 随机抽取7个名字
    else:
        randomnames = names
    for i in range(len(randomnames)):
        lname['text'] = randomnames[i]
        time.sleep((i + 1) / 35)
    # print('抽取动画结束')
    
    global data
    if not var_no_repeat_roll_call.get(): # 判断是否选中不重复点名
        name = sample(names, 1)[0] # 随机抽取1个名字
    else: # 如果选中不重复点名
        # print('选中不重复点名')
        global havenames
        randomhavenames = names.copy()
        for havename in havenames:
            randomhavenames.remove(havename)
        name = sample(randomhavenames, 1)[0] # 随机抽取1个名字
        havenames.append(name)
        if len(havenames) == len(names):
            # print('full')
            havenames = []
        else:
            pass
        remaining_names_Lable['text'] = '剩余姓名：'+str(len(names)-len(havenames))+'/'+ str(len(names))
        print(havenames)
    
    lname['text'] = name
    data['cumulative'] += 1
    cumulative_Label['text'] = '累计抽取人数：' + str(data['cumulative'])
    
    random_roll_call_Button['state'] = NORMAL     # 重新激活
    start_pause_Button['state'] = NORMAL     # 重新激活
    
    exit() # 退出线程

def random_roll_call():
    '随机点名'
    # global data
    # global havenames
    # global animation
    if len(names) == 0:
        messagebox.showerror(title = '没有指定姓名文件',
            message='没有指定姓名文件！\n或姓名文件被删除！\
\n或姓名文件为空\n请先指明姓名文件！')
    else:
        # 开始抽取线程
        threading.Thread(target=extract_animation).start() # , args=(old_verson, ))

def clearing():
    '累计清零'
    global data
    data['cumulative'] = 0
    cumulative_Label['text'] = '累计抽取人数：0'

def roll_call_begins():
    '开始滚动随机点名'
    # print('开始了')
    global data
    # cumulative
    zz = len(names)-1
    sj = randint(0,len(names)-1)
    # print(names[sj])
    for i in range(sj ,len(names)-1):
        if animation:
            lname['text'] = names[i]
            time.sleep(0.02)
        else:
            break
    while animation:# 循环显示名字
        if zz == -1:
            zz = len(names)-1
        lname['text'] = names[zz]
        zz -= 1
        time.sleep(0.02)

def start_pause():
    '控制动画（滚动点名）的开始暂停'
    global animation
    global data
    
    if len(names) == 0:
        messagebox.showerror(title = '没有指定姓名文件',
                            message='没有指定姓名文件！\n或姓名文件被删除！\n请先指明姓名文件！')
    else:
        if animation:
            random_roll_call_Button['state'] = NORMAL # 重新激活
            animation = False
            start_pause_Button['text'] = '开始点名'
            
            data['cumulative'] += 1
            cumulative_Label['text'] = '累计抽取人数：' + str(data['cumulative'])
        else:
            animation = True
            random_roll_call_Button['state'] = DISABLED # 禁用
            start_pause_Button['text'] = '暂停点名'
            # 开始滚动点名
            threading.Thread(target=roll_call_begins).start() # , args=(old_verson, ))

"""
def view_colors():
    window_view_colors = Tk()
    window_view_colors.title("随机点名——部分颜色代码")
    try:# 尝试打开设置图标
        window_view_colors.iconbitmap(icon_file_path)
    except:
        pass
    i = 0
    colcut = 5
    for color in colors.split('\n'):
        sp = color.split(' ')
        try:
            Label(window_view_colors,text=color, bg=sp[1]).grid(row=int(i/colcut),column=i%colcut, sticky=W+E+N+S)
        except :
            print('err',color)
            Label(window_view_colors,text='ERR'+color).grid(row=int(i/colcut),column=i%colcut, sticky=W+E+N+S)
        i += 1
    window_view_colors.mainloop()
"""

def set_up():
    '''显示设置窗口'''
    global window
    global wset_up
    # global data
    global file
    global background
    global buttonbg
    global f21# 方便保存时更改背景色
    global f31# 方便保存时更改背景色（用来测试）
    global animation
    
    animation = False
    
    file = data['file']
    background = data['background']
    window.destroy()# 销毁主窗口
    
    wset_up=Tk()# 设置窗口
    wset_up.title("随机点名——设置")
    wset_up.resizable(0,0)# 禁止调节窗口大小
    try:# 尝试打开设置图标
        wset_up.iconbitmap(icon_file_path)
    except:
        pass
    
    global vname_file
    global vbackground
    global vbuttonbg
    
    vname_file = StringVar()
    vbackground = StringVar()
    vbuttonbg = StringVar()
    
    vname_file.set(file)
    vbackground.set(data['background'])
    vbuttonbg.set(data['buttonbg'])
    
    global preview_LabelFrame
    preview_LabelFrame = LabelFrame(wset_up, text='预览', padx=5, pady=5, bg = data['background'])
    preview_LabelFrame.pack(side=RIGHT)

    global preview_name_Label
    preview_name_Label = Label(preview_LabelFrame,
                               text="姓名",
                               bg = data['background'],# 背景色
                               font=(data['font'], data['font_size']),         # 字体和字体大小
                               )
    preview_name_Label.pack(padx=5, pady=5)

    global preview_Button
    preview_Button = Button(preview_LabelFrame,
                            text="按钮",
                            bg = data['buttonbg'],# 按钮背景色
                            font=(data['font'], 20),         # 字体和字体大小
                            )
    preview_Button.pack(padx=20, pady=20)

    separator = ttk.Separator(wset_up, orient=VERTICAL) # HORIZONTAL为横分割线
    separator.pack(side=RIGHT, padx=5, pady=5, fill=Y)

    
    win = Frame(wset_up,
                #bg = data['background'],# 背景色
                )
    win.pack(side=LEFT)
    
    f1 = Frame(win,
               #bg = data['background'],# 背景色
               )
    f1.pack(fill=X,padx=5,pady=5)
    
    l1 = Label(f1, 
        text="姓名文件：",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l1.pack(side=LEFT)    # 固定窗口位置
    ename_file = Entry(f1,# 姓名文件名输入框
               textvariable=vname_file,
               #bg=data['background'],          # 背景颜色
               width=30,# 宽度
               )
    ename_file.pack(side=LEFT)
    SetRightClickMenu(ename_file, undo=False)
    bchoice = Button(f1,
               text="选择\n文件",
               #bg = data['buttonbg'],# 按钮背景色
               font=(data['font'], 10),         # 字体和字体大小
               command=choice,
               #width=25, height=25          # 标签长宽
               )
    bchoice.pack(side=RIGHT)
    
    
    """
# 设置状态为只读
self.Combo3.configure(state="readonly")
# 设置状态为禁用
#self.Combo3.configure(state="disabled")
    obj['state'] = DISABLED   ###禁用
    obj['state'] = NORMAL     ###重新激活
    """
    f11 = Frame(win,
               #bg = data['background'],# 背景色
               )
    f11.pack(fill=X,padx=5,pady=5)
    
    l11 = Label(f11, 
        text="姓名文件编码：",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l11.pack(side=LEFT)    # 固定窗口位置

    global encoding_combobox
    encoding_combobox = ttk.Combobox(f11, width=20)
    encoding_combobox['value'] = ["自动", "ANSI","UTF-8", "UTF-8-SIG",
                                  "UTF-16", "UTF-16 LE", "UTF-16 BE",
                                  "GB18030", "GB2312", "BIG5"]
    encoding_combobox.set(data["encoding"])
    encoding_combobox.pack(side=LEFT)    # 固定窗口位置
    SetRightClickMenu(encoding_combobox, undo=False)
    # encoding_combobox.configure(state="readonly")

    b_encoding_help = Button(f11,
               text="什么是\n文件编码",
               #bg = data['buttonbg'],# 按钮背景色
               font=(data['font'], 10),         # 字体和字体大小
               command=show_encoding_help,
               #width=25, height=25          # 标签长宽
               )
    b_encoding_help.pack(side=RIGHT)
    
    
    f2 = Frame(win,
               #bg = data['background'],# 背景色
               )
    f2.pack(fill=X,padx=5,pady=5)
    
    l2 = Label(f2, 
        text="背景颜色：",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        #fg="red",
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l2.pack(side=LEFT)    # 固定窗口位置
    # l2['state'] = DISABLED   ###禁用
    
    change_background_color_CMD = wset_up.register(change_background_color) # 包装起来
    ebackground = Entry(f2,
               textvariable=vbackground,#可变本文
               #bg=data['background'],          # 背景颜色
               width=10,# 宽度
               validate='key', # 启用验证，当输入框被编辑时验证
               validatecommand=(change_background_color_CMD, '%P'),
               )
    ebackground.pack(side=LEFT)
    # ebackground['state'] = DISABLED   ###禁用
    SetRightClickMenu(ebackground, undo=False)
    f21 = Frame(f2,
               bg = data['background'],# 背景色
               width=135,
               height=25,
               )
    f21.pack(side=LEFT)
    
    colorchooser_background_color_Button = Button(f2,
        text="选择",
        command = colorchooser_change_background_color,
        font=(data['font'], 12),         # 字体和字体大小
        )
    colorchooser_background_color_Button.pack(side=LEFT)
    
    f3 = Frame(win,
               #bg = data['background'],# 背景色
               )
    f3.pack(fill=X,padx=5,pady=5)
    buttonbg_color_Label = Label(f3, 
        text="按钮颜色：",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        #fg="red",
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    buttonbg_color_Label.pack(side=LEFT)    # 固定窗口位置
    # l3['state'] = DISABLED   ###禁用
    
    change_buttonbg_color_CMD = wset_up.register(change_buttonbg_color) # 包装起来
    ebuttonbg = Entry(f3,
               textvariable=vbuttonbg,#可变本文
               #bg=data['background'],          # 背景颜色
               width=10,# 宽度
               validate='key', # 启用验证，当输入框被编辑时验证
               validatecommand=(change_buttonbg_color_CMD, '%P'),
               )
    ebuttonbg.pack(side=LEFT)
    # ebuttonbg['state'] = DISABLED   ###禁用
    SetRightClickMenu(ebuttonbg, undo=False)
    f31 = Frame(f3,
               bg = data['buttonbg'],# 背景色
               width=135,
               height=25,
               )
    f31.pack(side=LEFT)
    
    colorchooser_buttonbg_color_Button = Button(f3,
        text="选择",
        command = colorchooser_change_buttonbg_color,
        font=(data['font'], 12),         # 字体和字体大小
        )
    colorchooser_buttonbg_color_Button.pack(side=LEFT)
    
    f4 = Frame(win,
               #bg = data['background'],# 背景色
               )
    f4.pack(fill=X,padx=5,pady=5)
    global var__topmost_Checkbutton
    var__topmost_Checkbutton = BooleanVar()
    var__topmost_Checkbutton.set(data['-topmost'])
    _topmost_Checkbutton = Checkbutton(f4, 
                     #bg = data['background'],# 背景色
                     text='主窗口置于顶层', 
                     variable=var__topmost_Checkbutton, 
                     onvalue=True, 
                     offvalue=False,
                     font=(data['font'], 12),         # 字体和字体大小
                     #command=no_repeat_roll_call,
                     )
    _topmost_Checkbutton.pack(side=LEFT)
    """
    view_colors_Button = Button(f4,
               # text="确定",
               text="查看部分颜色代码",
               font=(data['font'], 12),        # 字体和字体大小
               #bg=data['buttonbg'],
               command=view_colors,
               )
    view_colors_Button.pack(padx=0,pady=0,side=RIGHT) # fill=X,
    """
    global var_unrepeat_Checkbutton
    var_unrepeat_Checkbutton = BooleanVar()
    var_unrepeat_Checkbutton.set(data['unrepeat'])
    unrepeat_Checkbutton = Checkbutton(f4, 
                     #bg = data['background'],# 背景色
                     text='姓名去重', 
                     variable=var_unrepeat_Checkbutton, 
                     onvalue=True, 
                     offvalue=False,
                     font=(data['font'], 12),         # 字体和字体大小
                     #command=no_repeat_roll_call,
                     )
    unrepeat_Checkbutton.pack(side=RIGHT)

    font_Frame = Frame(win,
               #bg = data['background'],# 背景色
               )
    font_Frame.pack(fill=X,padx=5,pady=5)
    font_label = Label(font_Frame, 
        text="字体：",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        #fg="red",
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    font_label.pack(side=LEFT)    # 固定窗口位置
    global font_combobox
    font_combobox = ttk.Combobox(font_Frame, width=20)
    font_combobox['value'] = fonts
    font_combobox.set(data["font"])
    font_combobox.pack(side=LEFT)    # 固定窗口位置
    font_combobox.configure(state="readonly")
    # combobox.bind("<<ComboboxSelected>>",lambda event:set_information(get_information(combobox.get()))) #绑定事件,(下拉列表框被选中时，绑定go()函数)
    # global font_example_label
    font_example_label = Label(font_Frame, 
        text="字体示例",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        #fg="red",
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    font_example_label.pack(side=RIGHT)    # 固定窗口位置
    def change_example_font(event):
        font_example_label["font"] = (font_combobox.get(), 12)
        preview_name_Label["font"] = (font_combobox.get(), int(var_font_size_Scale.get()))
        preview_Button["font"] = (font_combobox.get(), 20)
    font_combobox.bind("<<ComboboxSelected>>", change_example_font)
    
    font_size_Frame = Frame(win) # 字体大小
    font_size_Frame.pack()
    font_size_Label = Label(font_size_Frame, 
        text="字体\n大小",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        #fg="red",
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    font_size_Label.pack(side=LEFT)    # 固定窗口位置
    global var_font_size_Scale
    var_font_size_Scale = StringVar()
    def f_example_font_size(now_font_size):
        preview_name_Label['font'] = (font_combobox.get(), now_font_size)
    font_size_Scale = Scale(font_size_Frame,# 滑块
        from_ = 1,#设置最小值
        to = 500,#设置最大值
        orient = HORIZONTAL,#设置横向
        resolution=1,#设置步长
        tickinterval = 100,#设置刻度
        length = 300,# 设置像素
        variable = var_font_size_Scale,#绑定变量
        command = f_example_font_size, # print(now_font_size), # 改变时调用的函数
        )
    font_size_Scale.pack(side=LEFT)    # 固定滑块位置
    var_font_size_Scale.set(str(data['font_size']))
    
    _alpha_Frame = Frame(win) # 透明度
    _alpha_Frame.pack()
    _alpha_Label = Label(_alpha_Frame, 
        text="主窗口\n透明度",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        #fg="red",
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    _alpha_Label.pack(side=LEFT)    # 固定窗口位置
    global var__alpha_Scale
    var__alpha_Scale = StringVar()
    _alpha_Scale = Scale(_alpha_Frame,# 滑块
        from_ = 0.0,#设置最小值
        to = 1.0,#设置最大值
        orient = HORIZONTAL,#设置横向
        resolution=0.01,#设置步长
        tickinterval = 0.2,#设置刻度
        length = 290,# 设置像素
        variable = var__alpha_Scale,#绑定变量
        command = lambda now_alpha_Scale: wset_up.wm_attributes("-alpha", now_alpha_Scale) 
        )
    _alpha_Scale.pack(side=LEFT)    # 固定滑块位置
    var__alpha_Scale.set(str(data['-alpha']))
    
    
    fb = Frame(win,
               #bg = data['background'],# 背景色
               )
    fb.pack(padx=5,pady=5)
    bsave_changes = Button(fb,
               # text="确定",
               text="保存",
               font=(data['font'], 14),        # 字体和字体大小
               #bg=data['buttonbg'],
               command=save_changes,
               )
    bsave_changes.pack(side=LEFT,padx=5,pady=5)
    bcancel = Button(fb,
               text="取消",
               font=(data['font'], 14),        # 字体和字体大小
               #bg=data['buttonbg'],
               command=wset_up.destroy,
               )
    bcancel.pack(side=LEFT,padx=5,pady=5)
    brestore_default = Button(fb,
               # text="确定",
               text="恢复默认",
               font=(data['font'], 14),        # 字体和字体大小
               #bg=data['buttonbg'],
               command=restore_default,
               )
    brestore_default.pack(side=LEFT,padx=5,pady=5)
    bupdata = Button(fb,
               # text="确定",
               text="检查更新",
               font=(data['font'], 14),        # 字体和字体大小
               #bg=data['buttonbg'],
               command=lambda: updata(data_default['verson'], data['font']),
               )
    bupdata.pack(side=LEFT,padx=5,pady=5)
    
    
    wset_up.wm_attributes("-alpha", data['-alpha']) 
    wset_up.mainloop()           #循环消息，让窗口活起来
    root()

def root():
    '''显示主窗口'''
    global window
    # global data
    # print(data)
    window=Tk()
    global fonts
    fonts = sorted([i for i in font.families() if not i.startswith("@")],reverse=True)
    global data
    if data["font"] == "默认字体":
        data["font"] = fonts[0]
    global data_default
    if data_default["font"] == "默认字体":
        data_default["font"] = fonts[0]
    # print(fonts)
    # print(data["font"])
    window.title("随机点名V%i.%i.%i.%i"%tuple([data['verson'][i] for i in range(4)]))
    window.resizable(0,0)# 禁止调节窗口大小
    try:# 尝试打开设置图标
        window.iconbitmap(icon_file_path)
    except:
        pass
    
    global var_no_repeat_roll_call
    
    var_no_repeat_roll_call = IntVar()
    
    var_no_repeat_roll_call.set(0)
    
    
    win = Frame(window,
                bg = data['background'],# 背景色
                )
    win.pack(fill=X)
    
    f1 = Frame(win,
               bg = data['background'],# 背景色
               )
    f1.pack(fill=X)
    '''
    try:# 尝试打开设置图片
        ppset_up = PhotoImage(file=".\\program\\image\\set_up.png")
    except:# 打开失败
        bset_up = Button(f1,
                         text="设置",
                         # bd=0,# 按钮边框的大小，默认为2个像素
                         bg = data['buttonbg'],# 按钮背景色
                         # image=pset_up,#加入图片
                         # compound = CENTER,#关键:设置为背景图片
                         font=(data['font'], 12),         # 字体和字体大小
                         command=set_up# 命令
                         )
    else:# 否则正常显示
        bset_up = Button(f1,
                     text="设置",
                     bd=0,# 按钮边框的大小，默认为2个像素
                     bg = data['background'],# 按钮背景色
                     image=ppset_up,#加入图片
                     # compound = CENTER,#关键:设置为背景图片
                     font=(data['font'], 12),         # 字体和字体大小
                     command=set_up,# 命令
                     )
    finally:# 最后
        bset_up.pack(side=LEFT)
    '''
    bset_up = Button(f1,
        text="设置",
        # bd=0,# 按钮边框的大小，默认为2个像素
        # bg = data['background'],# 按钮背景色
        bg = data['buttonbg'],# 按钮背景色
        # image=ppset_up,#加入图片
        # compound = CENTER,#关键:设置为背景图片
        font=(data['font'], 12),         # 字体和字体大小
        command=set_up,# 命令
        )
    bset_up.pack(side=LEFT)
    
    no_repeat_roll_call_Checkbutton = Checkbutton(f1, 
                     bg = data['background'],# 背景色
                     text='不重复点名', 
                     variable=var_no_repeat_roll_call, 
                     onvalue=1, 
                     offvalue=0,
                     font=(data['font'], 12),         # 字体和字体大小
                     command=no_repeat_roll_call,
                     )
    no_repeat_roll_call_Checkbutton.pack(side=LEFT)
    if not data['unrepeat']:
        no_repeat_roll_call_Checkbutton.pack_forget()
    
    global reset_Button
    reset_Button = Button(f1,
           text="复位",
           bg=data['buttonbg'],         # 背景颜色
           font=(data['font'], 12),         # 字体和字体大小
           command=reset,
           )
    reset_Button.pack(side=LEFT)
    reset_Button.pack_forget()
    
    global remaining_names_Lable
    remaining_names_Lable = Label(f1,
        # textvariable=v3,
        text='剩余姓名：'+str(len(names)-len(havenames))+'/'+str(len(names)),    # 标签的文字
        bg=data['background'],         # 背景颜色
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    remaining_names_Lable.pack(side=LEFT) # 固定窗口位置
    remaining_names_Lable.pack_forget()

    
    
    '''
    l1 = Label(f1, 
               text="                             ",    # 标签的文字
               bg = data['background'],# 背景色
               font=(data['font'], 12),         # 字体和字体大小
               #width=15, height=2          # 标签长宽
               )
    l1.pack(side=LEFT)    # 固定窗口位置
    '''
    '''
    try:# 尝试打开设置图片
        phelp = PhotoImage(file=".\\program\\image\\help.png")
    except:# 打开失败
        bhelp = Button(f1,
                         text="帮助",
                         #image=phelp,#加入图片
                         bg = data['buttonbg'],# 按钮背景色
                         #bd=0,# 按钮边框的大小，默认为2个像素
                         font=(data['font'], 12),         # 字体和字体大小
                         command=help,
                         )
    else:# 否则正常显示
        bhelp = Button(f1,
                         text="帮助",
                         image=phelp,#加入图片
                         bg = data['background'],# 按钮背景色
                         bd=0,# 按钮边框的大小，默认为2个像素
                         font=(data['font'], 12),         # 字体和字体大小
                         command=help,
                         )
    finally:# 最后
        bhelp.pack(side=RIGHT)
    '''
    bhelp = Button(f1,
         text="帮助",
         # image=phelp,#加入图片
         # bg = data['background'],# 按钮背景色
         bg = data['buttonbg'],# 按钮背景色
         # bd=0,# 按钮边框的大小，默认为2个像素
         font=(data['font'], 12),         # 字体和字体大小
         command=show_help,
         )
    bhelp.pack(side=RIGHT)
    
    
    
    f2 = Frame(win,
               bg = data['background'],# 背景色
               )
    f2.pack()
    '''
    l2 = Label(f2, 
        text="\n\n\n",    # 标签的文字
        bg = data['background'],# 背景色
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l2.pack()    # 固定窗口位置
    '''
    global lname
    lname = Label(f2, 
        text='',    # 标签的文字
        bg = data['background'],# 背景色
        font=(data['font'], data['font_size']),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    lname.pack()    # 固定窗口位置
    
    global random_roll_call_Button
    random_roll_call_Button = Button(f2,
               text="随机点名",
               bg = data['buttonbg'],# 按钮背景色
               font=(data['font'], 20),         # 字体和字体大小
               command=random_roll_call,
               )
    random_roll_call_Button.pack()# side=LEFT
    
    global start_pause_Button
    start_pause_Button = Button(f2,# 开始暂停
               text="开始点名",
               bg = data['buttonbg'],# 按钮背景色
               font=(data['font'], 20),         # 字体和字体大小
               command=start_pause,
               )
    start_pause_Button.pack()# side=LEFT
    '''
    l21 = Label(f2, 
        text="\n\n\n",    # 标签的文字
        bg = data['background'],# 背景色
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l21.pack()    # 固定窗口位置
    '''
    
    
    
    f3 = Frame(win,
               bg = data['background'],# 背景色
               )
    f3.pack(fill=X)    # 固定窗口位置
    
    clearing_Button = Button(f3,
               text="清零",
               bg = data['buttonbg'],# 按钮背景色
               font=(data['font'], 12),         # 字体和字体大小
               command=clearing,
               )
    clearing_Button.pack(side=LEFT)
    
    global cumulative_Label
    cumulative_Label = Label(f3, 
        # textvariable=v6,
        text="累计抽取人数："+str(data['cumulative']),    # 标签的文字
        bg = data['background'],# 背景色
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    cumulative_Label.pack(side=LEFT)    # 固定窗口位置
    
    
    lnone = Label(f3, 
               text="                   ",    # 标签的文字
               bg = data['background'],# 背景色
               font=(data['font'], 12),         # 字体和字体大小
               #width=15, height=2          # 标签长宽
               )
    lnone.pack(side=LEFT)    # 固定窗口位置
    
    
    reduce_font_size_Button = Button(f3,
               text="-",
               bg = data['buttonbg'],# 按钮背景色
               font=(data['font'], 12),         # 字体和字体大小
               command=reduce_font_size
               )
    reduce_font_size_Button.pack(side=RIGHT)
    
    increase_font_size_Button = Button(f3,
               text="+",
               bg = data['buttonbg'],# 按钮背景色
               font=(data['font'], 12),         # 字体和字体大小
               command=increase_font_size
               )
    increase_font_size_Button.pack(side=RIGHT)

    
    lzh = Label(f3, 
        text="字号：",    # 标签的文字
        bg = data['background'],# 背景色
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    lzh.pack(side=RIGHT)    # 固定窗口位置
    
    
    
    # window.protocol("WM_DELETE_WINDOW", save_exit)
    window.wm_attributes("-alpha", data['-alpha'])        # 透明度(0.0~1.0)
    # window.wm_attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
    window.wm_attributes("-topmost", data['-topmost'])     # 永远处于顶层    topmost
    window.mainloop()           #循环消息，让窗口活起来

def main():
    global data
    '程序入口函数'
    # 读数据
    data = read_data(data, json_data_file)
    
    data = change_data(data, data_default)
    data['verson'] = data_default['verson'] # 保持版本号为当前版本号
    data['program_path'] = sys.argv[0] # 更新程序路径
    data['program_name'] = data_default['program_name'] # 保持程序名为当前程序名
    
    first_read() #第一次（启动时）读取姓名
    root()# 显示主窗口
    
    data['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # 更新时间
    # 保存数据
    save_data(data, json_data_file)


if __name__ == '__main__':
    '''
    # 读数据
    data = read_data(data, json_data_file)
    
    root()# 显示主窗口
    # data['verson'] = [1,1,1,1]
    # root()# 显示主窗口
    
    # 保存数据
    save_data(data, json_data_file)
    '''
    """
    try:
        # 读数据
        data = read_data(data, json_data_file)
        
        data = change_data(data, data_default)
        data['verson'] = data_default['verson'] # 保持版本号为当前版本号
        data['program_path'] = sys.argv[0] # 更新程序路径
        data['program_name'] = data_default['program_name'] # 保持程序名为当前程序名
        
        first_read() #第一次（启动时）读取姓名
        root()# 显示主窗口
        # data['verson'] = [1,1,1,1]
        # root()# 显示主窗口
        data['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # 更新时间
        # 保存数据
        save_data(data, json_data_file)
    # except Exception as e:
    except:
        #exc_type, exc_value, exc_traceback_obj = sys.exc_info()
        # sys.exc_info() # (None, None, None)
        # print(sys.exc_info()[0].__dict__)
        #print(sys.exc_info()[0].__doc__)
        # messagebox.showerror(
        #                 title = '程序出错！',
        #                 message='程序出现未知错误！\n%s\n%s\n%s\n请和制作人联系!\n小喾苦QQ:3434623263' % (sys.exc_info()[0], sys.exc_info()[1] ,sys.exc_info()[2] ) )
        messagebox.showerror(
                        title = '程序出错！',
                        message='程序出现未知错误！请联系制作者(QQ(小喾苦):3434623263 Q群(随机点名):681032320)\n%s' % (format_exc() ))
    """
    pass
    
