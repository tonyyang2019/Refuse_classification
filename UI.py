import tkinter as tk
import tkinter.filedialog as fd  #必加的模块
from refuse_classification import classification

root = tk.Tk()
root.title('智能垃圾识别系统')
root.geometry('350x300')

def callback():
    fileName = fd.askopenfilename()  #tkinter.filedialog的函数
    return fileName

def a():
    try:
        data = classification(callback())
        x = data['物品名称'] + ":" + data['垃圾类别']
        A = tk.Label(root, text=x, font=('Arial', 12))
        A.pack()
    except:
        x = "无法识别垃圾类别"
        A = tk.Label(root, text=x, font=('Arial', 12))
        A.pack()


tk.Button(root,text="识别",font=('Arial', 12),command=a,width=15, height=2,).pack()
tk.mainloop()