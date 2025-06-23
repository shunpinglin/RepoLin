import tkinter as tk
from tkinter import messagebox
import random

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("猜數字遊戲")
        self.master.geometry("300x200")

        self.target = random.randint(1, 20)

        self.label = tk.Label(master, text="請猜一個 1 到 20 的數字")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="確認！", command=self.check_guess)
        self.button.pack(pady=5)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.restart_button = tk.Button(master, text="重新開始", command=self.restart_game)
        self.restart_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            #self.entry.delete(0, tk.END)  # 每次判斷後立即清空輸入區
            if guess < 1 or guess > 20:
                self.result_label.config(text="請輸入 1 到 20 的數字")
                return

            if guess < self.target:
                self.result_label.config(text="太小了！")
            elif guess > self.target:
                self.result_label.config(text="太大了！")
            else:
                self.result_label.config(text="恭喜你，猜對了！")
                messagebox.showinfo("成功", "你猜對了！")
        except ValueError:
            #self.entry.delete(0, tk.END)  # 非法輸入時也清空
            self.result_label.config(text="請輸入有效的整數")

    def restart_game(self):
        self.target = random.randint(1, 20)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
