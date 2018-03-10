#!/usr/bin/env python
#coding=utf-8
import commands
import sys
from Tkinter import *
import tkFileDialog


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)

def selectPath():
    path_ = tkFileDialog.askopenfilename()
    path_ = path_.replace(" ","\ ")
    path.set(path_)
    global uuid
    global dSYMName
    reload(sys)
    sys.setdefaultencoding('utf-8')
    dSYMName = commands.getoutput("cd " + path_ +" && cd dSYMs && ls")
    id = commands.getoutput("dwarfdump --uuid " + path_ + "/dSYMs/" +dSYMName)
    list = id.split()
    uuid.set(list[0]+list[1])
    print uuid

def analysys():
    print dSYMName
    print path.get()
    print vmaddr.get()
    print crashaddr.get()
    name = commands.getoutput("cd "+ path.get()+"&& cd dSYMs/"+dSYMName+"/Contents/Resources/DWARF && ls")
    print name
    error = commands.getoutput("cd "+ path.get()+"&& cd dSYMs/"+dSYMName+"/Contents/Resources/DWARF" + " && atos -o "+name +" -arch "+archiveType.get() +" -l "+vmaddr.get() +" "+crashaddr.get())
    errorMessage.set(error)

root = Tk()
root.title('计算crash位置')
center_window(root, 300, 240)
root.maxsize(900, 700)
root.minsize(700, 500)

dSYMName = "";
uuid = StringVar()
path = StringVar()
archiveType = StringVar()
vmaddr = StringVar()
crashaddr = StringVar()
errorMessage = StringVar()
Label(root,text="选择xcarchive文件:").place(x = 5, y = 15,width = 120, height = 15)
Entry(root, textvariable=path).place(x = 130, y = 10, width = 400, height = 30)
Button(root, text="路径选择", command = selectPath).place(x=535, y = 10,width = 120, height = 30)
Label(root,text="archive文件对应的编译类型:").place(x = 5, y = 55, width = 175, height = 15)
Entry(root, textvariable=archiveType).place(x = 185, y = 50, width = 130, height = 30)
Label(root,text="选择xcarchive的 uuid:").place(x = 5, y = 90,width = 145, height = 15)
Entry(root, textvariable=uuid).place(x = 5, y = 110, width = 400, height = 30)
Label(root,text="请输入运行的起始地址:").place(x = 5, y = 155,width = 150, height = 15)
Entry(root, textvariable=vmaddr).place(x = 5, y = 175, width = 690,height=30)
Label(root,text="请输入运行时崩溃地址:").place(x = 5, y = 215,width = 150, height = 15)
Entry(root, textvariable=crashaddr).place(x = 5, y = 235, width = 690,height=30)
Button(root, text="分析", command = analysys).place(x=5, y = 275,width = 690, height = 30)
Label(root,text="出错的地方:").place(x = 5, y = 315,width = 80, height = 15)
Entry(root, textvariable=errorMessage).place(x = 5, y = 335, width = 690, height = 120)

root.mainloop()


