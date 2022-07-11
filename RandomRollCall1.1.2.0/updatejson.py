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

a = {
    'verson': [1, 1, 1, 0],
    'time': '2022/7/7 9:34:11',
    'size': '''
    win32单文件版zip压缩：7.48 MB(解压后约为8.18 MB，可能运行较慢)
    win32多文件版zip压缩：8.36 MB(解压后约为18.7 MB)
    python源码版zip压缩：29.6 KB(解压后约为86.5 KB，需要安装Python3.8)''',
    'update-content': '''
    1、修复读取姓名文件时读取失败的问题
    2、加入文件编码自动识别、选择功能
    3、增加姓名去重功能
    4、增加字体选择功能
    5、增加预览功能
    6、将字体大小最大值改为500
    7、优化了信息显示窗口
    8、优化了检查更新功能
    9、增加右键复制、粘贴等功能
    10、优化了程序报错功能''',
    'url': ['''蓝奏云单文件版zip压缩：
https://www.lanzout.com/i9tUP07hlf6h
文件大小：7.48 MB(解压后约为8.18 MB，可能运行较慢)

蓝奏云多文件版zip压缩：
https://www.lanzout.com/itZF407hlfde
文件大小：8.36 MB(解压后约为18.7 MB)

蓝奏云python源码版zip压缩：
https://www.lanzout.com/iWixE07hlfef
文件大小：29.6 KB(解压后约为86.5 KB，需要安装Python3.8)

GitHub开源地址：
https://github.com/xkk1/RandomRollCall
'''],
}

b = json.dumps(a)

print(b)

with open('update.json', 'w') as f:
    f.write(b)
