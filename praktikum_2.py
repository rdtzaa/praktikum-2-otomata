import tkinter as tk
from tkinter import messagebox
import re

class FSMVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Praktikum #2")
        
        self.input_string = ""
        self.current_index = 0
        self.current_state = 'S'
        self.is_running = False
        
        self.setup_ui()
        self.draw_fsm()

    def setup_ui(self):
        top_frame = tk.Frame(self.root, pady=10)
        top_frame.pack()
        
        tk.Label(top_frame, text="Masukkan String (0/1):", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        self.entry_str = tk.Entry(top_frame, font=("Arial", 14), width=15)
        self.entry_str.pack(side=tk.LEFT, padx=5)
        
        tk.Button(top_frame, text="Load", command=self.load_string, font=("Arial", 10), bg="lightblue").pack(side=tk.LEFT, padx=5)

        self.lbl_info = tk.Label(self.root, text="Belum ada string input.", font=("Courier", 16, "bold"))
        self.lbl_info.pack(pady=5)

        self.canvas = tk.Canvas(self.root, width=500, height=400, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.pack(pady=10)

        bottom_frame = tk.Frame(self.root, pady=10)
        bottom_frame.pack()
        
        self.btn_step = tk.Button(bottom_frame, text="Continue step", command=self.step_fsm, font=("Arial", 12), state=tk.DISABLED)
        self.btn_step.pack(side=tk.LEFT, padx=10)
        
        self.btn_reset = tk.Button(bottom_frame, text="Reset", command=self.reset_fsm, font=("Arial", 12))
        self.btn_reset.pack(side=tk.LEFT, padx=10)

    def draw_fsm(self):
        self.canvas.delete("all")
        
        # S -> A (0)
        self.canvas.create_line(125, 185, 225, 115, arrow=tk.LAST, width=2)
        self.canvas.create_text(160, 140, text="0", font=("Arial", 14, "bold"), fill="blue")
        
        # S -> B (1)
        self.canvas.create_line(125, 215, 225, 285, arrow=tk.LAST, width=2)
        self.canvas.create_text(160, 260, text="1", font=("Arial", 14, "bold"), fill="blue")
        
        # A -> C (0)
        self.canvas.create_line(280, 100, 370, 100, arrow=tk.LAST, width=2)
        self.canvas.create_text(325, 85, text="0", font=("Arial", 14, "bold"), fill="blue")
        
        # A -> B (1) - Garis Kiri
        self.canvas.create_line(240, 130, 240, 270, arrow=tk.LAST, width=2)
        self.canvas.create_text(225, 200, text="1", font=("Arial", 14, "bold"), fill="blue")
        
        # B -> A (0) - Garis Kanan
        self.canvas.create_line(260, 270, 260, 130, arrow=tk.LAST, width=2)
        self.canvas.create_text(275, 200, text="0", font=("Arial", 14, "bold"), fill="blue")
        
        # B -> B (1) Self Loop
        self.canvas.create_oval(230, 330, 270, 380, width=2)
        self.canvas.create_text(285, 355, text="1", font=("Arial", 14, "bold"), fill="blue")
        
        # C -> C (0,1) Self Loop
        self.canvas.create_oval(380, 40, 420, 70, width=2)
        self.canvas.create_text(435, 55, text="0, 1", font=("Arial", 14, "bold"), fill="blue")

        self.draw_node(100, 200, "S", is_active=(self.current_state == 'S'))
        self.draw_node(250, 100, "A", is_active=(self.current_state == 'A'))
        self.draw_node(250, 300, "B", is_active=(self.current_state == 'B'), is_final=True)
        self.draw_node(400, 100, "C", is_active=(self.current_state == 'C'))

    def draw_node(self, x, y, text, is_active=False, is_final=False):
        color = "#90EE90" if is_active else "white"
        self.canvas.create_oval(x-30, y-30, x+30, y+30, fill=color, width=2)
        
        if is_final:
            self.canvas.create_oval(x-24, y-24, x+24, y+24, width=1)
            
        self.canvas.create_text(x, y, text=text, font=("Arial", 16, "bold"))

    def load_string(self):
        val = self.entry_str.get().strip()
        if not val or not re.match(r'^[01]+$', val):
            messagebox.showerror("Error", "Input tidak valid! Harap masukkan hanya angka 0 dan 1.")
            return
            
        self.input_string = val
        self.reset_fsm()
        self.is_running = True
        self.btn_step.config(state=tk.NORMAL)
        self.update_info_label()

    def update_info_label(self):
        if not self.is_running:
            return
            
        display_text = ""
        for i, ch in enumerate(self.input_string):
            if i == self.current_index:
                display_text += f"[{ch}]" # Karakter saat ini dikurung siku
            else:
                display_text += ch
                
        self.lbl_info.config(text=f"Proses: {display_text}")

    def step_fsm(self):
        if self.current_index >= len(self.input_string):
            self.finish_simulation()
            return
            
        ch = self.input_string[self.current_index]
        
        if self.current_state == 'S':
            if ch == '0':
                self.current_state = 'A' 
            else:
                self.current_state = 'B'
        elif self.current_state == 'A':
            if ch == '0':
                self.current_state = 'C' 
            else:
                self.current_state = 'B'
        elif self.current_state == 'B':
            if ch == '0':
                self.current_state = 'A'
            else:
                self.current_state = 'B'
        elif self.current_state == 'C':
            self.current_state = 'C'
            
        self.current_index += 1
        self.draw_fsm()
        self.update_info_label()
        
        # if self.current_index == len(self.input_string):
        #     self.finish_simulation()

    def finish_simulation(self):
        self.is_running = False
        self.btn_step.config(state=tk.DISABLED)
        self.lbl_info.config(text=f"Selesai: {self.input_string}")
        
        if self.current_state == 'B':
            messagebox.showinfo("Hasil", f"String '{self.input_string}' DITERIMA (Accepted)!\nFinal State = B.")
        else:
            messagebox.showwarning("Hasil", f"String '{self.input_string}' DITOLAK (Rejected)!\nFinal State = {self.current_state}.")

    def reset_fsm(self):
        self.current_state = 'S'
        self.current_index = 0
        self.is_running = False
        self.btn_step.config(state=tk.DISABLED)
        self.lbl_info.config(text="Belum ada string input")
        self.draw_fsm()

if __name__ == "__main__":
    root = tk.Tk()
    app = FSMVisualizer(root)
    root.mainloop()