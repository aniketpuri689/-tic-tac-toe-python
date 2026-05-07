import tkinter as tk
import random
window=tk.Tk()
window.title("TIC TAC TOE MASTER")
window.geometry("450x850")  

                                            # --- Creating frames ---

frame_menu=tk.Frame(window , width=450, height=850, bg="#56dee2")       
frame_game=tk.Frame(window , width=450, height=850, bg="#44ddf1")       
frame_board=tk.Frame(window , width=450, height=850, bg="#44ddf1")  
frame_ai_menu=tk.Frame(window , width=450, height=850, bg="#56dee2")   
frame_pwc=tk.Frame(window , width=450, height=850, bg="#44ddf1")       
frame_ai=tk.Frame(window , width=450, height=850, bg="#44ddf1")

                                        # --- Frame switching functions  ---

def show_menu():
    frame_game.pack_forget()
    frame_board.pack_forget()
    frame_ai_menu.pack_forget()
    frame_pwc.pack_forget()
    frame_ai.pack_forget()
    frame_menu.pack(fill="both", expand=True)
    

def show_game():
    frame_menu.pack_forget()
    frame_ai_menu.pack_forget()
    frame_pwc.pack_forget()
    frame_ai.pack_forget()
    frame_board.pack(fill="x", expand=False)
    frame_game.pack(fill="both", expand=True) 

def show_ai_menu():
    frame_menu.pack_forget()
    frame_pwc.pack_forget()
    frame_ai.pack_forget()
    frame_game.pack_forget()
    frame_board.pack_forget()
    frame_ai_menu.pack(fill="both", expand=True) 
    

def pwc():
    frame_board.pack_forget()
    frame_menu.pack_forget()
    frame_game.pack_forget()
    frame_ai_menu.pack_forget()
    frame_ai.pack_forget()
    frame_pwc.pack(fill="both", expand=True)

def ai():
    frame_board.pack_forget()
    frame_menu.pack_forget()
    frame_game.pack_forget()
    frame_pwc.pack_forget()
    frame_ai_menu.pack_forget()
    frame_ai.pack(fill="both", expand=True)

                                                    # --- MENU FRAME ---

label_title=tk.Label(frame_menu, text="TIC TAC TOE", font=("Comic Sans MS", 36, "bold"), bg="#1e1e2f", fg="#f0f0f0")
btn_pwf=tk.Button(frame_menu, text="PLAY WITH FRIENDS", command=show_game, width=20, height=2, bg="#ff6f61", fg="black", font=("Comic Sans MS", 14, "bold"))
btn_pwc=tk.Button(frame_menu, text="PLAY WITH COMPUTER", command=show_ai_menu, width=20, height=2, bg="#6fa1f2", fg="black", font=("Comic Sans MS", 14, "bold"))
btn_exit=tk.Button(frame_menu, text="EXIT GAME", command=window.quit, width=20, height=2, bg="#ffcc00", fg="black", font=("Comic Sans MS", 14, "bold"))

label_title.pack(pady=60)
btn_pwf.pack(pady=20)
btn_pwc.pack(pady=20)
btn_exit.pack(pady=20)
show_menu()

                                                    # --- GAME FRAME ---

game_gui=[[],[],[]]
game_logic=[[0,0,0],[0,0,0],[0,0,0]]
turn="X"
game_record={}
chanse=1
round=1

for i in range(3):
     for j in range(3):
         btn=tk.Button(frame_board,text="", width=8, height=4, bg="white", fg="black", font=("Comic Sans MS", 20), command=lambda x=i,y=j: (save_game(x,y),current_player(x,y),check_winner())) 
         game_gui[i].append(btn)
         btn.grid(row=(i+4),column=(j+2))

def save_game(x,y):
     global game_record,turn,chanse,round
     if round not in game_record:
        game_record[round] = {}
     game_record[round][chanse] = {"player": turn, "position": (x, y)}
     chanse += 1
     
def current_player(x,y):
    global game_logic,game_gui,turn
    if game_logic[x][y]==0:
        if turn=="X":
            game_gui[x][y].config(text="X", fg="#f73221", font=("Comic Sans MS", 20))
            game_logic[x][y]="X"
            player_label.config(text="Player O's turn", fg="#1af6ee")
            turn="O"
        else:
            game_gui[x][y].config(text="O", fg="#1fbefc", font=("Comic Sans MS", 20))
            game_logic[x][y]="O"
            player_label.config(text="Player X's turn", fg="#ff6f61")
            turn="X"

