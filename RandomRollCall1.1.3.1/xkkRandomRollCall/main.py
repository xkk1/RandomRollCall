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
import tkinter.simpledialog # 输入对话框
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
from .show_information import show_add1_help # 显示帮助
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
name_color = "#000000" # 姓名颜色
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
    'history_files': [], # 历史姓名文件，最多保存15个
    'background': "#f0f0f0", # 背景色
    'buttonbg': "#f0f0f0", # 按钮背景色
    'name_color': '#000000', # 姓名颜色
    '-alpha': 1.0, # 透明度
    '-topmost': False, # 是否置于顶层
    'encoding': "自动", # 文件默认编码
    'unrepeat': True, # 是否姓名去重
    'add1': False, # 是否打开加一模式
    'add1_tip': True, # 是否开启“+1”提示
    'extract_animation': True, # 是否启用“随机点名”抽取动画
    'window_auto_center': False, # 是否启用点名结束窗口自动居中
    'hide_unnecessary': False, # 主窗口隐藏不必要的
    'no_repeat_roll_call': False, #  不重复点名
    'names': [], # 读取的姓名
    'havenames': [], # 未抽取的姓名
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
    # global file
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
        # file = filename
        # vname_file.set(file)
        name_file_combobox.set(filename)
        # print(file)

def save_changes():
    """保存设置的更改"""
    # global names
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
    # global havenames
    global encoding_combobox
    if read_file:
        try:
            # name_file = vname_file.get()
            name_file = name_file_combobox.get()
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
                # data['names'] = names
                
                if name_file in data['history_files']:
                    data['history_files'].remove(name_file)
                if name_file != data['file']:
                    if data['file'] not in data['history_files']:
                        if len(data['history_files']) >= 15:
                            data['history_file'].pop()
                        data['history_files'].insert(0, data['file'])
                    else:
                        data['history_files'].remove(data['file'])
                        data['history_files'].insert(0, data['file'])
                # data['file'] = name_file
                # print(names)
                # for j in names:
                #     print(j)
        except UnicodeDecodeError:
            b = False
            string = (f'用“{encoding_combobox.get()}”编码解码文件“{name_file_combobox.get()}”失败！\n'
                    "您可以换几个文件编码试试，推荐“自动”、“UTF-8”、“UTF-8-SIG”、“GB18030”\n"
                    "win10、win7操作系统的用户可以用记事本打开姓名文件，点击菜单栏上的“文件(F)”、\
    点击“另存为(A)”，编码选择“ANSI”后点“保存(S)”\n，确认替换“是(Y)”，回到随机点名，在设置里的\
    姓名文件编码选择“自动”或“ANSI”就可以了（^_^）")
            info += string
            errorinfo += string + "报错：\n" + format_exc() +"\n"
        except LookupError:
            b = False
            string = (f'不支持用“{encoding_combobox.get()}”编码解码文件“{name_file_combobox.get()}”失败！\n'
                    "可能是编码拼写错误，请检查编码拼写\n"
                    "win10、win7操作系统的用户可以用记事本打开姓名文件，点击菜单栏上的“文件(F)”、\
    点击“另存为(A)”，编码选择“ANSI”后点“保存(S)”\n，确认替换“是(Y)”，回到随机点名，在设置里的\
    姓名文件编码选择“自动”或“ANSI”就可以了（^_^）")
            info += string
            errorinfo += string + "报错：\n" + format_exc() +"\n"
        except:
            b = False
            # string = '读取文件“%s”失败！\n' % vname_file.get() # , format_exc())
            string = '读取文件“%s”失败！\n' % name_file_combobox.get() # , format_exc())
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
    try:
        name_color_show_Frame['bg'] = vname_color.get()
        data['name_color'] = vname_color.get()
    except:
        b = False
        string = '无效的姓名颜色“%s”!\n' % vname_color.get()
        info += string
        errorinfo += string + "报错：\n" + format_exc() +"\n"

    if b:
        data['background'] = vbackground.get()
        data['buttonbg'] = vbuttonbg.get()
        data['name_color'] = vname_color.get()
        data['font_size'] = int(var_font_size_Scale.get())
        data['-alpha'] = float(var__alpha_Scale.get())
        data['-topmost'] = var__topmost_Checkbutton.get()
        data['encoding'] = encoding_combobox.get()
        data['font'] = font_combobox.get()
        data['add1']  = var_add1_Checkbutton.get()
        data['add1_tip'] = var_add1_tip_Checkbutton.get()
        data['extract_animation'] = var_extract_animation_Checkbutton.get()
        data['window_auto_center'] = var_window_auto_center_Checkbutton.get()
        data['hide_unnecessary'] = var_hide_unnecessary_Checkbutton.get()
        data['no_repeat_roll_call'] = setting_no_repeat_roll_call
        # havenames = []
        if read_file:
            data['unrepeat'] = var_unrepeat_Checkbutton.get()
            data['file'] = name_file
            data['names'] = names
            data['havenames'] = data['names'].copy()
        else:
            data['havenames'] = setting_havenames
        # 保存数据
        save_data(data, json_data_file)
        wset_up.destroy()# 销毁设置窗口
    else:
        # messagebox.showerror(title='数据错误！',message=string)
        show_information(information=info+errorinfo, title="保存设置时出错！", icon=icon_file_path)

