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
    'verson': [1, 1, 0, 1],
    'time': '2020-10-04 11:42:22',
    'size': '''
    win32版zip压缩：7.82MB
    win32自解压版：7.95MB
    python源码版zip压缩：16.6KB(需要安装Python3.x)''',
    'update-content': '第一个随机点名的发布版',
    'url': ['''蓝奏云win32版zip压缩：https://www.lanzoux.com/iDxAPh5o8od
蓝奏云win32自解压版：https://www.lanzoux.com/i6P9Sh5nzdi
蓝奏云python源码版zip压缩：https://www.lanzoux.com/iVRY6h5orra (需要安装Python3.x)'''],
}

b = json.dumps(a)

print(b)

with open('update.json', 'w') as f:
    f.write(b)