won=False
def check_winner():
    global game_logic,game_gui,result_label,won,player_label
    for i in range(3):
        if game_logic[i][0]==game_logic[i][1]==game_logic[i][2]!=0:
            player_label.config(text="",bg="#44ddf1")
            result_label.config(text=f" PLAYER {game_logic[i][0]} WIN ", fg="#00ff00",bg="#44ddf1")
            won=True
        if game_logic[0][i]==game_logic[1][i]==game_logic[2][i]!=0:
            player_label.config(text="",bg="#44ddf1")
            result_label.config(text=f" PLAYER {game_logic[0][i]} WIN ", fg="#00ff00",bg="#44ddf1")
            won=True
    if game_logic[0][0]==game_logic[1][1]==game_logic[2][2]!=0:
            player_label.config(text="",bg="#44ddf1")
            result_label.config(text=f" PLAYER {game_logic[0][0]} WIN ", fg="#00ff00",bg="#44ddf1")
            won=True
    if game_logic[0][2]==game_logic[1][1]==game_logic[2][0]!=0:
            player_label.config(text="",bg="#44ddf1")
            result_label.config(text=f" PLAYER {game_logic[0][2]} WIN ", fg="#00ff00",bg="#44ddf1")
            won=True
    if won==False:
        all_filled=True
        for i in range(3):
            for j in range(3):
                if game_logic[i][j]==0:
                    all_filled=False
        if all_filled:
            player_label.config(text="")
            result_label.config(text=f" ITS A DRAW ", fg="#FFFDFD",bg="#44ddf1")
            ai_result_label.config(text=f" ITS A DRAW ", fg="#FFFDFD",bg="#44ddf1")
    if won==True:
         for row in game_gui:
             for btn in row:
                 btn.config(state="disabled")
         print_record()


def restart_game():
    global game_logic,game_gui,turn,won,game_record,chanse,round
    chanse=1
    turn="X"
    game_logic=[[0,0,0],[0,0,0],[0,0,0]]
    result_label.config(text="")
    for row in game_gui:
             for btn in row:
                 btn.config(text="", state="normal")
    player_label.config(text="Player X's starts",fg="#000000", bg="#44ddf1")
    won=False
    record_label.config(text="Game Record")
    round+=1

def print_record():
    global game_record,record_label,won,round
    if won:
        rec=f"Game Record:\nROUND: {round}\n"
        for key in game_record[round]:
            move=game_record[round][key]
            rec+=f'Chanse {key}: Player {move["player"]} placed at position {move["position"]}\n'
        record_label.config(text=rec)


back_btn=tk.Button(frame_board,text="BACK TO MENU", width=10, height=2, bg="#ffcc00", fg="black", command=show_menu)
restart_btn=tk.Button(frame_game,text="RESTART", width=8, height=2, bg="white", fg="black", command=restart_game)
player_label=tk.Label(frame_game,text="Player X starts", font=("Comic Sans MS",20), fg="#000000", bg="#44ddf1")
result_label=tk.Label(frame_game,font=("Comic Sans MS",20), bg="#44ddf1", fg="black")
record_label=tk.Label(frame_game, text="Game Record",font=("Comic Sans MS",16,"bold"), bg="#44ddf1", fg="#000000")

back_btn.grid(row=0,column=0, pady=10)
#GAME BOARD
result_label.grid(row=7,column=6, pady=10)
player_label.grid(row=8,column=6, pady=10)
restart_btn.grid(row=9,column=6,padx=10, pady=20)
record_label.grid(row=10,column=2, pady=10)

                                                     #--- AI MENU ---

ai_menu_label=tk.Label(frame_ai_menu, text="PLAY FOR FUN OR TRAIN", font=("Comic Sans MS", 24, "bold"), bg="#1e1e2f", fg="#f0f0f0")
ai_menu_pwc=tk.Button(frame_ai_menu, text="PLAY FOR FUN", command=pwc, width=20, height=2, bg="#ff6f61", fg="black", font=("Comic Sans MS", 14, "bold"))
ai_menu_train_ai=tk.Button(frame_ai_menu, text="PLAY TO TRAIN AI", command=ai, width=20, height=2, bg="#6fa1f2", fg="black", font=("Comic Sans MS", 14, "bold"))
ai_menu_back_btn=tk.Button(frame_ai_menu, text="MAIN MENU", command=show_menu, width=20, height=2, bg="#ffcc00", fg="black", font=("Comic Sans MS", 14, "bold"))

