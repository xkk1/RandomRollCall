#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def _main():
    try:
        from xkkRandomRollCall.show_information import show_error
        # show_error()
    except Exception:
        print("程序报错功能导入异常！")
        try:
            from tkinter import messagebox # 对话框
            from traceback import format_exc #用于精准的获取错误异常
            messagebox.showerror(
                title = '程序报错功能导入异常！',
                message='程序报错功能导入异常！\n\
    https://xkk1.github.io/program/randomrollcall/\n请联系制作者(QQ(小喾苦):3434623263 \
    Q群(随机点名):681032320)\n%s' % (format_exc() ))
            def show_error():
                messagebox.showerror(
                   title = '程序出错！',
                   message='程序出现未知错误！程序报错功能异常！请联系制作者(QQ(小喾苦):3434623263 \
    Q群(随机点名):681032320)\n%s' % (format_exc() ))
        except Exception:
            print("您的 Python 版本太低或不支持Tkinter无法正常运行该程序，请用 Python3.8 及其以上的 Python！")
            input("按回车键退出 . . .")
            exit()
    try:
        from xkkRandomRollCall import main # 导入随机点名入口模块
        main.main() # 执行入口函数
    except Exception:
        show_error()


if __name__ == '__main__':
    _main()
