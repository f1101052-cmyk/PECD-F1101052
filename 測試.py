#第二版
import tkinter as tk
from tkinter import messagebox

# 遊戲類別
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("OOXX 遊戲")

        # 遊戲狀態
        self.board = [""] * 9  # 棋盤 3x3
        self.current_player = "X"
        
        # 建立棋盤按鈕
        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text="", width=10, height=3, font=("Arial", 20),
                               command=lambda i=i: self.click_button(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        # 重新開始按鈕
        self.restart_button = tk.Button(root, text="重新開始", width=10, height=2, font=("Arial", 14), command=self.restart)
        self.restart_button.grid(row=3, column=0, columnspan=3)

    def click_button(self, index):
        # 若該格已經有玩家選擇，則不進行操作
        if self.board[index] != "":
            return

        # 更新棋盤和按鈕
        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)

        # 檢查遊戲是否結束
        if self.check_winner():
            messagebox.showinfo("遊戲結束", f"玩家 {self.current_player} 贏了!")
            self.reset_board()
        elif "" not in self.board:
            messagebox.showinfo("遊戲結束", "平手！")
            self.reset_board()
        else:
            # 換下一位玩家
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # 檢查所有可能的勝利組合
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 橫向
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 縱向
            [0, 4, 8], [2, 4, 6]  # 斜向
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_board(self):
        # 重置棋盤
        for i in range(9):
            self.board[i] = ""
            self.buttons[i].config(text="")
        self.current_player = "X"

    def restart(self):
        # 重新開始遊戲
        self.reset_board()

# 建立視窗
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()