def pack_packforget_preview_add1_button():
    """设置中“+1”按钮的显示与否"""
    global var_add1_Checkbutton
    global add1_preview_Button
    global add1_tip_Checkbutton
    if var_add1_Checkbutton.get():
        add1_preview_Button.pack(side=LEFT)
        add1_tip_Checkbutton.pack(side=RIGHT)
    else:
        add1_preview_Button.pack_forget()
        add1_tip_Checkbutton.pack_forget()

def restore_default():
    '''恢复默认'''
    # global data
    global file
    global background
    global buttonbg
    global name_color
    global f21
    global f31
    global name_color_show_Frame
    
    # data = data_default
    file = data_default['file']
    background = data_default['background']
    buttonbg = data_default['buttonbg']
    name_color = data_default['name_color']
    
    f21['bg'] = data_default['background']
    f31['bg'] = data_default['buttonbg']
    name_color_show_Frame['bg'] = data_default['name_color']
    
    # vname_file.set(data_default['file'])
    name_file_combobox.set(data_default['file'])
    vbackground.set(data_default['background'])
    vbuttonbg.set(data_default['buttonbg'])
    vname_color.set(data_default['name_color'])
    var_font_size_Scale.set(data_default['font_size'])
    var__alpha_Scale.set(str(data_default['-alpha']))
    var__topmost_Checkbutton.set(data_default['-topmost'])
    var_unrepeat_Checkbutton.set(data_default['unrepeat'])
    encoding_combobox.set(data_default['encoding'])
    font_combobox.set(data_default['font'])
    wset_up.wm_attributes("-alpha", data_default['-alpha'])
    preview_name_Label["font"]= (data_default['font'], data_default['font_size'])
    preview_Button["font"]= (data_default['font'], 20)
    var_add1_Checkbutton.set(data_default['add1'])
    var_add1_tip_Checkbutton.set(data_default['add1_tip'])
    var_extract_animation_Checkbutton.set(data_default['extract_animation'])
    var_window_auto_center_Checkbutton.set(data_default['window_auto_center'])
    var_hide_unnecessary_Checkbutton.set(data_default['hide_unnecessary'])
    var_no_repeat_roll_call.set(data_default['no_repeat_roll_call'])

    pack_packforget_preview_add1_button()

def first_read():
    '第一次（启动时）读姓名'
    global data
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
            
            # data['file'] = name_file
            data['names'] = names
            # print(names)
            # for j in names:
            #     print(j)
    except:
        pass
    
    # if names == []: # 如果没有读到任何姓名
        # names = ['孙八', '张三', '吴十', '刘一', '李四', '杨九', '陈二', '赵六', '钱七', '王五']
        # print('暂无姓名！')
        # pass

def change_background_color(color):
    '及时改变背景颜色'
    # print('change_background_color')
    global f21
    global preview_name_Label
    global preview_LabelFrame
    global preview_name_Frame
    try:
        f21['bg'] = color
        preview_name_Label['bg'] = color
        preview_LabelFrame['bg'] = color
        preview_name_Frame['bg'] = color
    except:
        pass
    return True

def change_buttonbg_color(color):
    '及时改变按钮颜色'
    global f31
    global preview_Button
    global add1_example_Button
    try:
        f31['bg'] = color
        preview_Button['bg'] = color
        add1_preview_Button['bg'] = color
    except:
        pass
    return True

def change_name_color_show(color):
    '及时改变姓名颜色'
    global name_color_show_Frame
    global preview_name_Label

    try:
        name_color_show_Frame['bg'] = color
        preview_name_Label['fg'] = color
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

def colorchooser_change_name_color():
    # print("name_color")
    color = colorchooser.askcolor(data['name_color'])
    # print(color[1])
    if color[1] != None:
        vname_color.set(color[1])

