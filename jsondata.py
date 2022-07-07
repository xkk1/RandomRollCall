'''
用于对数据进行保存
函数:
    check_code(data):'生成校验码'
    test_check(data):'检验校验码是否正确,返回bool值'
    save_data(data, json_data_file):'保存数据到文件'
    read_data(data, json_data_file):'读数据'
变量:
        # json数据文件名称/地址
    json_data_file = 'data.json'
    # 初始化数据
    data = {
        'program_name': 'Python program',#程序名
        'program_path': sys.argv[0],# 程序路径
        'verson': [0, 0, 0, 0],# 版本号
        'autor': '小喾苦',# 制作人
        'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),# 时间
        'check_code': '',# 校验码
        }
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
import time
'''
# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
'''
# 使用MD5加密生成校验码
import hashlib
'hashlib.md5(string.encode()).hexdigest()'
# 用于获取argv
import sys
'print(sys.argv)'
# 用于文件操作
import os.path
# 对话框
from tkinter import messagebox

def check_code(dat):
    # 浅拷贝，防止源数据效验码丢失
    data = dat.copy()
    '生成校验码'
    # 尝试删除数据文件原先的校验码
    try:
        data.pop('check_code')
    except:
        pass
    # 将数据改为以字符串格式
    data = repr(data)
    # 校验码是MD5加密后的结果
    check = hashlib.md5(data.encode()).hexdigest()
    # 返回校验码
    return check

def test_check(data):
    '检验校验码是否正确,返回bool值'
    # 尝试获取原校验码
    try:
        checkcode = data['check_code']
    except:
        return False
    # 获取校验码
    check = check_code(data)
    if checkcode == check:
        return True
    else:
        return False

def save_data(data, json_data_file):
    '保存数据到文件'
    # 更新校验码
    data['check_code'] = check_code(data)
    # 写入 JSON 数据
    with open(json_data_file, 'w') as f:
        json.dump(data, f)
    return data

def read_data(data, json_data_file):
    '读数据'
    # 判断数据文件是否存在
    if os.path.isfile(json_data_file):
        with open(json_data_file, 'r') as f:
            new_data = json.load(f)
            # print(new_data)
        if test_check(new_data):
            # print(new_data)
            return new_data
        else:
            messagebox.showerror(title = '数据受损，无法读取！',message='数据受损，无法读取！\n请不要修改数据！')
            save_data(data, json_data_file)
            return data
    else:
        # print("文件")
        save_data(data, json_data_file)
        return data


# json数据文件名称/地址
json_data_file = 'data.json'
# 初始化数据
data = {
    'program_name': 'Python program',#程序名
    'program_path': sys.argv[0],# 程序路径
    'verson': [0, 0, 0, 0],# 版本号
    'autor': '小喾苦',# 制作人
    'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),# 时间
    'check_code': '',# 校验码
}


if __name__ == '__main__':
    # json_str = json.dumps(data)
    # print ("Python 原始数据：", repr(data))
    # print ("JSON 对象：", json_str)
    
    '''
    "文件操作"
    # 写入 JSON 数据
    with open('data.json', 'w') as f:
        json.dump(data, f)
    '''
    data = save_data(data, json_data_file)
    # 读取数据
    with open('data.json', 'r') as f:
        data = json.load(f)
    

    print(data)
    print(test_check(data))
