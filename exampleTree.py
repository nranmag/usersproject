import tkinter as tk
from tkinter import ttk
class Arbol(ttk.Frame):
	
	def __init__(self, main_window):
		super().__init__(main_window)
		main_window.title("Vista de árbol en Tkinter")
		
		self.treeview = ttk.Treeview(self)
		self.treeview.pack()
		
		item = self.treeview.insert("", tk.END, text="User de Duluth: ")		
		self.treeview.insert(item, tk.END, text="Nombre completo:\nUser de MFS:\nTurno:")
		self.pack()

main_window = tk.Tk()

cl = Arbol(main_window)
cl.mainloop()