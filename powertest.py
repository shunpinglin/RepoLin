import tkinter as tk
import time

def start_loop():
    label.config(text="計算中...")
    root.update()
    start_time = time.time()
    for i in range(40000):
        for j in range(40000):
            pass  # 空操作
    elapsed = time.time() - start_time
    label.config(text=f"執行時間：{elapsed:.2f} 秒")

root = tk.Tk()
root.title("40000x40000 遍歷計時")

button = tk.Button(root, text="開始", command=start_loop)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()