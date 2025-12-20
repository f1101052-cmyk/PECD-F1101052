import tkinter as tk
from tkinter import messagebox

# =========================
# 基本設定
# =========================
WINDOW_SIZE = 300       # 視窗大小
GRID_SIZE = 3           # 3x3 棋盤

# =========================
# 主視窗
# =========================
root = tk.Tk()
root.title("OOXX 遊戲")
root.resizable(False, False)

# =========================
# 遊戲變數
# =========================
current_player = "X"    # 目前玩家
game_over = False       # 是否結束
board = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
buttons = []            # 儲存按鈕

# =========================
# 重新開始遊戲
# =========================
def reset_game():
    global current_player, game_over
    current_player = "X"
    game_over = False

    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            board[r][c] = ""
            buttons[r][c].config(text="", state="normal")

    status_label.config(text="目前輪到：X")

# =========================
# 檢查是否獲勝
# =========================
def check_win(player):
    # 檢查橫列
    for row in board:
        if all(cell == player for cell in row):
            return True

    # 檢查直行
    for col in range(GRID_SIZE):
        if all(board[row][col] == player for row in range(GRID_SIZE)):
            return True

    # 檢查對角線
    if all(board[i][i] == player for i in range(GRID_SIZE)):
        return True

    if all(board[i][GRID_SIZE - 1 - i] == player for i in range(GRID_SIZE)):
        return True

    return False

# =========================
# 檢查是否平手
# =========================
def check_draw():
    return all(board[r][c] != "" for r in range(GRID_SIZE) for c in range(GRID_SIZE))

# =========================
# 點擊棋格事件
# =========================
def on_click(row, col):
    global current_player, game_over

    if game_over:
        return

    # 該格已被佔用
    if board[row][col] != "":
        return

    # 放置棋子
    board[row][col] = current_player
    buttons[row][col].config(text=current_player)

    # 判斷勝負
    if check_win(current_player):
        game_over = True
        messagebox.showinfo("遊戲結束", f"{current_player} 獲勝！")
        status_label.config(text=f"{current_player} 獲勝！")
        return

    # 判斷平手
    if check_draw():
        game_over = True
        messagebox.showinfo("遊戲結束", "平手！")
        status_label.config(text="平手！")
        return

    # 換玩家
    current_player = "O" if current_player == "X" else "X"
    status_label.config(text=f"目前輪到：{current_player}")

# =========================
# 建立棋盤按鈕
# =========================
board_frame = tk.Frame(root)
board_frame.pack()

for r in range(GRID_SIZE):
    row_buttons = []
    for c in range(GRID_SIZE):
        btn = tk.Button(
            board_frame,
            text="",
            width=6,
            height=3,
            font=("Arial", 20),
            command=lambda r=r, c=c: on_click(r, c)
        )
        btn.grid(row=r, column=c)
        row_buttons.append(btn)
    buttons.append(row_buttons)

# =========================
# 狀態顯示
# =========================
status_label = tk.Label(root, text="目前輪到：X", font=("Arial", 14))
status_label.pack(pady=5)

# =========================
# 重新開始按鈕
# =========================
reset_button = tk.Button(root, text="重新開始", command=reset_game)
reset_button.pack(pady=5)

# =========================
# 啟動程式
# =========================
root.mainloop()