ai_menu_label.pack(pady=50)
ai_menu_pwc.pack(pady=30)
ai_menu_train_ai.pack(pady=30)
ai_menu_back_btn.pack(pady=30)

                                                     #--- TRAIN AI ---
ai_cooimgsoon_label=tk.Label(frame_ai, text="AI COMING SOON...!", font=("Comic Sans MS", 24, "bold"), bg="#1e1e2f", fg="#f0f0f0")
ai_cooimgsoon_label.pack(pady=200)

                                                    # --- PWC FRAME ---

ai_game_gui=[[],[],[]]
ai_game_logic=[[0,0,0],[0,0,0],[0,0,0]]
avilable_moves=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

for i in range(3):
     for j in range(3):
         btn=tk.Button(frame_pwc,text="", width=8, height=4, bg="#f9f9fc", fg="black", font=("Comic Sans MS", 20), command=lambda x=i,y=j: (ai_current_player(x,y),ai_check_winner())) 
         ai_game_gui[i].append(btn)
         btn.grid(row=(i+2),column=(j+2))

def ai_current_player(x,y):
    global ai_game_gui,ai_game_logic,turn,avilable_moves,ai_won
    if ai_game_logic[x][y]==0:
        if turn=="X":
            ai_game_gui[x][y].config(text="X", fg="#f73221", font=("Comic Sans MS", 20))
            ai_game_logic[x][y]="X"
            avilable_moves.remove((x,y))
            ai_check_winner()
            
            if not ai_won:
                turn = "O"
                ai_player_label.config(text="COMPUTER'S TURN", fg="#1af6ee")
                ai_move()
                ai_check_winner()

