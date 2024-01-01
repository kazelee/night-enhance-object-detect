# coding=utf8
# python2.7 core program
'''
封装成一个类
!类中的属性要用self.使用
'''
import os
from time import sleep
# from Tkinter import *
from tkinter import *

class ListDir(object):
    def __init__(self, initdir=None):
        '''程序的主要显示框架'''
        self.top = Tk()
        self.label = Label(self.top, text='DirList v1.1')  # 显示应用名称
        self.label.pack()
        self.cwd = StringVar(self.top)

        self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))  # 显示查询的目录
        self.dirl.pack()

        self.dirfm = Frame(self.top)  # 列出目录的主要显示框，一个列表显示，一个滚动条
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
        self.dirsb.bind('<Double-1>', self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(fill=BOTH, side=LEFT)
        self.dirfm.pack()

        self.dirn = Entry(self.top, width=50, textvariable=self.cwd)  # 输入要选择的目录，相当于单行文本框
        self.dirn.bind('Return', self.doLs)
        self.dirn.pack()

        self.bfm = Frame(self.top)  # 按钮域 清除 列表 关闭
        self.clr = Button(self.bfm, text='Clear', command=self.clrDir, fg='white', bg='blue')
        self.ls = Button(self.bfm, text='List Dir', command=self.doLs, fg='white', bg='green')
        self.quit = Button(self.bfm, text='Quit', command=self.top.quit, fg='white', bg='red')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()

        if initdir:
            self.cwd.set(os.curdir)
            self.doLs()

    def clrDir(self, ev=None):
        '''清空目录'''
        self.cwd.set('')

    def setDirAndGo(self, ev=None):
        '''到达指定的目录，并且调用查看文件的dols'''
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLs()

    def doLs(self, ev=None):
        '''核心算法，列出文件目录'''
        error = ''
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir

        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ': no such dri'

        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.top.update()
            return

        self.cwd.set('FETCHING DIR CONTS...')
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)
        self.dirl.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)  # 当前目录 .
        self.dirs.insert(END, os.pardir)  # 父目录 ..
        for eachFile in dirlist:
            self.dirs.insert(END, eachFile)
            self.cwd.set(os.curdir)
            self.dirs.config(selectbackground='LightSkyBlue')


def main():
    ls = ListDir(os.curdir)
    mainloop()


if __name__ == '__main__':
    main()

'''
解释和解析：
最主要的方法就是os.listdir()
'''