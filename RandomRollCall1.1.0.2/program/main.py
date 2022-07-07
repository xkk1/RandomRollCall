# from tkinter import * # 图形界面
# from tkinter import messagebox # 对话框
from tkinter import filedialog #文件操作
# from sys import exc_info # 用于抛出异常
from traceback import format_exc #用于精准的获取错误异常
from os.path import exists # 文件、路径是否存在
from random import sample # 从列表里随机抽取
from random import randint # 生成随机数字
from tkinter import colorchooser # 用于选择颜色

try:
    from .jsondata import * # 用于保存数据
    from .updata import * # 用于文件更新
except:
    from jsondata import * # 用于保存数据
    from updata import * # 用于文件更新
# updata([0,0,0,0])

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

# json数据文件名称/地址
json_data_file = 'data.json'
# 初始化数据
data = {
    'cumulative': 0, # 累计人数
    'font_size': 100, # 字号
    'file': 'names.txt', # 姓名文件
    'background': "#f0f0f0", # 背景色
    'buttonbg': "#f0f0f0", # 按钮背景色
    '-alpha': 1.0, # 透明度
    '-topmost': False, # 是否置于顶层
    'program_name': 'RandomRollCall', #程序名
    'program_path': sys.argv[0], # 程序路径
    'verson': [1, 1, 0, 2], # 版本号
    'autor': '小喾苦', # 制作人
    'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), # 时间
    'check_code': '', # 校验码
}
data_default = data.copy() # 数据默认值
bbh = "%i.%i.%i.%i"%tuple([data['verson'][i] for i in range(4)]) # 版本号

