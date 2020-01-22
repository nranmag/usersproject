import tkinter as tk
from tkinter import *
from tkinter import ttk, font
import getpass
from datetime import datetime, date, time, timedelta
from tkinter import messagebox
import csv, operator
import pandas as pd
import logging
from tkinter import scrolledtext
import os
from status import *
from certif import *

class Aplicacion():
	#Creando un Log del sistema donde registrará todos los eventos importantes y errores que arroje''''logs/registro.log'
	i = "logs/registro-"
	f = str(date.today())
	e = ".log"
	name = i + f + e
	logging.basicConfig(filename=name, format='%(asctime)s %(message)s', datefmt='%I:%M:%S %p',level=logging.DEBUG)
	logging.info("Iniciando el sistema")
	
	def __init__(self):
		def __Cancel(event=None): pass #Se usará para anular el botón Cerrar en la Ventana de Login
		self.raiz = Tk()
		#self.raiz.geometry('1900x1000+0+0')
		self.raiz.attributes('-fullscreen',True)
		self.raiz.resizable(0,0)
		self.raiz.minsize(400,300)
		self.raiz.title("Sistema de Usuarios")
		self.raiz.iconbitmap("logo2.ico")
		self.ifondo=PhotoImage(file="imagenes/IBM.png")
		Label(self.raiz, image=self.ifondo).place(x=0, y=0)
		self.fuente = font.Font(family='calibri', size=14, weight='bold')
		#Menú de la Ventana Principal
		menubar = Menu(self.raiz)
		self.raiz.config(menu=menubar)
		filemenu = Menu(menubar, tearoff=0)
		self.icoRegistrar = PhotoImage(file="imagenes/id16x16.png")
		self.icoBuscar = PhotoImage(file="imagenes/buscar16x16.png")
		self.icoSalir = PhotoImage(file="imagenes/salir16x16.png")
		self.icoSwitch = PhotoImage(file="imagenes/switch16x16.png")
		filemenu.config(font=("Calibri",12))
		filemenu.add_command(label="Registrar Usuario", command=self.registro, accelerator="Ctrl+N", image=self.icoRegistrar, compound=LEFT)
		filemenu.add_command(label="Buscar Usuario", command=self.opbuscar, accelerator="Ctrl+B", image=self.icoBuscar, compound=LEFT)
		filemenu.add_separator()
		filemenu.add_command(label="Cambiar de Usuario", command=self.switch, accelerator="Ctrl+U", image=self.icoSwitch, compound=LEFT)
		filemenu.add_command(label="Salir", command=self.quit, accelerator="Ctrl+S", image=self.icoSalir, compound=LEFT)
		toolmenu = Menu(menubar, tearoff=0)
		self.icoEditar = PhotoImage(file="imagenes/edit16x16.png")
		self.icoStatus = PhotoImage(file="imagenes/material16x16.png")
		toolmenu.config(font=("Calibri",12))
		toolmenu.add_command(label="Editar Usuario", command=lambda: self.edit, accelerator="Ctrl+E", image=self.icoEditar, compound=LEFT)
		toolmenu.add_separator()
		toolmenu.add_command(label="Status Activos", command=self.statusVent, accelerator="Ctrl+M", image=self.icoEditar, compound=LEFT)
		toolmenu.add_command(label="Certificaciones", command=self.examenes, compound=LEFT)
		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.config(font=("Calibri",12))
		helpmenu.add_command(label="Acerca de...", accelerator="Ctrl+C", command=self.ayuda)
		menubar.add_cascade(label="Usuarios", menu=filemenu)
		menubar.add_cascade(label="Herramientas", menu=toolmenu)
		menubar.add_cascade(label="Ayuda", menu=helpmenu)
		#Declaración de accesos rápidos
		self.raiz.bind("<Control-s>", lambda event: self.quit())
		self.raiz.bind("<Control-S>", lambda event: self.quit())
		self.raiz.bind("<Control-n>", lambda event: self.registro())
		self.raiz.bind("<Control-N>", lambda event: self.registro())
		self.raiz.bind("<Control-b>", lambda event: self.opbuscar())
		self.raiz.bind("<Control-B>", lambda event: self.opbuscar())
		self.raiz.bind("<Control-e>", lambda event: self.editar())
		self.raiz.bind("<Control-E>", lambda event: self.editar())
		self.raiz.bind("<Control-v>", lambda event: self.statusVent())
		self.raiz.bind("<Control-V>", lambda event: self.statusVent())
		self.raiz.bind("<Control-c>", lambda event: self.examenes())
		self.raiz.bind("<Control-C>", lambda event: self.examenes())
		#Barra de Herramientas
		self.btGuardar = PhotoImage(file="imagenes/id32x32.png")
		self.btBuscar = PhotoImage(file="imagenes/buscar32x32.png")
		self.btEditar = PhotoImage(file="imagenes/edit32x32.png")
		self.btGolden = PhotoImage(file="imagenes/golden32x32.png")
		self.btSalir = PhotoImage(file="imagenes/salir32x32.png")
		self.btSwitch = PhotoImage(file="imagenes/switch32x32.png")
		self.btExamenes = PhotoImage(file="imagenes/material32x32.png")
		self.barra = Frame(self.raiz, relief=RAISED, bd=2, bg="#E5E5E5")
		self.bot1 = Button(self.barra, image=self.btGuardar, command=self.registro)
		self.bot1.pack(side=LEFT, padx=1, pady=1)
		self.bot2 = Button(self.barra, image=self.btBuscar, command=self.opbuscar)
		self.bot2.pack(side=LEFT, padx=1, pady=1)
		self.bot3 = Button(self.barra, image=self.btEditar, command=lambda: self.editar())
		self.bot3.pack(side=LEFT, padx=1, pady=1)
		self.sepr = Label(self.barra, text="|", font=("Calibri",20))
		self.sepr.pack(side=LEFT, padx=10, pady=1)
		self.bot4 = Button(self.barra, image=self.btGolden, command=lambda: self.statusVent())
		self.bot4.pack(side=LEFT, padx=1, pady=1)
		self.sep1 = Label(self.barra, text="|", font=("Calibri",20))
		self.sep1.pack(side=LEFT, padx=10, pady=1)
		self.bot5 = Button(self.barra, image=self.btExamenes, command=self.examenes)
		self.bot5.pack(side=LEFT, padx=1, pady=1)
		self.bot6 = Button(self.barra, image=self.btSwitch, command=self.switch)
		self.bot6.pack(side=RIGHT, padx=1, pady=1)
		self.bot7 = Button(self.barra, image=self.btSalir, command=self.quit)
		self.bot7.pack(side=RIGHT, padx=1, pady=1)
		self.barra.pack(side=TOP, fill=X)
		#Ventana de Acceso o Login
		self.login = Toplevel()
		self.login.geometry('450x250+700+300')
		self.login.resizable(0,0)
		self.login.title("Login")
		#Las dos siguientes líneas se utilizan para anular el botón Cerrar de esta ventana
		self.login.attributes("-toolwindow",-1)
		self.login.protocol('WM_DELETE_WINDOW', __Cancel )
		#Componentes de la Ventana Login
		self.e1 = ttk.Label(self.login, text="User / Nombre de Usuario: ", font=self.fuente)
		self.e2 = ttk.Label(self.login, text="Password / Contraseña: ", font=self.fuente)
		self.mensaje = StringVar()
		self.e3 = ttk.Label(self.login, text="¿No tienes acceso? Registrate.")
		self.usuario = StringVar()
		self.passw = StringVar()
		self.t1 = ttk.Entry(self.login, textvariable=self.usuario, font=self.fuente, width=35)
		self.t2 = ttk.Entry(self.login, textvariable=self.passw, font=self.fuente, width=35, show="*")
		self.b1 = ttk.Button(self.login, text='Aceptar',padding=(5,5))
		self.b2 = ttk.Button(self.login, text='Cancelar',padding=(5,5),command=self.quit)
		self.e1.place(x=30, y=25)
		self.e2.place(x=30, y=95)
		self.t1.place(x=50, y=55)
		self.t2.place(x=50, y=125)
		self.b1.place(x=120, y=180)
		self.b2.place(x=260, y=180)
		self.e3.place(x=150, y=225)
		self.t1.focus_set()
		#Las siguientes dos líneas son para usar el Enter del teclado.
		self.t2.bind('<Return>',self.onEnter)
		self.b1.config(command=self.aceptar)
		#Las 3 líneas siguientes nos sirven para que no podamos hacer nada en la Ventana raíz hasta que nos logguemos
		self.login.transient(master=self.raiz)
		self.login.grab_set()
		self.raiz.wait_window(self.login)
		#Cierra el ciclo del programa
		self.raiz.mainloop()

	def aceptar(self):
		dicc = {'admin':'ZSE$7ujm','nahum':'n'}
		if self.usuario.get().lower() == "" or self.passw.get().lower() == "":
			logging.error("El campo usuario o password estan vacíos")
			messagebox.showerror("Incompleto","Favor de rellenar los campos")
		else:
			if self.usuario.get().lower() in dicc:
				valor = dicc.get(self.usuario.get().lower())
				if valor == None:
					logging.error("El usuario "+self.usuario.get()+" no existe")
					messagebox.showerror("No Existe","Este usuario no existe")
				elif valor != self.passw.get():
					logging.error(self.usuario.get()+" puso su password incorrecto")
					messagebox.showwarning("REVISAR","Por favor revisa tu password.")
				else:
					#Barra de Estado
					mensaje = "User: "+self.usuario.get().lower()+"  ::  "+str(datetime.now().strftime("%A %d %B %Y %I:%M"))
					self.barraest = Label(self.raiz, text=mensaje, bd=1, relief=SUNKEN, anchor=SE, font=("Calibri",14,"bold"))
					self.barraest.pack(side=BOTTOM, fill=X)
					logging.info("Entró "+self.usuario.get()+" como usuario ADMIN")
					self.login.destroy()
			else:
				#Login desde archivo
				encontrado = 0
				#Leer archivo para obtener datos
				with open('import/users.csv','r') as csvarchivo:
					entrada = csv.DictReader(csvarchivo)
					for reg in entrada:
						if self.usuario.get().lower() == reg['USER'] and self.passw.get().upper() != reg['PASSW']:
							logging.error("El usuario "+self.usuario.get()+" ingresó mal su password")
							messagebox.showerror("REVISA","Tu password es incorrecto")
							self.passw.set("")
							encontrado = 1
						if self.usuario.get().lower() == reg['USER'] and self.passw.get().upper() == reg['PASSW']:
							logging.info("Entrando con el user "+self.usuario.get()+" como USUARIO")
							v1 = self.usuario.get()
							v2 = self.passw.get()
							encontrado = 1
							self.usuario.set("")
							self.passw.set("")
							Aplicacion2(v1,v2)
				csvarchivo.close()
				if encontrado == 0:
					logging.error("El usuario "+self.usuario.get()+" no existe")
					messagebox.showerror("NO EXISTE","Este usuario no está registrado")
					self.usuario.set("")
					self.passw.set("")

	def onEnter(self, event):
		self.aceptar()

	def ayuda(self):
		messagebox.showinfo("Ayuda","Esta es la ayuda del Proyecto...\n\nMade by Nahum Rangel Magaña\n\n\t@ 2019")

	def statusVent(self):
		#Inicialización de Variables
		self.num_part = StringVar()
		self.op1 = IntVar()
		self.op2 = IntVar()
		self.op3 = IntVar()
		self.op4 = IntVar()
		self.op5 = IntVar()
		#Creacion de la ventana 
		self.statusv = Toplevel()
		self.statusv.geometry("650x850+500+100")
		self.statusv.resizable(0,0)
		self.statusv.title("Buscar")
		self.statusv.iconbitmap("logo2.ico")
		self.ibuscar = PhotoImage(file="imagenes/material.png")
		Label(self.statusv, image=self.ibuscar).place(x=30, y=35)
		#Componentes de la Ventana
		self.eti_tit = ttk.Label(self.statusv, text="BUSQUEDA DEL STATUS DE USERS", font=("calibri",18,"bold")).place(x=230, y=50)
		self.eti_filtro = ttk.Label(self.statusv, text="Selecciona el filtro a buscar:", font=("calibri",14,"bold")).place(x=250, y=100)
		self.opc1 = ttk.Checkbutton(self.statusv, text="Activos", variable=self.op1).place(x=190, y=140)
		self.opc2 = ttk.Checkbutton(self.statusv, text="Inactivos", variable=self.op2).place(x=260, y=140)
		self.opc3 = ttk.Checkbutton(self.statusv, text="Turno 1", variable=self.op3).place(x=330, y=140)
		self.opc4 = ttk.Checkbutton(self.statusv, text="Turno 2", variable=self.op4).place(x=400, y=140)
		self.opc5 = ttk.Checkbutton(self.statusv, text="Turno 3", variable=self.op5).place(x=470, y=140)
		self.bt_filtrar = ttk.Button(self.statusv, text=">>", command=self.btstatus).place(x=550, y=136)

	def btstatus(self):
		self.r = scrolledtext.ScrolledText(self.statusv, width=75, height=40)
		if self.op1.get() == 1:
			s = statusActivos()
			self.r.insert(INSERT,str(s))
		if self.op2.get() == 1:
			s = statusInactivos()
			self.r.insert(INSERT,str(s))
		if self.op3.get() == 1:
			s = statusTurno1()
			self.r.insert(INSERT,str(s))
		if self.op4.get() == 1:
			s = statusTurno2()
			self.r.insert(INSERT,str(s))
		if self.op5.get() == 1:
			s = statusTurno3()
			self.r.insert(INSERT,str(s))
		self.r.place(x=20, y=180)
		self.r.config(state=DISABLED)

	def btbuscar(self):
		c = 0
		print("El usuario a buscar por "+self.campo_buscar.get()+" es: "+self.buscar_per.get())
		logging.info("Se buscó la información de "+self.buscar_per.get())
		if self.buscar_per.get() == "":
			messagebox.showwarning("Datos incompletos","Por favor escribe el texto a buscar en el campo en blanco. Gracias")
			self.buscar.focus_set()
		else:
			#Apertura del Archivo
			with open('import/datos.csv') as File:	
				reader = csv.reader(File, delimiter=',',quotechar=',',quoting=csv.QUOTE_MINIMAL)
				for elemento in reader:
					if self.campo_buscar.get() == "User de Duluth":
						if self.buscar_per.get().lower() == elemento[1]:
							item = self.treeview.insert("", tk.END, text=elemento[1], values=(elemento[0],elemento[2],elemento[3],elemento[5],elemento[6],elemento[7],self.activos(elemento[8]),self.perman(elemento[9])), tags=("mytag",))
							logging.warning("La info se buscó por el campo User de Duluth")
							c=1
					if self.campo_buscar.get() == "Nombre":
						if self.buscar_per.get().upper() == elemento[3]:
							item = self.treeview.insert("", tk.END, text=elemento[1], values=(elemento[0],elemento[2],elemento[3],elemento[5],elemento[6],elemento[7],self.activos(elemento[8]),self.perman(elemento[9])), tags=("mytag",))
							logging.warning("La info se buscó por el campo Nombre")
							c=1
					if self.campo_buscar.get() == "User de MFS":
						if self.buscar_per.get().upper() == elemento[2]:
							item = self.treeview.insert("", tk.END, text=elemento[1], values=(elemento[0],elemento[2],elemento[3],elemento[5],elemento[6],elemento[7],self.activos(elemento[8]),self.perman(elemento[9])), tags=("mytag",))
							logging.warning("La info se buscó por el campo User de MFS")
							c=1
					if self.campo_buscar.get() == "Numero de Empleado":
						if self.buscar_per.get().upper() == elemento[0]:
							item = self.treeview.insert("", tk.END, text=elemento[1], values=(elemento[0],elemento[2],elemento[3],elemento[5],elemento[6],elemento[7],self.activos(elemento[8]),self.perman(elemento[9])), tags=("mytag",))
							logging.warning("La info se buscó por el campo Numero de empleado")
							c=1
			if c==0:
				print("Usuario "+self.buscar_per.get()+" no registrado en la DB.")
				messagebox.showerror("NO EXISTE","El user no existe, favor de intentar con otro user o registre primero este user")
				logging.warning("Se buscó información del usuario "+self.buscar_per.get()+" pero no esta registrado")
				self.buscar.focus_set()

	def activos(self,str):
		if str == "1":
			return "Activo"
		else:
			return "No activo"

	def perman(self,str):
		if str == "1":
			return "SI"
		else:
			return "NO"

	def noactivos(self,str):		
		if str == "Activo":
			return "1"
		else:
			return "0"

	def btregistrar(self):
		#Inicializar variable
		self.status = StringVar()
		#Mandar llamar la función Validar datos.
		self.valida_datos()
		#Obtencion de Datos para registrar validando los campos de Numero de empleado, Nombre y Compañía que deben estar rellenados
		if self.num_emp.get() != "" and self.nom_user.get() != "" and self.compania.get() != "":
			file = open('import/datos.csv','a', newline='')
			file.write("\n"+self.num_emp.get()+","+self.user_duluth.get().lower()+","+self.user_mfs.get().upper()+","+self.nom_user.get().upper()+","+self.day.get()+"/"+self.mes.get()+"/"+self.year.get()+","+self.user_rol.get()+","+self.compania.get()+","+self.turno.get()+",1,"+self.perma.get())
			file.close()
			logging.info("El archivo de datos se cerró")
			messagebox.showinfo("GUARDADO","La info fue guardada exitosamente")
			self.registrar.destroy()
			logging.warning("Se registró el Usuario con el Numero de empleado "+self.num_emp.get())
		else:
			messagebox.showerror("Falta rellenar","Por favor, al menos introduzca datos en los campos de: \n\n\t*Número de Empleado\n\t*Nombre\n\t*Compañía")
			self.registrar.focus_set()
			logging.error("No se rellenó correctamente los datos de: "+self.num_emp.get())

	def examenes(self):
		#Inicialización de Variables
		self.nomb = StringVar()
		self.usmfs = StringVar()
		self.fechai = StringVar()
		self.role = StringVar()
		self.statuse =StringVar()
		#Creacion de la ventana Registrar Material Golden
		self.certif = Toplevel()
		self.certif.geometry("900x500+500+200")
		self.certif.resizable(0,0)
		self.certif.title("Examen")
		self.certif.iconbitmap("logo2.ico")
		self.iregis = PhotoImage(file="imagenes/golden.png")
		Label(self.certif, image=self.iregis).place(x=20, y=5)
		#Componentes de la Ventana
		self.tit = ttk.Label(self.certif, text="EJEMPLO DE EXAMEN", font=("calibri",18,"bold")).place(x=400, y=20)
		self.dat = ttk.Label(self.certif, text="Datos generales: ", font=("calibri",16,"bold")).place(x=430, y=50)
		self.nom = ttk.Label(self.certif, text="Nombre: ", font=self.fuente).place(x=150, y=90)
		self.txt_nom = ttk.Entry(self.certif, textvariable=self.nomb, state='readonly', width=40, font=self.fuente).place(x=240, y=90)
		self.emp = ttk.Label(self.certif, text="User de MFS: ", font=self.fuente).place(x=660, y=90)
		self.txt_emp = ttk.Entry(self.certif, textvariable=self.usmfs, state='readonly', width=10, font=self.fuente).place(x=770, y=90)
		self.fec = ttk.Label(self.certif, text="Fecha de Ingreso: ", font=self.fuente).place(x=150, y=130)
		self.txt_fec = ttk.Entry(self.certif, textvariable=self.fechai, state='readonly', width=16, font=self.fuente).place(x=300, y=130)
		self.rol = ttk.Label(self.certif, text="Rol: ", font=self.fuente).place(x=500, y=130)
		self.txt_rol = ttk.Entry(self.certif, textvariable=self.role, state='readonly', width=10, font=self.fuente).place(x=540, y=130)
		self.stat = ttk.Label(self.certif, text="Status: ", font=self.fuente).place(x=690, y=130)
		self.txt_stat = ttk.Entry(self.certif, textvariable=self.statuse, state='readonly', width=10, font=self.fuente).place(x=770, y=130)
		self.cert = ttk.Label(self.certif, text="Tipo de Certificacion que realizará: ", font=self.fuente).place(x=50, y=170)
		self.cmb_cert = ttk.Combobox(self.certif, width=35, font=self.fuente, values=('Certificacion 1','Certificacion 2','Certificacion 3','Certificacion 4')).place(x=350, y=170)
		self.btdatos = ttk.Button(self.certif, text="Datos", command=self.btEx).place(x=800, y=170)
		self.pregunta()
		self.certif.focus_set()

	def pregunta(self):
		#Ventana para tomar dato
		self.p = Toplevel()
		self.p.geometry("350x150+800+450")
		self.p.resizable(0,0)
		self.p.title("Certificaciones")
		self.ipre = PhotoImage(file="imagenes/edit.png")
		Label(self.p, image=self.ipre).place(x=30, y=35)
		#Variables
		self.dato = StringVar()
		#Etiqueta y cuadro de texto
		self.pre = ttk.Label(self.p, text="Escribe el User de la persona: ", font=("calibri",15,"bold")).place(x=50, y=30)
		self.txt_pre = ttk.Entry(self.p, textvariable=self.dato, width=30, font=self.fuente).place(x=30, y=60)
		self.bt_ok = ttk.Button(self.p, text="Ok", command=self.btEx).place(x=100, y=100)
		self.bt_ok = ttk.Button(self.p, text="Cancelar", command=self.p.destroy).place(x=200, y=100)

	def btEx(self):
		#self.nomb.set(self.dato.get())
		if self.dato.get() == "":
			messagebox.showwarning("Datos incompletos","Por favor escribe el texto a buscar en el campo en blanco. Gracias")
			self.p.focus_set()
		else:
			with open('import/datos.csv') as File:	
				reader = csv.reader(File, delimiter=',',quotechar=',',quoting=csv.QUOTE_MINIMAL)
				for elemento in reader:
					if self.dato.get().upper() == elemento[2]:
						self.nomb.set(elemento[3]),self.usmfs.set(elemento[2]),self.fechai.set(elemento[4]),self.role.set(elemento[5]),self.statuse.set(self.activos(elemento[8]))
						cadena = elemento
			self.p.destroy()

	def editar(self):
		#Creacion de la ventana Editar User
		self.edit = Toplevel()
		self.edit.geometry("730x460+600+300")
		self.edit.resizable(0,0)
		self.edit.title("Editar")
		self.edit.iconbitmap("logo2.ico")
		self.edit.configure(background="white")
		self.iedit = PhotoImage(file="imagenes/edit.png")
		Label(self.edit, image=self.iedit, background="white").place(x=30, y=80)
		self.btBus = PhotoImage(file="imagenes/b16x16.png")
		#Inicialización de variables
		self.txt = StringVar()
		self.num = StringVar()
		self.nom = StringVar()
		self.usm = StringVar()
		self.usd = StringVar()
		self.fei = StringVar()
		self.tur = StringVar()
		self.sta = StringVar()
		self.rol = StringVar()
		self.com = StringVar()
		self.per = StringVar()
		#Componentes de la Ventana
		self.lbltit = ttk.Label(self.edit, text="EDITAR USUARIO", foreground="blue", background="white", font=("calibri",28,"bold")).place(x=290, y=20)
		self.lblTxt = ttk.Label(self.edit, text="Texto a buscar: ", background="white",font=self.fuente).place(x=240, y=90)
		self.txtTxt = ttk.Entry(self.edit, textvariable=self.txt, width=25, font=self.fuente).place(x=380, y=90)
		self.btIr = ttk.Button(self.edit, text=">>>", command=self.btE, image=self.btBus).place(x=650, y=91)
		self.lblNum = ttk.Label(self.edit, text="Número de Empleado: ", background="white", font=self.fuente).place(x=180, y=140)
		self.txtNum = ttk.Entry(self.edit, textvariable=self.num, width=29, font=self.fuente).place(x=380, y=140)
		self.lblNom = ttk.Label(self.edit, text="Nombre: ", background="white", font=self.fuente).place(x=180, y=190)
		self.txtNom = ttk.Entry(self.edit, textvariable=self.nom, width=40, font=self.fuente).place(x=270, y=190)
		self.lblUsM = ttk.Label(self.edit, text="User de MFS: ", background="white", font=self.fuente).place(x=50, y=240)
		self.txtUsM = ttk.Entry(self.edit, textvariable=self.usm, width=18, font=self.fuente).place(x=180, y=240)
		self.lblUsD = ttk.Label(self.edit, text="User de Duluth: ", background="white", font=self.fuente).place(x=380, y=240)
		self.txtUsD = ttk.Entry(self.edit, textvariable=self.usd, width=15, font=self.fuente).place(x=520, y=240)
		self.lblFeI = ttk.Label(self.edit, text="Fecha de ingreso: ", background="white", font=self.fuente).place(x=50, y=290)
		self.txtFeI = ttk.Entry(self.edit, textvariable=self.fei, width=15, font=self.fuente).place(x=220, y=290)
		self.lblCom = ttk.Label(self.edit, text="Compañia: ", background="white", font=self.fuente).place(x=420, y=290)
		self.txtCom = ttk.Entry(self.edit, textvariable=self.com, width=15, font=self.fuente).place(x=520, y=290)
		self.lblRol = ttk.Label(self.edit, text="Rol: ", background="white", font=self.fuente).place(x=50, y=340)
		self.txtRol = ttk.Entry(self.edit, textvariable=self.rol, width=12, font=self.fuente).place(x=100, y=340)	
		self.lblTur = ttk.Label(self.edit, text="Turno: ", background="white", font=self.fuente).place(x=250, y=340)
		self.txtTur = ttk.Entry(self.edit, textvariable=self.tur, width=12, font=self.fuente).place(x=310, y=340)
		self.lblSta = ttk.Label(self.edit, text="Status: ", background="white", font=self.fuente).place(x=450, y=340)
		self.txtSta = ttk.Entry(self.edit, textvariable=self.sta, width=12, font=self.fuente).place(x=550, y=340)
		self.lblPer = ttk.Label(self.edit, text="Permanencia: ", background="white", font=self.fuente).place(x=50, y=390)
		self.txtPer = ttk.Entry(self.edit, textvariable=self.per, width=12, font=self.fuente).place(x=180, y=390)
		self.edit.focus_set()

	def btE(self):
		#Inicializacion de Variables
		cadena = ""
		self.btMod = ttk.Button(self.edit, text="Guardar", command=lambda: self.modificar(cadena)).place(x=600, y=400)
		print("El usuario a editar es "+self.txt.get())
		#Apertura del Archivo
		if self.txt.get() == "":
			messagebox.showwarning("Datos incompletos","Por favor escribe el texto a buscar en el campo en blanco. Gracias")
		else:
			with open('import/datos.csv') as File:	
				reader = csv.reader(File, delimiter=',',quotechar=',',quoting=csv.QUOTE_MINIMAL)
				for elemento in reader:
					if self.txt.get().upper() == elemento[0]:
						self.num.set(elemento[0]),self.nom.set(elemento[3]),self.usm.set(elemento[2]),self.usd.set(elemento[1]),self.fei.set(elemento[4]),self.rol.set(elemento[5]),self.com.set(elemento[6]),self.tur.set(elemento[7]),self.sta.set(self.activos(elemento[8])),self.per.set(self.perman(elemento[9]))
						cadena = elemento
					elif self.txt.get().lower() == elemento[1]:
						self.num.set(elemento[0]),self.nom.set(elemento[3]),self.usm.set(elemento[2]),self.usd.set(elemento[1]),self.fei.set(elemento[4]),self.rol.set(elemento[5]),self.com.set(elemento[6]),self.tur.set(elemento[7]),self.sta.set(self.activos(elemento[8])),self.per.set(self.perman(elemento[9]))
						cadena = elemento
						print(elemento)
					elif self.txt.get().upper() == elemento[2]:
						self.num.set(elemento[0]),self.nom.set(elemento[3]),self.usm.set(elemento[2]),self.usd.set(elemento[1]),self.fei.set(elemento[4]),self.rol.set(elemento[5]),self.com.set(elemento[6]),self.tur.set(elemento[7]),self.sta.set(self.activos(elemento[8])),self.per.set(self.perman(elemento[9]))
						cadena = elemento
			File.close()
			if cadena == "":
				messagebox.showerror("INEXISTENTE","No EXISTE el user, favor de buscar de nuevo")
				print("No existe el usuario "+self.txt.get())
				logging.info("Se buscó el user "+self.txt.get()+" pero no está registrado en la BD")
			
	def modificar(self,cadena):
		cadena2 = cadena
		logging.info("Datos originales: "+str(cadena))
		if self.num.get() != cadena[0]:
			print("Se modificó el campo Numero de empleado")
			cadena2[0] = self.num.get()
			logging.info("Datos despues de modificar el Num de Empleado: "+str(cadena2))
		if self.usd.get() != cadena[1]:
			print("Se modificó el campo Usuario de Duluth")
			cadena2[1] = self.usd.get()
			logging.info("Datos despues de modificar el User de Duluth: "+str(cadena2))
		if self.usm.get() != cadena[2]:
			print("Se modificó el campo Usuario de MFS")
			cadena2[2] = self.usm.get()
			logging.info("Datos despues de modificar el User de MFS: "+str(cadena2))
		if self.nom.get() != cadena[3]:
			print("Se modificó el campo Nombre de empleado")
			cadena2[3] = self.nom.get()
			logging.info("Datos despues de modificar el Nombre: "+str(cadena2))
		if self.fei.get() != cadena[4]:
			print("Se modificó el campo Fecha de ingreso")
			cadena2[4] = self.fei.get()
			logging.info("Datos despues de modificar a fecha: "+str(cadena2))
		if self.rol.get() != cadena[5]:
			print("Se modificó el campo Rol del empleado")
			cadena2[5] = self.rol.get()
			logging.info("Datos despues de modificar el Rol: "+str(cadena2))
		if self.com.get() != cadena[6]:
			print("Se modificó el campo Compañia")
			cadena2[6] = self.com.get()
			logging.info("Datos despues de modificar la Compañía: "+str(cadena2))
		if self.tur.get() != cadena[7]:
			print("Se modificó el campo Turno del empleado")
			cadena2[7] = self.tur.get()
			logging.info("Datos despues de modificar el Turno: "+str(cadena2))
		if self.sta.get() != self.activos(cadena[8]):
			print("Se modificó el campo Status del empleado")
			cadena2[8] = self.noactivos(self.sta.get())
			logging.info("Datos despues de modificar el Status: "+str(cadena2))
		r = messagebox.askyesnocancel("Modificar","¿Realmente quieres modificar este registro?")
		if r == TRUE:
			#condiciones
			archivo = open('import/datos.csv')
			data = csv.reader(archivo)
			df = pd.DataFrame(data, columns=['NUM_EMP','USER_DUL','USER_MFS','NOMBRE','FECHA_IN','ROL','COMPANIA','TURNO','STATUS','PERMA','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14'])
			archivo.close()
			linea = df.loc[df['NUM_EMP'] == self.num.get()]
			dfnew = pd.DataFrame(df.drop([linea.index[0]],inplace=False))
			dfnew.to_csv('import/datos2.csv', index = None, header = None, encoding='utf-8')
			file = open('import/datos2.csv','a', encoding='utf_8_sig')
			file.write(self.num.get()+","+self.usd.get().lower()+","+self.usm.get().upper()+","+self.nom.get().upper()+","+self.fei.get()+","+self.rol.get()+","+self.com.get()+","+self.tur.get()+","+self.noactivos(self.sta.get()))
			file.close()
			os.remove('import/datos.csv')
			os.rename('import/datos2.csv','import/datos.csv')
			logging.info("Se hacen las modificaciones del usuario con Numero de empleado "+self.num.get()+" y se cierran los archivos satisfactoriamente.")
			self.edit.destroy()
			
	def opbuscar(self):
		#Inicialización de Variables
		self.campo_buscar = StringVar()
		self.buscar_per = StringVar()
		self.btBus = PhotoImage(file="imagenes/b16x16.png")
		#Creacion de la ventana Buscar un User
		self.buscar = Toplevel()
		self.buscar.geometry("1030x460+550+100")
		self.buscar.title("Buscar")
		self.buscar.iconbitmap("logo2.ico")
		self.ibuscar = PhotoImage(file="imagenes/buscar.png")
		Label(self.buscar, image=self.ibuscar).place(x=40, y=35)
		#Componentes de la Ventana
		self.campo_buscar.set("User de Duluth")
		self.eti_tit = ttk.Label(self.buscar, text="BUSQUEDA DE USUARIO", foreground="blue", font=("calibri",30,"bold")).place(x=350, y=20)
		self.eti_buscar = ttk.Label(self.buscar, text=" Buscar por: ", font=self.fuente).place(x=375, y=103)
		self.combo_buscar = ttk.Combobox(self.buscar, textvariable=self.campo_buscar, values=("User de Duluth","Nombre","Numero de Empleado","User de MFS"), font=self.fuente, width=23).place(x=480, y=100)
		self.eti_text = ttk.Label(self.buscar, text="Texto a buscar: ", font=self.fuente).place(x=345, y=134)
		self.txt_buscar = ttk.Entry(self.buscar, textvariable=self.buscar_per, font=("calibri",14), width=22).place(x=480, y=131)
		self.bt_buscar = ttk.Button(self.buscar, image=self.btBus, command=self.btbuscar, width=5).place(x=706, y=133)
		#Creación del Estilo para el Treeview(Vista árbol)
		self.styletree = ttk.Style()
		self.styletree.configure("mystyle.Treeview", highlighthickness=0, bd=0, font=("calibri",13))
		self.styletree.configure("mystyle.Treeview.Heading", font=("calibri",14,"bold"))
		#Creación del Treeview(Vista árbol)
		self.treeview = ttk.Treeview(self.buscar, columns=("1","2","3","4","5","6","7","8"), style="mystyle.Treeview")
		self.treeview.place(x=20, y=200)
		self.treeview.heading("#0", text="Duluth user")
		self.treeview.heading("1", text="Número ID")
		self.treeview.heading("2", text="MFS user")
		self.treeview.heading("3", text="Nombre")
		self.treeview.heading("4", text="Rol")
		self.treeview.heading("5", text="Compañía")
		self.treeview.heading("6", text="Turno")
		self.treeview.heading("7", text="Status")
		self.treeview.heading("8", text="Perma")
		self.treeview.column("#0", width=100, minwidth=100, stretch=tk.NO)
		self.treeview.column("1", width=100, minwidth=100, stretch=tk.NO)
		self.treeview.column("2", width=100, minwidth=100, stretch=tk.NO)
		self.treeview.column("3", width=300, minwidth=300)
		self.treeview.column("4", width=90, minwidth=90, stretch=tk.NO)
		self.treeview.column("5", width=90, minwidth=90, stretch=tk.NO)
		self.treeview.column("6", width=70, minwidth=70, stretch=tk.NO)
		self.treeview.column("7", width=70, minwidth=70, stretch=tk.NO)
		self.treeview.column("8", width=70, minwidth=70, stretch=tk.NO)
		#Creación de etiqueta Seleccionado
		self.treeview.tag_bind("mytag", "<<TreeviewSelect>>",self.item_selected)
		self.buscar.focus_set()

	def item_selected(self, event):
		self.txtbus = self.buscar_per.get()
		self.bt_editar = ttk.Button(self.buscar, text="Abrir la ventana de Editar", command=lambda: self.editar()).place(x=800, y=430)
		print("Se seleccionó el usuario: "+self.txtbus)
		logging.info("Se buscó la información de: "+self.txtbus)
		return self.txtbus

	def quit(self):
		#Preguntará si quiere cerrar el Programa
		r = messagebox.askyesnocancel("Salir","¿Realmente quieres salir?")
		if r == TRUE:
			self.raiz.destroy()
			logging.info("Sistema cerrado y saliendo...")

	def registro(self):
		#Inicialización de Variables
		self.num_emp = StringVar()
		self.user_duluth = StringVar()
		self.user_mfs = StringVar()
		self.nom_user = StringVar()
		self.user_rol = StringVar()
		self.user_rol.set("TA")
		self.compania = StringVar()
		self.turno = StringVar()
		self.perma = StringVar()
		self.perma.set(False)
		#Creacion de la ventana Registrar User
		self.registrar = Toplevel()
		self.registrar.geometry("600x350+50+100")
		self.registrar.resizable(0,0)
		self.registrar.title("Registrar")
		self.registrar.iconbitmap("logo2.ico")
		self.iregis = PhotoImage(file="imagenes/candidate.png")
		Label(self.registrar, image=self.iregis).place(x=20, y=5)
		#Componentes de la Ventana
		self.eti_tit = ttk.Label(self.registrar, text="REGISTRO DE USUARIOS ", font=("calibri",18,"bold")).place(x=220, y=35)
		self.eti_msj = ttk.Label(self.registrar, text="* Campos requeridos").place(x=290, y=75)
		self.eti_num = ttk.Label(self.registrar, text="*Número de Empleado", font=self.fuente).place(x=20, y=140)
		self.txt_num = ttk.Entry(self.registrar, textvariable=self.num_emp, width=16, font=self.fuente).place(x=40, y=165)
		self.eti_dul = ttk.Label(self.registrar, text="Usuario de Duluth", font=self.fuente).place(x=215, y=140)
		self.txt_dul = ttk.Entry(self.registrar, textvariable=self.user_duluth, width=16, font=self.fuente).place(x=225, y=165)
		self.eti_mfs = ttk.Label(self.registrar, text="Usuario de MFS", font=self.fuente).place(x=400, y=140)
		self.txt_mfs = ttk.Entry(self.registrar, textvariable=self.user_mfs, width=16, font=self.fuente).place(x=410, y=165)
		self.eti_nom = ttk.Label(self.registrar, text="*Nombre ", font=self.fuente).place(x=20, y=210)
		self.txt_nom = ttk.Entry(self.registrar, textvariable=self.nom_user, width=46, font=self.fuente).place(x=110, y=210)
		self.eti_fechain = ttk.Label(self.registrar, text="Fecha de ingreso ", font=self.fuente).place(x=20, y=260)
		d=IntVar()
		m=StringVar()
		y=IntVar()
		d.set(datetime.now().strftime("%d"))
		m.set(datetime.now().strftime("%m"))
		y.set(datetime.now().strftime("%Y"))
		self.day = Spinbox(self.registrar, from_=1, to=31, width=3, textvariable=d)
		self.day.place(x=167, y=260)
		self.day.config(font=("calibri",14))
		self.mes = Spinbox(self.registrar, from_=1, to=12, width=4, textvariable=m)
		self.mes.place(x=220, y=260)
		self.mes.config(font=("calibri",14))
		self.year = Spinbox(self.registrar, from_=2013, to=2025, width=5, textvariable=y)
		self.year.place(x=285, y=260)
		self.year.config(font=("calibri",14))
		self.eti_com = ttk.Label(self.registrar, text="*Compañía ", font=self.fuente).place(x=390, y=260)
		self.rbcomage = ttk.Radiobutton(self.registrar, text="IBM", variable=self.compania, value="IBM").place(x=480, y=265)
		self.rbcomibm = ttk.Radiobutton(self.registrar, text="Kelly", variable=self.compania, value="Kelly").place(x=525, y=265)
		self.eti_rol = ttk.Label(self.registrar, text="Rol ", font=self.fuente).place(x=20, y=310)
		self.rolcb = ttk.Combobox(self.registrar, textvariable=self.user_rol, values=("TA","TT","ESP","TA Lead","TA Trainer"), font=("calibri",14), width=8).place(x=60, y=310)
		self.eti_turno = ttk.Label(self.registrar, text="Turno", font=self.fuente).place(x=180, y=310)
		self.rbturn1 = ttk.Radiobutton(self.registrar, text="1", variable=self.turno, value="1").place(x=230, y=315)
		self.rbturn2 = ttk.Radiobutton(self.registrar, text="2", variable=self.turno, value="2").place(x=260, y=315)
		self.rbturn3 = ttk.Radiobutton(self.registrar, text="3", variable=self.turno, value="3").place(x=290, y=315)
		self.eti_perma = ttk.Label(self.registrar, text="Permanencia", font=self.fuente).place(x=335, y=310)
		self.perm = ttk.Checkbutton(self.registrar, variable=self.perma).place(x=450, y=315)
		self.btregis = ttk.Button(self.registrar, text="Registrar", padding=(5,5), command=self.btregistrar).place(x=490, y=300)
		self.registrar.focus_set()

	def switch(self):
		#Cambio de Usuario
		self.quit()
		main()

	def valida_datos(self):
		#Validación de los campos Numero de Empleado y Compañía
		c = StringVar()
		c = self.num_emp.get()
		if self.compania.get() == "Kelly":
			n=self.num_emp.get().isdigit()
			if n == False or len(c) != 8:
				messagebox.showerror("INCORRECTO","El Número de Empleado debe ser de 8 dígitos y sólo números")
				self.num_emp.set("")
				logging.error("El campo Numero de empleado no se ha rellenado correctamente")
		elif self.compania.get() == "IBM":
			n=self.num_emp.get().isalnum()
			print(n)
			if n == False or len(c) > 6:
				messagebox.showerror("INCORRECTO","El Número de Empleado debe ser de 6 caracteres alfanuméricos")
				self.num_emp.set("")
				logging.error("El campo Numero de empleado no se ha rellenado correctamente")
		else:
			messagebox.showerror("Seleccionar","Favor de Seleccionar la Compañía")
			logging.error("El campo Compañia no ha sido rellenado")
		#Validación de los Campos User de Duluth y MFS
		d = StringVar()
		m = StringVar()
		d = self.user_duluth.get() 
		m = self.num_emp.get()
		print(d+" , "+m)
		data = pd.read_csv('import/datos.csv', encoding="ISO-8859–1")
		df = pd.DataFrame(data)
		print(df)
		resd = df[df['USER_DUL'].str.contains(d, case=False)]
		resm = df[df['NUM_EMP'].str.contains(m, case=False)]
		print(resd)
		print(resm)
		if len(d) > 8 or len(m) > 8:
			messagebox.showerror("Verificar","Favor de checar que los usuarios de Duluth y MFS sean MÁXIMO de 8 caracteres.")
			logging.error("Uno de los campos User de Duluth o MFS no son de la longitud correcta")
			self.num_emp.set("")
		if any(resd['USER_DUL'] == d):
			messagebox.showerror("EXISTE","El usuario "+d.upper()+" ya existe\nFavor de utilizar otro")
			self.num_emp.set("")
			logging.error("El User de Duluth "+d.upper()+" ya está registrado")
		if any(resm['NUM_EMP'] == m):
			messagebox.showerror("EXISTE","El usuario "+m.upper()+" ya existe\nFavor de utilizar otro")
			self.num_emp.set("")
			logging.error("El numero de empleado "+m.upper()+" ya está registrado")


def main():
	inicio = Aplicacion()
	return(0)

if __name__ == '__main__':
	main()