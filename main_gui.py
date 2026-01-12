import tkinter as tk
from game_logic import GameLogic 

class RPSGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Mushi-ken: Best of 4")
        self.root.geometry("350x500")
        self.game = GameLogic()
        
        self.main_container = tk.Frame(self.root)
        self.main_container.pack(fill="both", expand=True)
        
        self.show_start_screen()

    def clear_screen(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def show_start_screen(self):
        self.clear_screen()
        
        tk.Label(self.main_container, text="Mushi-ken", font=("Arial", 22, "bold")).pack(pady=20)
        
        # Rules Box
        rules_frame = tk.LabelFrame(self.main_container, text=" Rules (Best of 4) ", padx=10, pady=10)
        rules_frame.pack(padx=20, pady=10)
        
        rules_text = (
            "• Frog eats Slug\n"
            "• Slug dissolves Snake\n"
            "• Snake eats Frog\n\n"
            "First to 3 points wins the match!"
        )
        tk.Label(rules_frame, text=rules_text, justify=tk.LEFT).pack()

        tk.Button(self.main_container, text="START MATCH", font=("Arial", 12, "bold"), 
                  bg="#2ecc71", fg="white", width=15, command=self.show_game_screen).pack(pady=20)
        
        tk.Button(self.main_container, text="EXIT", font=("Arial", 12), 
                  width=15, command=self.root.quit).pack()

    def show_game_screen(self):
        self.clear_screen()
        
        tk.Label(self.main_container, text="Match in Progress", font=("Arial", 10, "italic")).pack(pady=5)
        self.target_label = tk.Label(self.main_container, text="First to 3 Points Wins", font=("Arial", 12, "bold"), fg="blue")
        self.target_label.pack(pady=5)

        # Choice Buttons
        btn_frame = tk.Frame(self.main_container)
        btn_frame.pack(pady=20)
        
        for val, name in self.game.choices.items():
            tk.Button(btn_frame, text=name, width=10, height=2, font=("Arial", 10, "bold"),
                      command=lambda v=val: self.play_round(v)).pack(side=tk.LEFT, padx=5)

        # Results Area
        self.res_label = tk.Label(self.main_container, text="Choose your creature!", font=("Arial", 12), height=3)
        self.res_label.pack()
        
        # Score Board
        score_frame = tk.Frame(self.main_container, relief=tk.RIDGE, borderwidth=2)
        score_frame.pack(pady=20, padx=20, fill="x")
        
        self.score_label = tk.Label(score_frame, text=f"YOU: {self.game.player_score}   |   CPU: {self.game.computer_score}", 
                                    font=("Arial", 14, "bold"))
        self.score_label.pack(pady=10)

        tk.Button(self.main_container, text="End Match Early", fg="gray", command=self.show_end_screen).pack(side=tk.BOTTOM, pady=20)

    def play_round(self, player_choice):
        comp_choice = self.game.get_computer_choice()
        result = self.game.determine_winner(player_choice, comp_choice)
        
        p_name = self.game.choices[player_choice]
        c_name = self.game.choices[comp_choice]
        
        self.res_label.config(text=f"{p_name} vs {c_name}\n{result}")
        self.score_label.config(text=f"YOU: {self.game.player_score}   |   CPU: {self.game.computer_score}")
        
        # Best of 4 Logic: First to 3 wins
        if self.game.player_score >= 3 or self.game.computer_score >= 3:
            # Short delay so user can see the final round result
            self.root.after(1000, self.show_end_screen)

    def show_end_screen(self):
        self.clear_screen()
        
        # Determine Winner
        if self.game.player_score > self.game.computer_score:
            msg = "VICTORY!"
            color = "green"
        elif self.game.computer_score > self.game.player_score:
            msg = "DEFEAT!"
            color = "red"
        else:
            msg = "DRAW!"
            color = "black"

        tk.Label(self.main_container, text=msg, font=("Arial", 30, "bold"), fg=color).pack(pady=30)
        
        score_text = f"Final Series Score\n\nYou: {self.game.player_score}\nCPU: {self.game.computer_score}"
        tk.Label(self.main_container, text=score_text, font=("Arial", 14)).pack(pady=10)

        tk.Button(self.main_container, text="RESTART MATCH", font=("Arial", 12, "bold"), 
                  bg="#3498db", fg="white", width=18, command=self.restart_game).pack(pady=10)
        
        tk.Button(self.main_container, text="QUIT TO DESKTOP", font=("Arial", 12), 
                  width=18, command=self.root.quit).pack()

    def restart_game(self):
        self.game.player_score = 0
        self.game.computer_score = 0
        self.show_game_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSGui(root)
    root.mainloop()