colors = '''#FFB6C1 LightPink 浅粉红
#FFC0CB Pink 粉红
#DC143C Crimson 深红/猩红
#FFF0F5 LavenderBlush 淡紫红
#DB7093 PaleVioletRed 弱紫罗兰红
#FF69B4 HotPink 热情的粉红
#FF1493 DeepPink 深粉红
#C71585 MediumVioletRed 中紫罗兰红
#DA70D6 Orchid 暗紫色/兰花紫
#D8BFD8 Thistle 蓟色
#DDA0DD Plum 洋李色/李子紫
#EE82EE Violet 紫罗兰
#FF00FF Magenta 洋红/玫瑰红
#FF00FF Fuchsia 紫红/灯笼海棠
#8B008B DarkMagenta 深洋红
#800080 Purple 紫色
#BA55D3 MediumOrchid 中兰花紫
#9400D3 DarkViolet 暗紫罗兰
#9932CC DarkOrchid 暗兰花紫
#4B0082 Indigo 靛青/紫兰色
#8A2BE2 BlueViolet 蓝紫罗兰
#9370DB MediumPurple 中紫色
#7B68EE MediumSlateBlue 中暗蓝色/中板岩蓝
#6A5ACD SlateBlue 石蓝色/板岩蓝
#483D8B DarkSlateBlue 暗灰蓝色/暗板岩蓝
#E6E6FA Lavender 淡紫色/熏衣草淡紫
#F8F8FF GhostWhite 幽灵白
#0000FF Blue 纯蓝
#0000CD MediumBlue 中蓝色
#191970 MidnightBlue 午夜蓝
#00008B DarkBlue 暗蓝色
#000080 Navy 海军蓝
#4169E1 RoyalBlue 皇家蓝/宝蓝
#6495ED CornflowerBlue 矢车菊蓝
#B0C4DE LightSteelBlue 亮钢蓝
#778899 LightSlateGray 亮蓝灰/亮石板灰
#708090 SlateGray 灰石色/石板灰
#1E90FF DodgerBlue 闪兰色/道奇蓝
#F0F8FF AliceBlue 爱丽丝蓝
#4682B4 SteelBlue 钢蓝/铁青
#87CEFA LightSkyBlue 亮天蓝色
#87CEEB SkyBlue 天蓝色
#00BFFF DeepSkyBlue 深天蓝
#ADD8E6 LightBlue 亮蓝
#B0E0E6 PowderBlue 粉蓝色/火药青
#5F9EA0 CadetBlue 军兰色/军服蓝
#F0FFFF Azure 蔚蓝色
#E0FFFF LightCyan 淡青色
#AFEEEE PaleTurquoise 弱绿宝石
#00FFFF Cyan 青色
#00FFFF Aqua 浅绿色/水色
#00CED1 DarkTurquoise 暗绿宝石
#2F4F4F DarkSlateGray 暗瓦灰色/暗石板灰
#008B8B DarkCyan 暗青色
#008080 Teal 水鸭色
#48D1CC MediumTurquoise 中绿宝石
#20B2AA LightSeaGreen 浅海洋绿
#40E0D0 Turquoise 绿宝石
#7FFFD4 Aquamarine 宝石碧绿
#66CDAA MediumAquamarine 中宝石碧绿
#00FA9A MediumSpringGreen 中春绿色
#F5FFFA MintCream 薄荷奶油
#00FF7F SpringGreen 春绿色
#3CB371 MediumSeaGreen 中海洋绿
#2E8B57 SeaGreen 海洋绿
#F0FFF0 Honeydew 蜜色/蜜瓜色
#90EE90 LightGreen 淡绿色
#98FB98 PaleGreen 弱绿色
#8FBC8F DarkSeaGreen 暗海洋绿
#32CD32 LimeGreen 闪光深绿
#00FF00 Lime 闪光绿
#228B22 ForestGreen 森林绿
#008000 Green 纯绿
#006400 DarkGreen 暗绿色
#7FFF00 Chartreuse 黄绿色/查特酒绿
#7CFC00 LawnGreen 草绿色/草坪绿
#ADFF2F GreenYellow 绿黄色
#556B2F DarkOliveGreen 暗橄榄绿
#9ACD32 YellowGreen 黄绿色
#6B8E23 OliveDrab 橄榄褐色
#F5F5DC Beige 米色/灰棕色
#FAFAD2 LightGoldenrodYellow 亮菊黄
#FFFFF0 Ivory 象牙色
#FFFFE0 LightYellow 浅黄色
#FFFF00 Yellow 纯黄
#808000 Olive 橄榄
#BDB76B DarkKhaki 暗黄褐色/深卡叽布
#FFFACD LemonChiffon 柠檬绸
#EEE8AA PaleGoldenrod 灰菊黄/苍麒麟色
#F0E68C Khaki 黄褐色/卡叽布
#FFD700 Gold 金色
#FFF8DC Cornsilk 玉米丝色
#DAA520 Goldenrod 金菊黄
#B8860B DarkGoldenrod 暗金菊黄
#FFFAF0 FloralWhite 花的白色
#FDF5E6 OldLace 老花色/旧蕾丝
#F5DEB3 Wheat 浅黄色/小麦色
#FFE4B5 Moccasin 鹿皮色/鹿皮靴
#FFA500 Orange 橙色
#FFEFD5 PapayaWhip 番木色/番木瓜
#FFEBCD BlanchedAlmond 白杏色
#FFDEAD NavajoWhite 纳瓦白/土著白
#FAEBD7 AntiqueWhite 古董白
#D2B48C Tan 茶色
#DEB887 BurlyWood 硬木色
#FFE4C4 Bisque 陶坯黄
#FF8C00 DarkOrange 深橙色
#FAF0E6 Linen 亚麻布
#CD853F Peru 秘鲁色
#FFDAB9 PeachPuff 桃肉色
#F4A460 SandyBrown 沙棕色
#D2691E Chocolate 巧克力色
#8B4513 SaddleBrown 重褐色/马鞍棕色
#FFF5EE Seashell 海贝壳
#A0522D Sienna 黄土赭色
#FFA07A LightSalmon 浅鲑鱼肉色
#FF7F50 Coral 珊瑚
#FF4500 OrangeRed 橙红色
#E9967A DarkSalmon 深鲜肉/鲑鱼色
#FF6347 Tomato 番茄红
#FFE4E1 MistyRose 浅玫瑰色/薄雾玫瑰
#FA8072 Salmon 鲜肉/鲑鱼色
#FFFAFA Snow 雪白色
#F08080 LightCoral 淡珊瑚色
#BC8F8F RosyBrown 玫瑰棕色
#CD5C5C IndianRed 印度红
#FF0000 Red 纯红
#A52A2A Brown 棕色
#B22222 FireBrick 火砖色/耐火砖
#8B0000 DarkRed 深红色
#800000 Maroon 栗色
#FFFFFF White 纯白
#F5F5F5 WhiteSmoke 白烟
#DCDCDC Gainsboro 淡灰色
#D3D3D3 LightGrey 浅灰色
#C0C0C0 Silver 银灰色
#A9A9A9 DarkGray 深灰色
#808080 Gray 灰色
#696969 DimGray 暗淡灰
#000000 Black 纯黑'''

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
    string = ''
    global data
    global f21
    global f31
    global havenames
    try:
        name_file = vname_file.get()
        if not exists(name_file):
            b = False
            string += '未找到文件,文件“%s”不存在！' % name_file
        else:
            f = open(name_file, 'r')
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
            names = list(set(names)) # 实现姓名查重功能(会自动排序)
            
            data['file'] = name_file
            
            print(names)
            # for j in names:
            #     print(j)
    except:
        b = False
        string += '读取文件“%s”失败！\n' % vname_file.get() #, format_exc())
    
    try:
        f21['bg'] = vbackground.get()
        data['background'] = vbackground.get()
    except:
        b = False
        string += '未知背景颜色“%s”!\n' % vbackground.get()
    
    try:
        f31['bg'] = vbuttonbg.get()
        data['buttonbg'] = vbuttonbg.get()
    except:
        b = False
        string += '未知按钮颜色“%s”!\n' % vbuttonbg.get()
    
    if b:
        data['background'] = vbackground.get()
        data['buttonbg'] = vbuttonbg.get()
        data['font_size'] = int(var_font_size_Scale.get())
        data['-alpha'] = float(var__alpha_Scale.get())
        data['-topmost'] = var__topmost_Checkbutton.get()
        havenames = []
        # 保存数据
        save_data(data, json_data_file)
        wset_up.destroy()# 销毁设置窗口
    else:
        messagebox.showerror(title='数据错误！',message=string)

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