def no_repeat_roll_call():
    # global remaining_names_Lable
    if var_no_repeat_roll_call.get():
        data['no_repeat_roll_call'] = True
        reset_Button.pack(side=LEFT)
        remaining_names_Lable.pack(side=LEFT)
    else:
        data['no_repeat_roll_call'] = False
        reset_Button.pack_forget()
        remaining_names_Lable.pack_forget()
    
    # 窗口大小自适应
    window.update()
    width = window.winfo_reqwidth()
    height = window.winfo_reqheight()
    if data['window_auto_center']:
        # 启用窗口自动居中
        screenwidth = window.winfo_screenwidth()  # 获取显示屏宽度
        screenheight = window.winfo_screenheight()  # 获取显示屏高度
        window.geometry("%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2) )
    else:
        window.geometry("%dx%d" % (width, height))

def no_repeat_roll_call_setting_command():
    global setting_no_repeat_roll_call
    if var_no_repeat_roll_call.get():
        setting_no_repeat_roll_call = True
        reset_Button.pack(side=LEFT)
        remaining_names_Lable.pack(side=LEFT)
    else:
        setting_no_repeat_roll_call = False
        reset_Button.pack_forget()
        remaining_names_Lable.pack_forget()

def increase_font_size():
    '增加字号'
    global data
    
    if data['font_size'] <= 495:
        lname['font'] = (data['font'], data['font_size']+5)
        data['font_size'] += 5
        
        # 窗口大小自适应
        window.update()
        width = window.winfo_reqwidth()
        height = window.winfo_reqheight()
        if data['window_auto_center']:
            # 启用窗口自动居中
            screenwidth = window.winfo_screenwidth()  # 获取显示屏宽度
            screenheight = window.winfo_screenheight()  # 获取显示屏高度
            window.geometry("%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2) )
        else:
            window.geometry("%dx%d" % (width, height))
    # print(data['font_size']) 1-335

def reduce_font_size():
    '减少字号'
    global data
    
    if data['font_size'] > 5:
        lname['font'] = (data['font'], data['font_size']-5)
        data['font_size'] -= 5
        
        # 窗口大小自适应
        window.update()
        width = window.winfo_reqwidth()
        height = window.winfo_reqheight()
        if data['window_auto_center']:
            # 启用窗口自动居中
            screenwidth = window.winfo_screenwidth()  # 获取显示屏宽度
            screenheight = window.winfo_screenheight()  # 获取显示屏高度
            window.geometry("%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2) )
        else:
            window.geometry("%dx%d" % (width, height))

def reset():# 复位
    global data
    remaining_names_Lable['text'] = "剩余姓名："+str(len(data['names']))+'/'+ str(len(data['names']))
    data['havenames'] = data['names'].copy()

def reset_setting_command():# 复位
    global setting_havenames
    remaining_names_Lable['text'] = "剩余姓名："+str(len(data['names']))+'/'+ str(len(data['names']))
    setting_havenames = data['names'].copy()

def extract_animation():
    '“随机点名”抽取动画'
    global data
    # names = data['names']
    random_roll_call_Button['state'] = DISABLED   # 禁用
    start_pause_Button['state'] = DISABLED   # 禁用
    #################姓名抽取动画#################################################
    if data['extract_animation']:
        # print("抽取动画开始")
        # 选择抽取动画的姓名
        if not data['no_repeat_roll_call']: # 如果没有选不重复点名
            if len(data['names']) > 7:
                randomnames = sample(data['names'], 7) # 随机抽取7个名字
            else:
                randomnames = data['names']
        else:
            if len(data['havenames']) > 7:
                randomnames = sample(data['havenames'], 7) # 随机抽取7个名字
            else:
                randomnames = data['havenames']
        # 显示抽取动画
        for i in range(len(randomnames)):
            lname['text'] = randomnames[i]
            time.sleep((i + 1) / 35)
        # print('抽取动画结束')
    ##########################################################################

    # 随机点名核心——随机抽取姓名
    if not data['no_repeat_roll_call']: # 如果没有选不重复点名
        name = sample(data['names'], 1)[0] # 随机抽取1个名字
    else: # 如果选中不重复点名
        # print('选中不重复点名')
        name = sample(data['havenames'], 1)[0] # 随机抽取1个名字
        data['havenames'].remove(name)

        if(len(data['havenames']) == 0):
            data['havenames'] = data['names'].copy()

        remaining_names_Lable['text'] = '剩余姓名：'+str(len(data['havenames']))+'/'+ str(len(data['names']))
        # print(havenames)
    
    lname['text'] = name
    data['cumulative'] += 1
    cumulative_Label['text'] = '累计抽取人数：' + str(data['cumulative'])
    
    random_roll_call_Button['state'] = NORMAL     # 重新激活
    start_pause_Button['state'] = NORMAL     # 重新激活

    # 窗口大小自适应
    window.update()
    width = window.winfo_reqwidth()
    height = window.winfo_reqheight()
    if data['window_auto_center']:
        # 启用窗口自动居中
        screenwidth = window.winfo_screenwidth()  # 获取显示屏宽度
        screenheight = window.winfo_screenheight()  # 获取显示屏高度
        window.geometry("%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2) )
    else:
        window.geometry("%dx%d" % (width, height))
    
    exit() # 退出线程

def random_roll_call():
    '随机点名'
    # global data
    # global havenames
    # global animation
    if len(data['names']) == 0:
        messagebox.showerror(title = '没有指定姓名文件',
            message='没有指定姓名文件！\n或姓名文件被删除！\
\n或姓名文件为空\n请先指明姓名文件！')
    elif len(data['names']) == 1:
        lname['text'] = data['names'][0]
        data['cumulative'] += 1
        cumulative_Label['text'] = '累计抽取人数：' + str(data['cumulative'])
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
    # 2023-1-11 完了，我已经看不懂我之前写的代码了……
    ''' # 这是之前写的屎一样的代码……
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
    '''
    # global animation
    name_index = 0
    if(not data['no_repeat_roll_call']): # 如果没选不重复点名
        while animation:
            if(name_index == len(data['names'])):
                name_index = 0
            lname['text'] = data['names'][name_index]
            name_index += 1
            time.sleep(0.02)
    else:
        only_one = False
        if(len(data['havenames']) == 1):
            lname['text'] = data['havenames'][0]
            data['havenames'] = data['names'].copy()
            start_pause() # 只剩1人时停止滚动点名
            only_one = True
        while animation:
            if(name_index == len(data['havenames'])):
                name_index = 0
            lname['text'] = data['havenames'][name_index]
            name_index += 1
            time.sleep(0.02)
        if(not only_one):
            data['havenames'].remove(lname['text'])
        remaining_names_Lable['text'] = '剩余姓名：'+str(len(data['havenames']))+'/'+ str(len(data['names']))
    
    data['cumulative'] += 1
    cumulative_Label['text'] = '累计抽取人数：' + str(data['cumulative'])

    

def start_pause():
    '控制动画（滚动点名）的开始暂停'
    global animation
    global data
    
    if len(data['names']) == 0:
        messagebox.showerror(title = '没有指定姓名文件',
                            message='没有指定姓名文件！\n或姓名文件被删除！\n请先指明姓名文件！')
    elif len(data['names']) == 1:
        lname['text'] = data['names'][0]
        data['cumulative'] += 1
        cumulative_Label['text'] = '累计抽取人数：' + str(data['cumulative'])
    else:
        if animation:
            random_roll_call_Button['state'] = NORMAL # 重新激活
            animation = False
            start_pause_Button['text'] = '开始点名'
            
            # 窗口大小自适应
            window.update()
            width = window.winfo_reqwidth()
            height = window.winfo_reqheight()
            if data['window_auto_center']:
                # 启用窗口自动居中
                screenwidth = window.winfo_screenwidth()  # 获取显示屏宽度
                screenheight = window.winfo_screenheight()  # 获取显示屏高度
                window.geometry("%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2) )
            else:
                window.geometry("%dx%d" % (width, height))
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

def hide_unnecessary_function():
    # global var_hide_unnecessary_Checkbutton
    if var_hide_unnecessary_Checkbutton.get():
        pass
    else:
        pass
    # TODOXKK

def auto_disabled_no_repeat_roll_call_Frame():
    if var_unrepeat_Checkbutton.get(): # and var_hide_unnecessary_Checkbutton.get():
        # no_repeat_roll_call_Frame.pack(expand=YES, fill=X ,padx=5, pady=5)
        no_repeat_roll_call_Checkbutton['state'] = NORMAL     # 重新激活
        reset_Button['state'] = NORMAL     # 重新激活
        remaining_names_Lable['state'] = NORMAL     # 重新激活
    else:
        no_repeat_roll_call_Checkbutton['state'] = DISABLED   # 禁用
        reset_Button['state'] = DISABLED   # 禁用
        remaining_names_Lable['state'] = DISABLED   # 禁用
        # no_repeat_roll_call_Frame.pack_forget()
    # no_repeat_roll_call_father_Frame.pack(expand=YES, fill=X)

def set_up():
    '''显示设置窗口'''
    global window
    global wset_up
    # global data
    global file
    global background
    global buttonbg
    global f21 # 方便保存时更改背景色
    global f31 # 方便保存时更改背景色（用来测试）
    global name_color_show_Frame
    global animation

    global setting_havenames
    global setting_no_repeat_roll_call
    setting_havenames = data['havenames']
    setting_no_repeat_roll_call = data['no_repeat_roll_call']
    global read_file
    read_file = False # 是否选择读重新文件

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
    
    # global vname_file
    global vbackground
    global vbuttonbg
    global vname_color
    
    # vname_file = StringVar()
    vbackground = StringVar()
    vbuttonbg = StringVar()
    vname_color = StringVar()
    
    # vname_file.set(file)
    vbackground.set(data['background'])
    vbuttonbg.set(data['buttonbg'])
    vname_color.set(data['name_color'])

    def show_name_file_setting():
        global read_file
        l1.pack(side=LEFT)    # “姓名文件：”
        name_file_combobox.pack(expand=YES, fill=X, side=LEFT)    # 姓名文件输入框
        bchoice.pack(side=RIGHT) # 选择文件
        l11.pack(side=LEFT)    # 姓名文件编码
        encoding_combobox.pack(expand=YES, fill=X, side=LEFT)    # 文件编码输入框
        b_encoding_help.pack(side=RIGHT) # 什么是文件编码
        unrepeat_Checkbutton['state'] = NORMAL     # 重新激活
        show_name_file_setting_Button.pack_forget()
        no_repeat_roll_call_help_Label.pack_forget()
        read_file = True

    f1 = Frame(wset_up,# win,
               #bg = data['background'],# 背景色
               )
    f1.pack(expand=YES, fill=X, padx=5, pady=5)
    
    l1 = Label(f1, 
        text="姓名文件：",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    """
    ename_file = Entry(f1,# 姓名文件名输入框
               textvariable=vname_file,
               #bg=data['background'],          # 背景颜色
               width=30,# 宽度
               )
    ename_file.pack(side=LEFT, expand=YES, fill=X)
    SetRightClickMenu(ename_file, undo=False)
    """
    global name_file_combobox
    name_file_combobox = ttk.Combobox(f1, width=30)
    name_file_combobox['value'] = [data['file']] + data['history_files']
    name_file_combobox.set(data["file"])
    SetRightClickMenu(name_file_combobox, undo=False)
    # name_file_combobox.configure(state="readonly")
    
    bchoice = Button(f1,
               text="选择\n文件",
               #bg = data['buttonbg'],# 按钮背景色
               font=(data['font'], 10),         # 字体和字体大小
               command=choice,
               #width=25, height=25          # 标签长宽
               )

    f1down = Frame(wset_up,# win,
               #bg = data['background'],# 背景色
               )
    f1down.pack(expand=YES, fill=BOTH)
    
    global preview_LabelFrame
    preview_LabelFrame = LabelFrame(f1down, text='预览', padx=5, pady=5, bg = data['background'], font=(data['font'], 12))
    preview_LabelFrame.pack(side=RIGHT)

    global preview_name_Frame
    preview_name_Frame = Frame(preview_LabelFrame, bg = data['background'])
    preview_name_Frame.pack(padx=5, pady=5)
    
    global preview_name_Label
    preview_name_Label = Label(preview_name_Frame,
                               text="姓名",
                               bg = data['background'],# 背景色
                               fg = data['name_color'],
                               font=(data['font'], data['font_size']),         # 字体和字体大小
                               )
    preview_name_Label.pack(side=LEFT)

    global add1_preview_Button
    add1_preview_Button= Button(preview_name_Frame,
                                text="+1",
                                bg = data['buttonbg'],
                                font=(data['font'], 12),
                                command=show_add1_help
                                )
    # add1_preview_Button.pack(side=LEFT)
    # add1_preview_Button.pack_forget()
    if data['add1']:
        add1_preview_Button.pack(side=LEFT)
    def change_preview_name():
        new_preview_name = tkinter.simpledialog.askstring(title = '更改预览姓名',prompt='请输入新的预览姓名：',initialvalue = preview_name_Label['text'])
        while new_preview_name == '':
            new_preview_name = tkinter.simpledialog.askstring(title = '更改预览姓名',prompt='预览姓名不能为空！\n请重新输入新的预览姓名：',initialvalue = preview_name_Label['text'])
        preview_name_Label['text'] = new_preview_name
    global preview_Button
    preview_Button = Button(preview_LabelFrame,
                            text="按钮",
                            bg = data['buttonbg'],# 按钮背景色
                            font=(data['font'], 20),         # 字体和字体大小
                            command=change_preview_name
                            )
    preview_Button.pack(padx=20, pady=20)

    separator = ttk.Separator(f1down, orient=VERTICAL) # HORIZONTAL为横分割线
    separator.pack(side=RIGHT, padx=5, pady=5, fill=Y)

    

    win = Frame(f1down,
                #bg = data['background'],# 背景色
                )
    win.pack(side=LEFT)
    
    """
# 设置状态为只读
self.Combo3.configure(state="readonly")
# 设置状态为禁用
#self.Combo3.configure(state="disabled")
    obj['state'] = DISABLED   ###禁用
    obj['state'] = NORMAL     ###重新激活
    """
    show_name_file_setting_Button = Button(win,
                text="读取新的姓名文件 或 重新读取姓名",
               bg = "orange", # 按钮背景色
               font=(data['font'], 14),         # 字体和字体大小
               command=show_name_file_setting,
               )
    show_name_file_setting_Button.pack(expand=YES, fill=X, padx=5)

    f11 = Frame(win,
               #bg = data['background'],# 背景色
               )
    f11.pack(expand=YES, fill=X, padx=5, pady=5)
    
    l11 = Label(f11, 
        text="姓名文件编码：",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    

    global encoding_combobox
    encoding_combobox = ttk.Combobox(f11, width=15)
    encoding_combobox['value'] = ["自动", "ANSI","UTF-8", "UTF-8-SIG",
                                  "UTF-16", "UTF-16 LE", "UTF-16 BE",
                                  "GB18030", "GB2312", "BIG5"]
    encoding_combobox.set(data["encoding"])

    SetRightClickMenu(encoding_combobox, undo=False)
    # encoding_combobox.configure(state="readonly")

    b_encoding_help = Button(f11,
               text="什么是\n文件编码",
               #bg = data['buttonbg'],# 按钮背景色
               font=(data['font'], 10),         # 字体和字体大小
               command=show_encoding_help,
               #width=25, height=25          # 标签长宽
               )
    
    
    f2 = Frame(win,
               #bg = data['background'],# 背景色
               )
    f2.pack(expand=YES, fill=X, padx=5, pady=5)
    
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
    f21.pack(expand=YES, fill=BOTH, side=LEFT)
    
    colorchooser_background_color_Button = Button(f2,
        text="选择",
        command = colorchooser_change_background_color,
        font=(data['font'], 12),         # 字体和字体大小
        )
    colorchooser_background_color_Button.pack(side=LEFT)
    
    f3 = Frame(win,
               #bg = data['background'],# 背景色
               )
    f3.pack(expand=YES, fill=X, padx=5, pady=5)
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
    f31.pack(expand=YES, fill=BOTH, side=LEFT)
    
    colorchooser_buttonbg_color_Button = Button(f3,
        text="选择",
        command = colorchooser_change_buttonbg_color,
        font=(data['font'], 12),         # 字体和字体大小
        )
    colorchooser_buttonbg_color_Button.pack(side=LEFT)



    name_color_Frame = Frame(win,
               #bg = data['background'],# 背景色
               )
    name_color_Frame.pack(expand=YES, fill=X, padx=5, pady=5)
    name_color_show_Label = Label(name_color_Frame, 
        text="姓名颜色：",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        #fg="red",
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    name_color_show_Label.pack(side=LEFT)    # 固定窗口位置
    # l3['state'] = DISABLED   ###禁用
    
    change_name_color_show_CMD = wset_up.register(change_name_color_show) # 包装起来
    name_color_Entry = Entry(name_color_Frame,
               textvariable=vname_color,#可变本文
               #bg=data['background'],          # 背景颜色
               width=10,# 宽度
               validate='key', # 启用验证，当输入框被编辑时验证
               validatecommand=(change_name_color_show_CMD, '%P'),
               )
    name_color_Entry.pack(side=LEFT)
    SetRightClickMenu(name_color_Entry, undo=False)
    name_color_show_Frame = Frame(name_color_Frame,
               bg = data['name_color'],
               width=135,
               height=25,
               )
    name_color_show_Frame.pack(expand=YES, fill=BOTH, side=LEFT)
    
    colorchooser_name_color_Button = Button(name_color_Frame,
        text="选择",
        command = colorchooser_change_name_color,
        font=(data['font'], 12),         # 字体和字体大小
        )
    colorchooser_name_color_Button.pack(side=LEFT)


    
    f4 = Frame(win,
               #bg = data['background'],# 背景色
               )
    f4.pack(expand=YES, fill=X, padx=5, pady=5)
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
                     command=auto_disabled_no_repeat_roll_call_Frame,
                     )
    unrepeat_Checkbutton.pack(side=RIGHT)
    unrepeat_Checkbutton['state'] = DISABLED   # 禁用
    add1_Frame = Frame(win)
    add1_Frame.pack(expand=YES, fill=X, padx=5, pady=5)
    global var_add1_Checkbutton
    var_add1_Checkbutton = BooleanVar()
    var_add1_Checkbutton.set(data['add1'])
    add1_Checkbutton = Checkbutton(add1_Frame, 
                     #bg = data['background'],# 背景色
                     text='增加被点到的概率“+1”', 
                     variable=var_add1_Checkbutton, 
                     onvalue=True, 
                     offvalue=False,
                     font=(data['font'], 12),         # 字体和字体大小
                     command=pack_packforget_preview_add1_button
                     )
    add1_Checkbutton.pack(side=LEFT)
    add1_help_Button = Button(add1_Frame,
                              text="什么是“+1”",
                              command=show_add1_help,
                              font=(data['font'], 12),         # 字体和字体大小
                              )
    add1_help_Button.pack(side=RIGHT)

    extract_animation_add1_tip_Frame = Frame(win)
    extract_animation_add1_tip_Frame.pack(expand=YES, fill=X, padx=5, pady=5)
    global var_extract_animation_Checkbutton
    var_extract_animation_Checkbutton = BooleanVar()
    var_extract_animation_Checkbutton.set(data['extract_animation'])
    extract_animation_Checkbutton = Checkbutton(extract_animation_add1_tip_Frame, 
                     #bg = data['background'],# 背景色
                     text='“随机点名”抽取动画', 
                     variable=var_extract_animation_Checkbutton, 
                     onvalue=True, 
                     offvalue=False,
                     font=(data['font'], 12),         # 字体和字体大小
                     )
    extract_animation_Checkbutton.pack(side=LEFT)
    global var_add1_tip_Checkbutton
    var_add1_tip_Checkbutton = BooleanVar()
    var_add1_tip_Checkbutton.set(data['add1_tip'])
    global add1_tip_Checkbutton
    add1_tip_Checkbutton = Checkbutton(extract_animation_add1_tip_Frame, 
                     #bg = data['background'],# 背景色
                     text='“+1”提示', 
                     variable=var_add1_tip_Checkbutton, 
                     onvalue=True, 
                     offvalue=False,
                     font=(data['font'], 12),         # 字体和字体大小
                     )
    add1_tip_Checkbutton.pack(side=RIGHT)
    if(not data['add1']):
        add1_tip_Checkbutton.pack_forget()

    window_auto_center_Frame = Frame(win)
    window_auto_center_Frame.pack(expand=YES, fill=X, padx=5, pady=5)
    global var_window_auto_center_Checkbutton
    var_window_auto_center_Checkbutton = BooleanVar()
    var_window_auto_center_Checkbutton.set(data['window_auto_center'])
    window_auto_center_Checkbutton = Checkbutton(window_auto_center_Frame, 
                     #bg = data['background'],# 背景色
                     text='点名后窗口自动居中', 
                     variable=var_window_auto_center_Checkbutton, 
                     onvalue=True, 
                     offvalue=False,
                     font=(data['font'], 12),         # 字体和字体大小
                     )
    window_auto_center_Checkbutton.pack(side=LEFT)
    global var_hide_unnecessary_Checkbutton
    var_hide_unnecessary_Checkbutton = BooleanVar()
    var_hide_unnecessary_Checkbutton.set(data['hide_unnecessary'])
    hide_unnecessary_Checkbutton = Checkbutton(window_auto_center_Frame, 
                     #bg = data['background'],# 背景色
                     text='主窗口隐藏不必要的', 
                     variable=var_hide_unnecessary_Checkbutton, 
                     onvalue=True, 
                     offvalue=False,
                     font=(data['font'], 12),         # 字体和字体大小
                     command=lambda:messagebox.showinfo("随机点名——提示","设置可从主窗口右键或按键盘“s”打开！") if var_hide_unnecessary_Checkbutton.get() else None,
                     )
    hide_unnecessary_Checkbutton.pack(side=RIGHT)

    global no_repeat_roll_call_Frame
    no_repeat_roll_call_Frame = Frame(win)
    no_repeat_roll_call_Frame.pack(expand=YES, fill=X ,padx=5, pady=5)

    global var_no_repeat_roll_call
    var_no_repeat_roll_call = BooleanVar()
    var_no_repeat_roll_call.set(data['no_repeat_roll_call'])

    global no_repeat_roll_call_Checkbutton
    no_repeat_roll_call_Checkbutton = Checkbutton(no_repeat_roll_call_Frame, 
                     bg = data['background'],# 背景色
                     text='不重复点名', 
                     variable=var_no_repeat_roll_call, 
                     onvalue=1, 
                     offvalue=0,
                     font=(data['font'], 12),         # 字体和字体大小
                     command=no_repeat_roll_call_setting_command,
                     )
    no_repeat_roll_call_Checkbutton.pack(side=LEFT)
    
    global reset_Button
    reset_Button = Button(no_repeat_roll_call_Frame,
           text="复位",
           bg=data['buttonbg'],         # 背景颜色
           font=(data['font'], 12),         # 字体和字体大小
           command=reset_setting_command,
           )
    reset_Button.pack(side=LEFT)
    if(not data['no_repeat_roll_call']):
        reset_Button.pack_forget()
    
    global remaining_names_Lable
    remaining_names_Lable = Label(no_repeat_roll_call_Frame,
        # textvariable=v3,
        text='剩余姓名：'+str(len(data['havenames']))+'/'+str(len(data['names'])),    # 标签的文字
        bg=data['background'],         # 背景颜色
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    remaining_names_Lable.pack(side=LEFT) # 固定窗口位置
    if(not data['no_repeat_roll_call']):
        remaining_names_Lable.pack_forget()
    
    global no_repeat_roll_call_help_Label
    no_repeat_roll_call_help_Label = Label(no_repeat_roll_call_Frame,
        # textvariable=v3,
        text="需勾选姓名去重才能使用",    # 标签的文字
        fg="red",
        bg=data['background'],         # 背景颜色
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    no_repeat_roll_call_help_Label.pack(side=RIGHT) # 固定窗口位置
    if(data['unrepeat']):
        no_repeat_roll_call_help_Label.pack_forget()

    auto_disabled_no_repeat_roll_call_Frame()


    font_Frame = Frame(win,
               #bg = data['background'],# 背景色
               )
    font_Frame.pack(expand=YES, fill=X ,padx=5, pady=5)
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
    font_combobox.pack(expand=YES, fill=X, side=LEFT)    # 固定窗口位置
    font_combobox.configure(state="readonly")
    # combobox.bind("<<ComboboxSelected>>",lambda event:set_information(get_information(combobox.get()))) #绑定事件,(下拉列表框被选中时，绑定go()函数)
    # global font_example_label
    font_example_label = Label(font_Frame, 
        text="字体示例example",    # 标签的文字
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
    font_size_Frame.pack(expand=YES, fill=X ,padx=5, pady=5)
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
    font_size_Scale.pack(expand=YES, fill=X, side=LEFT)    # 固定滑块位置
    var_font_size_Scale.set(str(data['font_size']))
    
    _alpha_Frame = Frame(win) # 透明度
    _alpha_Frame.pack(expand=YES, fill=X ,padx=5, pady=5)
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
        from_ = 0.0, # 设置最小值
        to = 1.0, # 设置最大值
        orient = HORIZONTAL, # 设置横向
        resolution=0.01, # 设置步长
        tickinterval = 0.2, # 设置刻度
        length = 290, # 设置像素
        variable = var__alpha_Scale, # 绑定变量
        command = lambda now_alpha_Scale: wset_up.wm_attributes("-alpha", now_alpha_Scale) 
        )
    _alpha_Scale.pack(expand=YES, fill=X, side=LEFT)    # 固定滑块位置
    var__alpha_Scale.set(str(data['-alpha']))
    
    
    fb = Frame(win,
               #bg = data['background'],# 背景色
               )
    fb.pack(padx=5,pady=5)
    bsave_changes = Button(fb,
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
               text="恢复默认",
               font=(data['font'], 14),        # 字体和字体大小
               #bg=data['buttonbg'],
               command=restore_default,
               )
    brestore_default.pack(side=LEFT,padx=5,pady=5)
    bupdata = Button(fb,
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
    # window.resizable(0,0)# 禁止调节窗口大小
    # window.geometry('')
    try:# 尝试打开设置图标
        window.iconbitmap(icon_file_path)
    except:
        pass
    
    global var_no_repeat_roll_call
    
    var_no_repeat_roll_call = BooleanVar()
    
    var_no_repeat_roll_call.set(data['no_repeat_roll_call'])
    
    
    win = Frame(window,
                bg = data['background'],# 背景色
                )
    win.pack(fill=X)
    
    f1 = Frame(win,
               bg = data['background'],# 背景色
               )
    f1.pack(fill=X)
    if(data['hide_unnecessary']):
        f1.pack_forget()
    
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

    lzh = Label(f1, 
        text="字号：",    # 标签的文字
        bg = data['background'],# 背景色
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    lzh.pack(side=LEFT)    # 固定窗口位置

    increase_font_size_Button = Button(f1,
               text="+",
               bg = data['buttonbg'],# 按钮背景色
               font=(data['font'], 12),         # 字体和字体大小
               command=increase_font_size
               )
    increase_font_size_Button.pack(side=LEFT)

    reduce_font_size_Button = Button(f1,
               text="-",
               bg = data['buttonbg'],# 按钮背景色
               font=(data['font'], 12),         # 字体和字体大小
               command=reduce_font_size
               )
    reduce_font_size_Button.pack(side=LEFT)

    # no_repeat_roll_call_Frame = Frame(f1,
    #            bg = data['background'],# 背景色
    #            )
    # no_repeat_roll_call_Frame.pack(fill=X) 
    
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
    if not data['unrepeat']: # 如果姓名可以重复
        no_repeat_roll_call_Checkbutton.pack_forget()
        data['no_repeat_roll_call'] = False
    
    global reset_Button
    reset_Button = Button(f1,
           text="复位",
           bg=data['buttonbg'],         # 背景颜色
           font=(data['font'], 12),         # 字体和字体大小
           command=reset,
           )
    reset_Button.pack(side=LEFT)
    if(not data['no_repeat_roll_call']):
        reset_Button.pack_forget()
    
    global remaining_names_Lable
    remaining_names_Lable = Label(f1,
        # textvariable=v3,
        text='剩余姓名：'+str(len(data['havenames']))+'/'+str(len(data['names'])),    # 标签的文字
        bg=data['background'],         # 背景颜色
        font=(data['font'], 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    remaining_names_Lable.pack(side=LEFT) # 固定窗口位置
    if(not data['no_repeat_roll_call']):
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
    bset_up.pack(side=RIGHT)
    
    
    
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
    fname = Frame(f2,bg=data['background'])
    fname.pack()
    global lname
    lname = Label(fname, 
        text='',    # 标签的文字
        bg = data['background'],# 背景色
        fg = data['name_color'],
        font=(data['font'], data['font_size']),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    lname.pack(side=LEFT)    # 固定窗口位置
    
    def add1():
        global data
        now_name = lname['text']
        if now_name == '':
            messagebox.showinfo(title='不能“+1”', message="没有抽取姓名，不能使用“+1”功能")
        else:
            while ( len(now_name) != 0 ) and ( now_name[-1] in "0123456789"):
                now_name = now_name[:-1]
            # print(now_name)
            num  = 0
            while True:
                num += 1
                if now_name + str(num) not in data['names']:
                    data['names'].append(now_name + str(num))
                    data['havenames'].append(now_name + str(num))
                    shuffle(data['names']) # 打乱姓名列表
                    shuffle(data['havenames']) # 打乱姓名列表
                    # print(names)
                    break
            global remaining_names_Lable
            remaining_names_Lable['text'] = '剩余姓名：'+str(len(data['havenames']))+'/'+str(len(data['names']))
            if data['add1_tip']:
                messagebox.showinfo(title=f"“{now_name}”被“+1”", message=f"已提高“{now_name}”被抽到的概率\n目前是“{now_name+str(num)}”")
            
    
    global add1_Button
    add1_Button = Button(fname,
                         text="+1",
                         font=(data['font'], 12), # 字体和字体大小
                         bg = data['buttonbg'],# 按钮背景色
                         command=add1
                         )
    add1_Button.pack(side=LEFT)
    add1_Button.pack_forget()
    if data['add1']:
        add1_Button.pack(side=LEFT)
    
    f2_button = Frame(f2,
               bg = data['background'],# 背景色
               )
    f2_button.pack()
    global random_roll_call_Button
    random_roll_call_Button = Button(f2_button,
               text="随机点名",
               bg = data['buttonbg'],# 按钮背景色
               font=(data['font'], 20),         # 字体和字体大小
               command=random_roll_call,
               )
    random_roll_call_Button.pack(side=LEFT) 
    
    global start_pause_Button
    start_pause_Button = Button(f2_button,# 开始暂停
               text="开始点名",
               bg = data['buttonbg'],# 按钮背景色
               font=(data['font'], 20),         # 字体和字体大小
               command=start_pause,
               )
    start_pause_Button.pack(side=LEFT)
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
    if(data['hide_unnecessary']):
        f3.pack_forget()
    
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

    bhelp = Button(f3,
         text="帮助",
         # image=phelp,#加入图片
         # bg = data['background'],# 按钮背景色
         bg = data['buttonbg'],# 按钮背景色
         # bd=0,# 按钮边框的大小，默认为2个像素
         font=(data['font'], 12),         # 字体和字体大小
         command=show_help,
         )
    bhelp.pack(side=RIGHT)
    

    # 窗口居中显示
    lname["text"] = "中文名"
    window.update()
    screenwidth = window.winfo_screenwidth()  # 获取显示屏宽度
    screenheight = window.winfo_screenheight()  # 获取显示屏高度
    width = window.winfo_reqwidth()
    height = window.winfo_reqheight()
    window.geometry("%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2) )
    lname["text"] = ""
    
    # window.protocol("WM_DELETE_WINDOW", save_exit)
    window.wm_attributes("-alpha", data['-alpha'])        # 透明度(0.0~1.0)
    # window.wm_attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
    window.wm_attributes("-topmost", data['-topmost'])     # 永远处于顶层    topmost
    window.bind("<Button-3>", lambda event : set_up())                 # 绑定鼠标右键
    # win.bind("<Button-3>", lambda event : set_up())                 # 绑定鼠标右键
    # fname.bind("<Button-3>", lambda event : set_up())                 # 绑定鼠标右键
    # lname.bind("<Button-3>", lambda event : set_up())                 # 绑定鼠标右键
    # f2.bind("<Button-3>", lambda event : set_up())                 # 绑定鼠标右键
    def root_key_event(event):
        # print(f"事件触发键盘输入:{event.char},对应的ASCII码:{event.keycode}")
        if(event.char == 's' or event.char == 'S'):
            set_up()
        elif(event.char == 'h' or event.char == 'H'):
            show_help()
    window.bind("<Key>", root_key_event)
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
    
    if(len(data['names']) == 0):
        first_read() #第一次（启动时）读取姓名
    if(len(data['havenames']) == 0):
        data['havenames'] = data['names'].copy()
    # else:
    #     global names
    #     names = data['names']
    root() # 显示主窗口
    
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
    
