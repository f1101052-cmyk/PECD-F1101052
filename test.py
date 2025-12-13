import tkinter as tk #匯入 tkinter 並命名為 tk
win = tk.Tk() #建立主視窗物件
win.geometry("400x300") #設定視窗大小為 400x300像素
win.title("視窗程式") #設定視窗標題




win.mainloop() #進入主事件迴圈

import tkinter as tk
from tkinter import messagebox

# ===== 功能函式 =====
def on_click():
    label.config(text="妳很漂亮！")

def show_about():
    messagebox.showinfo("About", "這是一個使用 Tkinter 建立的視窗程式範例。")

def close_window():
    root.destroy()

# ===== 建立主視窗 =====
root = tk.Tk()
root.title("Tkinter 視窗程式")
root.geometry("500x350")

# ===== 建立選單列 =====
menubar = tk.Menu(root)

# File 選單
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=close_window)
menubar.add_cascade(label="File", menu=file_menu)

# Help 選單
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

# ===== 主介面元件 =====
label = tk.Label(root, text="歡迎使用 Tkinter！", font=("Arial", 16))
label.pack(pady=30)

button = tk.Button(root, text="按我一下", font=("Arial", 14), command=on_click)
button.pack()

# ===== 主迴圈 =====
root.mainloop()
