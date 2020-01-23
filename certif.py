import tkinter as tk
from tkinter import *
from tkinter import ttk, font
from datetime import datetime, date, time, timedelta
from tkinter import messagebox
import csv, operator

def Aplicacion2(v1,v2):
	#Inicialización de Variables
	name = StringVar()
	mfs = StringVar()
	date_in = StringVar()
	role = StringVar()
	state = StringVar()
	#Creacion de la ventana
	app = Tk()
	app.geometry('1200x900+300+100')
	app.resizable(0,0)
	app.minsize(400,300)
	app.title("Sistema de Certificaciones")
	app.iconbitmap("logo2.ico")
	app.config(bg="white")
	fuente = font.Font(family='calibri', size=14, weight='bold')
	titulo = Label(app, text="CERTIFICACIONES", fg="red", bg="white", font=("Verdana",26,"bold")).place(x=50, y=20)
	with open('import/datos.csv') as File:	
		reader = csv.reader(File, delimiter=',',quotechar=',',quoting=csv.QUOTE_MINIMAL)
		for elemento in reader:
			if v1 == elemento[1]:
				name=elemento[3];ecam=elemento[0];date_in=elemento[4];role=elemento[5];state=activos(elemento[8])
	File.close()
	#Componentes de la Ventana
	lbl_name = Label(app, text="Nombre: ", bg="white", font=("calibri",14,"bold")).place(x=100, y=90)
	txt_name = Label(app)
	txt_name.pack()
	txt_name.place(x=180, y=90)
	txt_name.config(text=name, fg="blue", bg="white", font=("calibri",14,"bold"))
	nemp = Label(app, text="ID Empleado: ", bg="white", font=("calibri",14,"bold")).place(x=680, y=90)
	txt_nemp = Label(app)
	txt_nemp.pack()
	txt_nemp.place(x=800, y=90)
	txt_nemp.config(text=ecam, fg="blue", bg="white", font=("calibri",14,"bold"))
	lbl_role = Label(app, text="Rol: ", bg="white", font=("calibri",14,"bold")).place(x=940, y=90)
	txt_role = Label(app)
	txt_role.pack()
	txt_role.place(x=980, y=90)
	txt_role.config(text=role, fg="blue", bg="white", font=("calibri",14,"bold"))
	date = Label(app, text="Fecha de Ingreso: ", bg="white", font=("calibri",14,"bold")).place(x=100, y=130)
	txt_date = Label(app)
	txt_date.pack()
	txt_date.place(x=250, y=130)
	txt_date.config(text=date_in, fg="blue", bg="white", font=("calibri",14,"bold"))
	lbl_state = Label(app, text="Status: ", bg="white", font=("calibri",14,"bold")).place(x=380, y=130)
	txt_state = Label(app)
	txt_state.pack()
	txt_state.place(x=450, y=130)
	txt_state.config(text=state, fg="blue", bg="white", font=("calibri",14,"bold"))
	certi = Label(app, text="Tipo de Certificacion que realizará: ", bg="white", font=("calibri",14,"bold")).place(x=550, y=130)
	cmb = ttk.Combobox(app, width=15, font=("calibri",14,"bold"), values=('Fase 1','Fase 2','Fase 3','Fase 4')).place(x=850, y=130)
	bt = Button(app, text="EXAMENES", command=lambda: examenes(name)).place(x=1080, y=130)
	#Tabla para Lista de Certificaciones
	lbl_fase = Label(app, text="FASE", bg="white", font=("calibri",14,"bold")).place(x=340, y=220)
	lbl_calif = Label(app, text="CALIFICACION", bg="white", font=("calibri",14,"bold")).place(x=550, y=220)
	lbl_certi = Label(app, text="FECHA DE CERTIFICACIÓN", bg="white", font=("calibri",14,"bold")).place(x=735, y=220)
	table = Table(app,10,3,v2)
	table.place(x=250, y=250)

