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
    'verson': [1, 1, 3, 1],
    'time': '2023/1/22 00:00:00',
    'size': '''
    单文件版zip压缩7.47 MB(解压后约为8.18 MB，可能运行较慢)
    多文件版zip压缩7.44 MB(解压后约为17.8 MB)
    Python源码版zip压缩32.1 KB(解压后约为98.2 KB，需要安装Python3.8)''',
    'update-content': '''
    1. 点名的结果可以被保存
    2. 点名后窗口大小会根据姓名长短自行调节
    3. 增加了点名后窗口自动居中的功能
    4. 更科学的随机点名抽取动画
    5. 滚动点名支持不重复点名
    6. 新增设置、帮助的打开方式
    7. 优化了部分程序逻辑
    8. 优化主窗口布局''',
    'url': ['''单文件版zip压缩7.47 MB(解压后约为8.18 MB，可能运行较慢)：
蓝奏云 

多文件版zip压缩7.44 MB(解压后约为17.8 MB)：
蓝奏云 

Python源码zip压缩32.1 KB(解压后约为98.2 KB，需要安装Python3.8)：
蓝奏云 

官网：https://xkk1.github.io/program/randomrollcall/
GitHub开源地址：https://github.com/xkk1/RandomRollCall
'''],
}

b = json.dumps(a)

print(b)

with open('update.json', 'w') as f:
    f.write(b)