def ai_move():
    global avilable_moves,ai_game_gui,ai_game_logic,turn
    ind={0,1,2}
    if turn=="O" and avilable_moves:
        for i in range(3):
             for j in range(3):
                  for k in range (3):
                         if ai_game_logic[i][j]==ai_game_logic[i][k]!=0 and j!=k :    # ROW WISE CHECKING IF ANY TWO CONTINOUS SAME ELEMENTS IN THE SAME ROW                                   
                            a=next(x for x in ind if x!=j and x!=k)                                                                          # IF(O) THEN THIS IS THE WINNING MOVE IF (X) THEN BLOCKING MOVE
                            if ai_game_logic[i][a]==0:
                                ai_game_gui[i][a].config(text="O", fg="#1fbefc", font=("Comic Sans MS", 20))
                                ai_game_logic[i][a]="O"                                                                             # (WINNING MOVE) WE WANT TO PLACE THE NEW MOVE IN THE SAME COLUMN BUT DIFFRENT ROW THEN J OR K
                                ai_player_label.config(text="YOUR TURN", fg="#ff6f61")
                                avilable_moves.remove((i,a))
                                turn="X"
                                return

                         elif ai_game_logic[j][i]==ai_game_logic[k][i]!=0 and j!=k :   # COLUMN WISE CHECKING IF ANY TWO CONTINOUS SAME ELEMENTS IN THE SAME COLUMN
                            a=next(x for x in ind if x!=j and x!=k)                                                             # IF(O) THEN THIS IS THE WINNING MOVE IF (X) THEN BLOCKING MOVE
                            if ai_game_logic[a][i]==0:
                                ai_game_gui[a][i].config(text="O", fg="#1fbefc", font=("Comic Sans MS", 20))
                                ai_game_logic[a][i]="O"                                                                             # (WINNING MOVE) WE WANT TO PLACE THE NEW MOVE IN THE SAME COLUMN BUT DIFFRENT ROW THEN J OR K
                                ai_player_label.config(text="YOUR TURN", fg="#ff6f61")
                                avilable_moves.remove((a,i))
                                turn="X"
                                return


                         elif ai_game_logic[j][j]==ai_game_logic[k][k]!=0 and j!=k :  # FIRST DIOGNAL WISE CHECKING IF ANY TWO CONTINOUS SAME ELEMENTS IN THE SAME DIOGNAL
                            a=next(x for x in ind if x!=j and x!=k)                                                             # IF(O) THEN THIS IS THE WINNING MOVE IF (X) THEN BLOCKING MOVE
                            if ai_game_logic[a][a]==0:
                                ai_game_gui[a][a].config(text="O", fg="#1fbefc", font=("Comic Sans MS", 20))
                                ai_game_logic[a][a]="O"                                                                             # (WINNING MOVE) WE WANT TO PLACE THE NEW MOVE IN THE SAME DIOGNAL
                                ai_player_label.config(text="YOUR TURN", fg="#ff6f61")
                                avilable_moves.remove((a,a))
                                turn="X"
                                return
                         
                             
                         elif (j+k==2) and ai_game_logic[j][k]==ai_game_logic[k][j]!=0:  # SECOND DIOGNAL WISE CHECKING IF ANY TWO CONTINOUS SAME ELEMENTS IN THE SAME DIOGNAL
                            if j==k and ai_game_logic[j][k]==ai_game_logic[0][2] and ai_game_logic[2][0]==0 :                                                   # IF AI_GAME_LOGIC[1][1]=AI_GAME_LOGIC[0][2]                                    
                                ai_game_gui[2][0].config(text="O", fg="#1fbefc", font=("Comic Sans MS", 20))                      # THEN TAKE ON AI_GAME_LOGIC[2][0]
                                ai_game_logic[2][0]="O"                                                                             # (WINNING MOVE) WE WANT TO PLACE THE NEW MOVE IN THE SAME DIOGNAL 
                                ai_player_label.config(text="YOUR TURN", fg="#ff6f61")
                                avilable_moves.remove((2,0))
                                turn="X"
                                return
                            elif j==k and ai_game_logic[j][k]==ai_game_logic[2][0]!=0 and ai_game_logic[0][2]==0 :                                                # IF AI_GAME_LOGIC[1][1]=AI_GAME_LOGIC[2][0]
                                ai_game_gui[0][2].config(text="O", fg="#1fbefc", font=("Comic Sans MS", 20))                      # THEN TAKE ON AI_GAME_LOGIC[0][2]
                                ai_game_logic[0][2]="O"                                                                             # (WINNING MOVE) WE WANT TO PLACE THE NEW MOVE IN THE SAME DIOGNAL 
                                ai_player_label.config(text="YOUR TURN", fg="#ff6f61")
                                avilable_moves.remove((0,2))
                                turn="X"
                                return
                            elif ai_game_logic[1][1]==0:
                                a=next(x for x in ind if x!=j and x!=k)                                                             # IF AI_GAME_LOGIC[0][2]=AI_GAME_LOGIC[2][0]
                                ai_game_gui[1][1].config(text="O", fg="#1fbefc", font=("Comic Sans MS", 20))                      # THEN TAKE ON AI_GAME_LOGIC[1][1]
                                ai_game_logic[1][1]="O"                                                                             # (WINNING MOVE) WE WANT TO PLACE THE NEW MOVE IN THE SAME DIOGNAL
                                ai_player_label.config(text="YOUR TURN", fg="#ff6f61")
                                avilable_moves.remove((1,1))
                                turn="X"
                                return


        if ai_game_logic[1][1]==0:                                                                           # TAKE CENTRE IF ITS EMPTY
            ai_game_gui[1][1].config(text="O", fg="#1fbefc", font=("Comic Sans MS", 20))
            ai_game_logic[1][1]="O"
            ai_player_label.config(text="YOUR TURN", fg="#ff6f61")
            avilable_moves.remove((1,1))
            turn="X"
            return

                        
        elif (j%2==0 and k%2==0) :                                                   # AT CORNER PEICES ONLY BOTH J,K ARE EVEN 
            corner_moves=[(b,c) for (b,c) in avilable_moves if b%2==0 and c%2==0 and ai_game_logic[b][c]==0]
            move=random.choice(corner_moves)
            row,col=move
            if ai_game_logic[row][col]==0:
                ai_game_gui[row][col].config(text="O", fg="#1fbefc", font=("Comic Sans MS", 20))                      # TAKE CORNER PEICES IF EMPTY
                ai_game_logic[row][col]="O"
                ai_player_label.config(text="YOUR TURN", fg="#ff6f61")
                avilable_moves.remove((row,col))
                turn="X"
                return
                            

        elif ((j+k)%2==1) :
            side_moves=[(b,c) for (b,c) in avilable_moves if (b+c)%2==1 and ai_game_logic[b][c]==0]
            move=random.choice(side_moves)
            row,col=move
            if ai_game_logic[row][col]==0:
                ai_game_gui[row][col].config(text="O", fg="#1fbefc", font=("Comic Sans MS", 20))
                ai_game_logic[row][col]="O"
                ai_player_label.config(text="YOUR TURN", fg="#ff6f61")
                avilable_moves.remove((row,col))
                turn="X"
                return

                             

