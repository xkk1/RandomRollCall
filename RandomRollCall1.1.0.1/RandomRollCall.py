from tkinter import messagebox # 对话框
from traceback import format_exc #用于精准的获取错误异常


if __name__ == '__main__':
    try:
        import program # 导入随机点名入口模块
        program.main.main() # 执行入口函数
    except:
        messagebox.showerror(
                title = '程序出错！',
                message='程序出现未知错误！请联系制作者(QQ(小喾苦):3434623263 Q群(随机点名):681032320)\n%s' % (format_exc() ))
        print(format_exc())