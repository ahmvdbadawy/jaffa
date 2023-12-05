import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import heapq
import random
import time
import wikipedia as wiki
 
class GUI:
    def __init__(self, master:tk.Tk, background_image_path, From, To):
                
        self.graph = {
            'Safad': ['Acre','Tiberias'],
            'Acre': ['Haifa','Nazareth','Tiberias','Safad'],
            'Haifa': ['Nazareth','Acre','Jinin','Tulkarm'],
            'Tiberias': ['Safad','Acre','Nazareth','Baysan'],
            'Nazareth': ['Baysan','Tiberias','Acre','Jinin','Haifa'],
            'Baysan': ['Tiberias','Nazareth','Jinin'],
            'Jinin': ['Tulkarm','Nablus','Baysan','Nazareth','Haifa'],
            'Nablus': ['Jinin','Tulkarm','Ramallah'],
            'Tulkarm': ['Haifa','Jinin','Nablus','jaffa'],
            'jaffa': ['Tulkarm','al-Ramla'],
            'Ramallah': ['Al-Quds','al-Ramla','Nablus'],
            'al-Ramla': ['jaffa','Ramallah','Al-Quds','Gaza'],
            'Al-Quds': ['al-Ramla','Ramallah','Hebron'],
            'Hebron': ['Al-Quds','Beersheba'],
            'Beersheba': ['Hebron','Gaza'],
            'Gaza': ['al-Ramla','Beersheba']
        }
        # (x,y)
        self.nodes={'Safad': (450,120),
                    'Acre': (326,130),
                    'Acre-Haifa1': (317.3,170.4),
                    'Acre-Haifa2': (310,178.2),
                    'Haifa': (292,177),
                    'Tiberias': (460,191),
                    'Nazareth': (390,219),
                    'Baysan': (455,301.2),
                    'Jinin': (395,308.8),
                    'Nablus': (384,405),
                    'Tulkarm': (310,367),
                    'jaffa': (229,464),
                    'Ramallah': (364,514),
                    'al-Ramla': (267,506.5),
                    'Al-Quds': (371.5,561),
                    'Hebron': (338.4,651),
                    'Beersheba': (236,748),
                    'Gaza': (137,665.6)}
        
        self.master = master
        self.From = From
        self.To = To
        self.text_box_width = 383
        self.text_box_x = 617
        self.text_box_height = 1000
        self.text_box_y = 0
        self.palestine_list = self._palestine_list()
        self.Current_drawing = []
        self.master.title("Jaffa")
        master.geometry('1000x1000')
        
        # Margin and additions
        Text_frame = tk.Text(master, bg="#2E4053", state=tk.DISABLED, font=("Verdana", 12), foreground="white", insertbackground="white", bd=3, relief=tk.SOLID, height=600, width=383)
        Text_frame.place(x=self.text_box_x, y=self.text_box_y)
        
        # Input frame
        input_frame = tk.LabelFrame(master, text="Direction", font=("bold", 14), labelanchor="n", bg="#3498DB", padx=10, pady=10, height=400, width=383)
        input_frame.place(x=self.text_box_x, y=800)
        
        # Label and Entry for "To" city
        city_label = tk.Label(input_frame,background='#3498DB', text="To", bg="#3498DB", font=("bold", 12), foreground="white")
        city_label.place(x=10, y=10)

        self.ans_from = from_combobox = ttk.Combobox(input_frame,width=30)
        from_combobox['value'] = self.palestine_list
        from_combobox.place(x=60, y=10)
        
        # self.to_city_input = tk.Entry(input_frame, bg="#B3C9F4", justify='left', font=("Verdana", 12))
        # self.to_city_input.place(x=80, y=10)
        
        # Label and Entry for "From" city
        
        from_city_label = tk.Label(input_frame, text="From", bg="#3498DB", font=("bold", 12), foreground="white")
        from_city_label.place(x=10, y=50)
        
        self.ans_to = to_combobox = ttk.Combobox(input_frame,width=30)
        to_combobox['value'] = self.palestine_list
        to_combobox.place(x=60, y=50)
        
        from_submit_button = tk.Button(input_frame, text="GO", bg="#4E6D8C", fg="white", font=("Verdana", 12), command=self.submit_path_city, relief=tk.GROOVE)
        from_submit_button.place(x=220, y=85)
        
        # checkbox
        
        tk.Label(input_frame, text="search on wikipedia", bg="#3498DB", font=("bold", 12), foreground="white").place(x=35, y=90)
        self.box = tk.Checkbutton(input_frame,bg="#3498DB").place(x=10, y=90)
        
        # ______________________________ خريطه فلسطين _______________________________
        
        self.background_image = Image.open(background_image_path)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = tk.Canvas(self.master, width=self.background_image.width, height=self.background_image.height)
        # self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.canvas.place(width=self.background_image.width, height=self.background_image.height,x=0,y=0)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)
        

        # path = self.BFS(self.From, self.To)
        # print(path)
        # self.draw_lines(path)
        # self.draw_nodes()
    
    def draw_nodes(self):
        for node, coordinates in self.nodes.items():
            x, y = coordinates
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill=self.random_color(), tags=node)
        
    def draw_lines(self, list):
        for x in range(0, len(list)-1):
            self.master.update()
            time.sleep(1)
            if list[x] == 'Acre' and list[x+1] == 'Haifa':
                A = self.nodes[list[x]]
                B = self.nodes['Acre-Haifa1']
                C = self.nodes['Acre-Haifa2']
                D = self.nodes[list[x+1]]
                line = self.canvas.create_line(A[0],A[1],B[0],B[1],C[0],C[1],D[0],D[1], fill="red", width=2)
                self.Current_drawing.append(line)
            elif list[x] == 'Haifa' and list[x+1] == 'Acre':
                A = self.nodes[list[x]]
                B = self.nodes['Acre-Haifa2']
                C = self.nodes['Acre-Haifa1']
                D = self.nodes[list[x+1]]
                line = self.canvas.create_line(A[0],A[1],B[0],B[1],C[0],C[1],D[0],D[1], fill="red", width=2)
                self.Current_drawing.append(line)
            else:    
                A = self.nodes[list[x]]
                B = self.nodes[list[x+1]]
                line = self.canvas.create_line(A[0],A[1],B[0],B[1], fill="red", width=2)
                self.Current_drawing.append(line)
    def BFS(self, From, To):
        visited = []
        queue = [[From]]
        while(queue):
            path = queue.pop(0)
            node = path[-1]
            if node in visited:
                continue
            visited.append(node)
            if node == To:
                return path 
            else:
                new_nodes = self.graph.get(node, [])
                for node2 in new_nodes:
                    new_path = path.copy()
                    new_path.append(node2)
                    queue.append(new_path)
            
    def random_color(self):
        return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def _palestine_list(self):
        list = []
        for x in self.graph:
            list.append(x)
        return list
    
    def clean_screen(self):
        for x in self.Current_drawing:
            self.canvas.delete(x)
    
    def submit_path_city(self):
        self.From = self.ans_from.get()
        self.To = self.ans_to.get()
        lst = self.BFS(self.From,self.To)
        if self.Current_drawing:
            self.clean_screen()
        self.draw_lines(lst)
        # Anas, add details

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root, "palestine_states.jpg",'Gaza','Tiberias')
    root.mainloop()
