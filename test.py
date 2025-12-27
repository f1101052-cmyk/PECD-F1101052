#第三版
import tkinter as tk
from tkinter import messagebox
import random

class MiyazakiTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("森林精靈井字遊戲")
        self.root.configure(bg="#F5F1E8")

        self.player = "🌱"
        self.computer = "🐾"
        self.board = [""] * 9
        self.difficulty = None

        self.create_start_menu()

    # ===== 開始選單 =====
    def create_start_menu(self):
        self.clear_window()

        title = tk.Label(
            self.root,
            text="🌿 森林精靈井字遊戲 🌿",
            font=("Helvetica", 20, "bold"),
            bg="#F5F1E8"
        )
        title.pack(pady=20)

        tk.Label(
            self.root,
            text="請選擇難度",
            font=("Helvetica", 14),
            bg="#F5F1E8"
        ).pack(pady=10)

        tk.Button(
            self.root, text="簡單 🌤",
            font=("Helvetica", 14),
            width=12,
            command=lambda: self.start_game("easy")
        ).pack(pady=5)

        tk.Button(
            self.root, text="困難 🌑",
            font=("Helvetica", 14),
            width=12,
            command=lambda: self.start_game("hard")
        ).pack(pady=5)

    # ===== 開始遊戲 =====
    def start_game(self, difficulty):
        self.difficulty = difficulty
        self.clear_window()
        self.board = [""] * 9
        self.buttons = []

        frame = tk.Frame(self.root, bg="#F5F1E8")
        frame.pack()

        for i in range(9):
            btn = tk.Button(
                frame,
                text="",
                font=("Helvetica", 24),
                width=4,
                height=2,
                bg="#FFFFFF",
                command=lambda i=i: self.player_move(i)
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        tk.Button(
            self.root,
            text="重新開始 🍃",
            font=("Helvetica", 12),
            command=self.create_start_menu
        ).pack(pady=15)

    # ===== 玩家行動 =====
    def player_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)

            if self.check_winner(self.player):
                messagebox.showinfo("結果", "🌱 你贏了！森林為你歡呼")
                self.create_start_menu()
                return

            if "" not in self.board:
                messagebox.showinfo("結果", "平手～森林保持平衡")
                self.create_start_menu()
                return

            self.root.after(400, self.computer_move)

    # ===== 電腦行動 =====
    def computer_move(self):
        if self.difficulty == "easy":
            move = random.choice([i for i in range(9) if self.board[i] == ""])
        else:
            move = self.smart_move()

        self.board[move] = self.computer
        self.buttons[move].config(text=self.computer)

        if self.check_winner(self.computer):
            messagebox.showinfo("結果", "🐾 森林精靈獲勝！")
            self.create_start_menu()

    # ===== 困難模式 AI =====
    def smart_move(self):
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.computer
                if self.check_winner(self.computer):
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.player
                if self.check_winner(self.player):
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        return random.choice([i for i in range(9) if self.board[i] == ""])

    # ===== 勝利判斷 =====
    def check_winner(self, symbol):
        wins = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        return any(all(self.board[i] == symbol for i in combo) for combo in wins)

    # ===== 清畫面 =====
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# 啟動程式
root = tk.Tk()
root.resizable(False, False)
game = MiyazakiTicTacToe(root)
root.mainloop()