def first_read():
    '第一次（启动时）读姓名'
    global names
    try:
        name_file = data['file']
        if not exists(name_file):
            pass
        else:
            f = open(name_file, 'r')
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
            names = list(set(names)) # 实现姓名查重功能
            
            data['file'] = name_file
            
            print(names)
            # for j in names:
            #     print(j)
    except:
        pass
    
    if names == []: # 如果没有读到任何姓名
        # names = ['孙八', '张三', '吴十', '刘一', '李四', '杨九', '陈二', '赵六', '钱七', '王五']
        print('暂无姓名！')

def change_background_color(color):
    '及时改变背景颜色'
    # print('change_background_color')
    global f21
    try:
        f21['bg'] = color
    except:
        pass
    return True

def change_buttonbg_color(color):
    '及时改变按钮颜色'
    global f31
    try:
        f31['bg'] = color
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
    
    if data['font_size'] < 331:
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
    print('开始了')
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

def view_colors():
    window_view_colors = Tk()
    window_view_colors.title("随机点名——部分颜色代码")
    try:# 尝试打开设置图标
        window_view_colors.iconbitmap('.\\program\\image\\RandomRollCall.ico')
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
        wset_up.iconbitmap('.\\program\\image\\RandomRollCall.ico')
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
    
    
    win = Frame(wset_up,
                #bg = data['background'],# 背景色
                )
    win.pack()
    
    f1 = Frame(win,
               #bg = data['background'],# 背景色
               )
    f1.pack(fill=X,padx=5,pady=5)
    
    l1 = Label(f1, 
        text="姓名文件：",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l1.pack(side=LEFT)    # 固定窗口位置
    ename_file = Entry(f1,# 姓名文件名输入框
               textvariable=vname_file,
               #bg=data['background'],          # 背景颜色
               width=30,# 宽度
               )
    ename_file.pack(side=LEFT)
    bchoice = Button(f1,
               text="选择\n文件",
               #bg = data['buttonbg'],# 按钮背景色
               font=('宋体', 10),         # 字体和字体大小
               command=choice,
               #width=25, height=25          # 标签长宽
               )
    bchoice.pack(side=RIGHT)
    
    
    """
    obj['state'] = DISABLED   ###禁用
    obj['state'] = NORMAL     ###重新激活
    """
    f2 = Frame(win,
               #bg = data['background'],# 背景色
               )
    f2.pack(fill=X,padx=5,pady=5)
    
    l2 = Label(f2, 
        text="背景颜色：",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        #fg="red",
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l2.pack(side=LEFT)    # 固定窗口位置
    # l2['state'] = DISABLED   ###禁用
    
    change_background_color_CMD = wset_up.register(change_background_color) # 包装起来
    ebackground = Entry(f2,# 姓名文件名输入框
               textvariable=vbackground,#可变本文
               #bg=data['background'],          # 背景颜色
               width=10,# 宽度
               validate='key', # 启用验证，当输入框被编辑时验证
               validatecommand=(change_background_color_CMD, '%P'),
               )
    ebackground.pack(side=LEFT)
    # ebackground['state'] = DISABLED   ###禁用
    f21 = Frame(f2,
               bg = data['background'],# 背景色
               width=135,
               height=25,
               )
    f21.pack(side=LEFT)
    
    colorchooser_background_color_Button = Button(f2,
        text="选择",
        command = colorchooser_change_background_color,
        font=('宋体', 12),         # 字体和字体大小
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
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    buttonbg_color_Label.pack(side=LEFT)    # 固定窗口位置
    # l3['state'] = DISABLED   ###禁用
    
    change_buttonbg_color_CMD = wset_up.register(change_buttonbg_color) # 包装起来
    ebuttonbg = Entry(f3,# 姓名文件名输入框
               textvariable=vbuttonbg,#可变本文
               #bg=data['background'],          # 背景颜色
               width=10,# 宽度
               validate='key', # 启用验证，当输入框被编辑时验证
               validatecommand=(change_buttonbg_color_CMD, '%P'),
               )
    ebuttonbg.pack(side=LEFT)
    # ebuttonbg['state'] = DISABLED   ###禁用
    f31 = Frame(f3,
               bg = data['buttonbg'],# 背景色
               width=135,
               height=25,
               )
    f31.pack(side=LEFT)
    
    colorchooser_buttonbg_color_Button = Button(f3,
        text="选择",
        command = colorchooser_change_buttonbg_color,
        font=('宋体', 12),         # 字体和字体大小
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
                     text='置于顶层', 
                     variable=var__topmost_Checkbutton, 
                     onvalue=True, 
                     offvalue=False,
                     font=('宋体', 12),         # 字体和字体大小
                     #command=no_repeat_roll_call,
                     )
    _topmost_Checkbutton.pack(side=LEFT)
    view_colors_Button = Button(f4,
               # text="确定",
               text="查看部分颜色代码",
               font=('宋体', 12),        # 字体和字体大小
               #bg=data['buttonbg'],
               command=view_colors,
               )
    view_colors_Button.pack(padx=0,pady=0,side=RIGHT) # fill=X,
    
    font_size_Frame = Frame(win) # 字体大小
    font_size_Frame.pack()
    font_size_Label = Label(font_size_Frame, 
        text="字体\n大小",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        #fg="red",
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    font_size_Label.pack(side=LEFT)    # 固定窗口位置
    global var_font_size_Scale
    var_font_size_Scale = StringVar()
    font_size_Scale = Scale(font_size_Frame,# 滑块
        from_ = 1,#设置最小值
        to = 335,#设置最大值
        orient = HORIZONTAL,#设置横向
        resolution=1,#设置步长
        tickinterval = 50,#设置刻度
        length = 300,# 设置像素
        variable = var_font_size_Scale,#绑定变量
        )
    font_size_Scale.pack(side=LEFT)    # 固定滑块位置
    var_font_size_Scale.set(str(data['font_size']))
    
    _alpha_Frame = Frame(win) # 透明度
    _alpha_Frame.pack()
    _alpha_Label = Label(_alpha_Frame, 
        text="主窗口\n透明度",    # 标签的文字
        #bg=data['background'],          # 背景颜色
        #fg="red",
        font=('宋体', 12),         # 字体和字体大小
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
               font=('宋体', 14),        # 字体和字体大小
               #bg=data['buttonbg'],
               command=save_changes,
               )
    bsave_changes.pack(side=LEFT,padx=5,pady=5)
    bcancel = Button(fb,
               text="取消",
               font=('宋体', 14),        # 字体和字体大小
               #bg=data['buttonbg'],
               command=wset_up.destroy,
               )
    bcancel.pack(side=LEFT,padx=5,pady=5)
    brestore_default = Button(fb,
               # text="确定",
               text="恢复默认",
               font=('宋体', 14),        # 字体和字体大小
               #bg=data['buttonbg'],
               command=restore_default,
               )
    brestore_default.pack(side=LEFT,padx=5,pady=5)
    bupdata = Button(fb,
               # text="确定",
               text="检查更新",
               font=('宋体', 14),        # 字体和字体大小
               #bg=data['buttonbg'],
               command=lambda: updata(data_default['verson']),
               )
    bupdata.pack(side=LEFT,padx=5,pady=5)
    
    
    
    wset_up.mainloop()           #循环消息，让窗口活起来
    root()

def root():
    '''显示主窗口'''
    global window
    # global data
    # print(data)
    window=Tk()
    window.title("随机点名V%i.%i.%i.%i"%tuple([data['verson'][i] for i in range(4)]))
    window.resizable(0,0)# 禁止调节窗口大小
    try:# 尝试打开设置图标
        window.iconbitmap('.\\program\\image\\RandomRollCall.ico')
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
                         font=('宋体', 12),         # 字体和字体大小
                         command=set_up# 命令
                         )
    else:# 否则正常显示
        bset_up = Button(f1,
                     text="设置",
                     bd=0,# 按钮边框的大小，默认为2个像素
                     bg = data['background'],# 按钮背景色
                     image=ppset_up,#加入图片
                     # compound = CENTER,#关键:设置为背景图片
                     font=('宋体', 12),         # 字体和字体大小
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
        font=('宋体', 12),         # 字体和字体大小
        command=set_up,# 命令
        )
    bset_up.pack(side=LEFT)
    
    no_repeat_roll_call_Checkbutton = Checkbutton(f1, 
                     bg = data['background'],# 背景色
                     text='不重复点名', 
                     variable=var_no_repeat_roll_call, 
                     onvalue=1, 
                     offvalue=0,
                     font=('宋体', 12),         # 字体和字体大小
                     command=no_repeat_roll_call,
                     )
    no_repeat_roll_call_Checkbutton.pack(side=LEFT)
    
    global reset_Button
    reset_Button = Button(f1,
           text="复位",
           bg=data['buttonbg'],         # 背景颜色
           font=('宋体', 12),         # 字体和字体大小
           command=reset,
           )
    reset_Button.pack(side=LEFT)
    reset_Button.pack_forget()
    
    global remaining_names_Lable
    remaining_names_Lable = Label(f1,
        # textvariable=v3,
        text='剩余姓名：'+str(len(names)-len(havenames))+'/'+str(len(names)),    # 标签的文字
        bg=data['background'],         # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    remaining_names_Lable.pack(side=LEFT) # 固定窗口位置
    remaining_names_Lable.pack_forget()

    
    
    '''
    l1 = Label(f1, 
               text="                             ",    # 标签的文字
               bg = data['background'],# 背景色
               font=('宋体', 12),         # 字体和字体大小
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
                         font=('宋体', 12),         # 字体和字体大小
                         command=help,
                         )
    else:# 否则正常显示
        bhelp = Button(f1,
                         text="帮助",
                         image=phelp,#加入图片
                         bg = data['background'],# 按钮背景色
                         bd=0,# 按钮边框的大小，默认为2个像素
                         font=('宋体', 12),         # 字体和字体大小
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
         font=('宋体', 12),         # 字体和字体大小
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
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l2.pack()    # 固定窗口位置
    '''
    global lname
    lname = Label(f2, 
        text='',    # 标签的文字
        bg = data['background'],# 背景色
        font=('黑体', data['font_size']),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    lname.pack()    # 固定窗口位置
    
    global random_roll_call_Button
    random_roll_call_Button = Button(f2,
               text="随机点名",
               bg = data['buttonbg'],# 按钮背景色
               font=('宋体', 20),         # 字体和字体大小
               command=random_roll_call,
               )
    random_roll_call_Button.pack()# side=LEFT
    
    global start_pause_Button
    start_pause_Button = Button(f2,# 开始暂停
               text="开始点名",
               bg = data['buttonbg'],# 按钮背景色
               font=('宋体', 20),         # 字体和字体大小
               command=start_pause,
               )
    start_pause_Button.pack()# side=LEFT
    '''
    l21 = Label(f2, 
        text="\n\n\n",    # 标签的文字
        bg = data['background'],# 背景色
        font=('宋体', 12),         # 字体和字体大小
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
               font=('宋体', 12),         # 字体和字体大小
               command=clearing,
               )
    clearing_Button.pack(side=LEFT)
    
    global cumulative_Label
    cumulative_Label = Label(f3, 
        # textvariable=v6,
        text="累计抽取人数："+str(data['cumulative']),    # 标签的文字
        bg = data['background'],# 背景色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    cumulative_Label.pack(side=LEFT)    # 固定窗口位置
    
    
    lnone = Label(f3, 
               text="                   ",    # 标签的文字
               bg = data['background'],# 背景色
               font=('宋体', 12),         # 字体和字体大小
               #width=15, height=2          # 标签长宽
               )
    lnone.pack(side=LEFT)    # 固定窗口位置
    
    
    reduce_font_size_Button = Button(f3,
               text="-",
               bg = data['buttonbg'],# 按钮背景色
               font=('宋体', 12),         # 字体和字体大小
               command=reduce_font_size
               )
    reduce_font_size_Button.pack(side=RIGHT)
    
    increase_font_size_Button = Button(f3,
               text="+",
               bg = data['buttonbg'],# 按钮背景色
               font=('宋体', 12),         # 字体和字体大小
               command=increase_font_size
               )
    increase_font_size_Button.pack(side=RIGHT)

    
    lzh = Label(f3, 
        text="字号：",    # 标签的文字
        bg = data['background'],# 背景色
        font=('宋体', 12),         # 字体和字体大小
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
    