ai_won=False
def ai_check_winner(): 
    global ai_game_logic,ai_game_gui,ai_result_label,ai_player_label,turn,ai_won
    for i in range(3):
        if ai_game_logic[i][0]==ai_game_logic[i][1]==ai_game_logic[i][2]!=0:
            ai_player_label.config(text="",bg="#44ddf1")
            ai_result_label.config(text=f" PLAYER {game_logic[i][0] } WIN ", fg="#00ff00",bg="#44ddf1")
            ai_won=True
        if ai_game_logic[0][i]==ai_game_logic[1][i]==ai_game_logic[2][i]!=0:
            ai_player_label.config(text="",bg="#44ddf1")
            ai_result_label.config(text=f" PLAYER {game_logic[0][i]} WIN ", fg="#00ff00",bg="#44ddf1")
            ai_won=True
    if ai_game_logic[0][0]==ai_game_logic[1][1]==ai_game_logic[2][2]!=0:
            ai_player_label.config(text="",bg="#44ddf1")
            ai_result_label.config(text=f" PLAYER {game_logic[0][0]} WIN ", fg="#00ff00",bg="#44ddf1")
            ai_won=True
    if ai_game_logic[0][2]==ai_game_logic[1][1]==ai_game_logic[2][0]!=0:
            ai_player_label.config(text="",bg="#44ddf1")
            ai_result_label.config(text=f" PLAYER {game_logic[0][2]} WIN ", fg="#00ff00",bg="#44ddf1")
            ai_won=True
    if ai_won==False:
        ai_all_filled=True
        for i in range(3):
            for j in range(3):
                if ai_game_logic[i][j]==0:
                    ai_all_filled=False
        if ai_all_filled:
            ai_player_label.config(text="")
            ai_result_label.config(text=f" ITS A DRAW ", fg="#FFFDFD",bg="#44ddf1")
    if ai_won==True:
         for row in ai_game_gui:
             for btn in row:
                 btn.config(state="disabled")

def ai_restart_game():
    global ai_game_logic,ai_game_gui,avilable_moves,turn,ai_won
    turn="X"
    ai_game_logic=[[0,0,0],[0,0,0],[0,0,0]]
    avilable_moves=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    ai_result_label.config(text="")
    for row in ai_game_gui:
             for btn in row:
                 btn.config(text="", state="normal")
    ai_player_label.config(text="YOUR TURN", fg="#ff6f61", bg="#44ddf1")
    ai_won=False

label_pwc=tk.Label(frame_pwc, text="Play with Computer ", font=("Comic Sans MS", 24), bg="#2f2f4f", fg="#ffffff")
ai_back_btn=tk.Button(frame_pwc, text="BACK TO MENU", bg="#fbf6f6", fg="black", width=10, height=2, command=show_menu)
ai_player_label=tk.Label(frame_pwc,text="YOUR TURN", font=("Comic Sans MS",20), fg="#ff6f61", bg="#44ddf1")
ai_result_label=tk.Label(frame_pwc,font=("Comic Sans MS",20), bg="#44ddf1", fg="black")
ai_restart_btn=tk.Button(frame_pwc,text="RESTART", width=8, height=2, bg="white", fg="black", command=ai_restart_game)

ai_back_btn.grid(row=0,column=0,pady=10)
label_pwc.grid(row=1,column=2, columnspan=3,pady=50)
# board frame
ai_player_label.grid(row=6,column=3, pady=10)
ai_result_label.grid(row=7,column=2,columnspan=2, pady=10,padx=10)
ai_restart_btn.grid(row=8,column=3, pady=20)
window.mainloop() 