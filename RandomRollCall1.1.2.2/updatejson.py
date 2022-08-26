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
    'verson': [1, 1, 2, 2],
    'time': '2022/8/27 0:22:29',
    'size': '''
    单文件版zip压缩7.47 MB(解压后约为8.18 MB，可能运行较慢)
    多文件版zip压缩7.44 MB(解压后约为17.8 MB)
    Python源码版zip压缩32.1 KB(解压后约为98.2 KB，需要安装Python3.8)''',
    'update-content': '''
    1、解决了名字长短不一导致窗口时大时小的问题
    2、启动窗口居于屏幕中间
    3、主窗口大小可被用户调节
    4、优化了用户体验
    5、修复了已知BUG''',
    'url': ['''单文件版zip压缩7.47 MB(解压后约为8.18 MB，可能运行较慢)：
蓝奏云 https://www.lanzout.com/iPd0g0acg0dc

多文件版zip压缩7.44 MB(解压后约为17.8 MB)：
蓝奏云 https://www.lanzout.com/ideew0acg0kj

Python源码zip压缩32.1 KB(解压后约为98.2 KB，需要安装Python3.8)：
蓝奏云 https://www.lanzout.com/ixt9x0acg0sh

官网：https://xkk1.github.io/program/randomrollcall/
GitHub开源地址：https://github.com/xkk1/RandomRollCall
'''],
}

b = json.dumps(a)

print(b)

with open('update.json', 'w') as f:
    f.write(b)