class Table(tk.Frame):
	def __init__(self, master, row_count, column_count, v2):
		tk.Frame.__init__(self, master, background="black")
		f1=f2=f3=f4=f5=f6=f7=f8=f9=f10=f11=f12=f13=f14=StringVar()
		with open('import/datos.csv') as File:	
			reader = csv.reader(File, delimiter=',',quotechar=',',quoting=csv.QUOTE_MINIMAL)
			for elemento in reader:
				if v2.upper() == elemento[2]:
					f1=elemento[10];f2=elemento[11];f3=elemento[12];f4=elemento[13];f5=elemento[14];f6=elemento[15];f7=elemento[16];f8=elemento[17]
					f9=elemento[18];f10=elemento[19];f11=elemento[20];f12=elemento[21];f13=elemento[22];f14=elemento[23]
		File.close()
		self._cells = []
		lista = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14']
		calif = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14]
		fecha = []#[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14]
		for x in range(len(lista)):
			row = []
			label = tk.Label(self, text="Fase %s" % (lista[x]), bg="white", borderwidth=10, width=30)
			label.grid(row=x, column=0, sticky="nsew", padx=1, pady=1)
			label2 = tk.Label(self, text="Calificación %s" % (calif[x]), bg="white", borderwidth=10, width=30)
			label2.grid(row=x, column=1, sticky="nsew", padx=1, pady=1)
			#label3 = tk.Label(self, text="Fecha %s" % (fecha[x]), bg="white", borderwidth=10, width=30)
			#label3.grid(row=x, column=2, sticky="nsew", padx=1, pady=1)
			row.append(label)
			self._cells.append(row)

def examenes(n):
	def __Cancel(event=None): pass #Se usará para anular el botón Cerrar en la Ventana de Login
	#Creacion de la ventana
	cert = Tk()
	cert.geometry("900x500+450+200")
	cert.resizable(0,0)
	cert.title("Examen")
	cert.iconbitmap("logo2.ico")
	cert.config(bg="white")
	#Componentes de la Ventana
	tit = Label(cert, text="EJEMPLO DE EXAMEN", bg="white", font=("calibri",18,"bold")).place(x=400, y=20)
	nom = Label(cert, text="Nombre: ", bg="white", font=("calibri",14,"bold")).place(x=150, y=90)
	txt_nom = Label(cert)
	txt_nom.pack()
	txt_nom.place(x=230, y=90)
	txt_nom.config(text=n, fg="blue", bg="white", font=("calibri",14,"bold"))
	#Ventana de Acceso o Login
	autor = Toplevel()
	autor.geometry('450x250+700+300')
	autor.resizable(0,0)
	autor.title("Autorizar")
	#Las dos siguientes líneas se utilizan para anular el botón Cerrar de esta ventana
	autor.attributes("-toolwindow",-1)
	autor.protocol('WM_DELETE_WINDOW', __Cancel)
	#Componentes de la Ventana Login
	e1 = Label(autor, text="User / Nombre de quien autoriza: ", font=("calibri",14,"bold"))
	e2 = Label(autor, text="Password / Contraseña: ", font=("calibri",14,"bold"))
	usuario = StringVar()
	passw = StringVar()
	t1 = Entry(autor, textvariable=usuario, font=("calibri",14,"bold"), width=35)
	t2 = Entry(autor, textvariable=passw, font=("calibri",14,"bold"), width=35, show="*")
	b1 = Button(autor, text='Aceptar')
	b2 = Button(autor, text='Cancelar',command=quit)
	e1.place(x=30, y=25)
	e2.place(x=30, y=95)
	t1.place(x=50, y=55)
	t2.place(x=50, y=125)
	b1.place(x=120, y=180)
	b2.place(x=260, y=180)
	t1.focus_set()
	#Las siguientes dos líneas son para usar el Enter del teclado.
	#t2.bind('<Return>',self.onEnter)
	#b1.config(command=self.aceptar)
	#Las 3 líneas siguientes nos sirven para que no podamos hacer nada en la Ventana raíz hasta que nos logguemos
	autor.transient(master=examenes)
	autor.grab_set()
	examenes.wait_window(autor)
	#Cierra el ciclo del programa
	examenes.mainloop()

def activos(str):
	if str == "1":
		return "Activo"
	else:
		return "No activo"