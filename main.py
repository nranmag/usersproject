import tkinter as tk
from tkinter import *
from tkinter import ttk, font
import getpass
from datetime import datetime, date, time, timedelta
import calendar
from tkinter import messagebox
import csv, operator
import pandas as pd
import logging
from tkinter import scrolledtext

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
		self.raiz.geometry('1900x1000+0+0')
		#self.raiz.attributes('-fullscreen',True)
		self.raiz.resizable(0,0)
		self.raiz.minsize(400,300)
		self.raiz.title("Sistema de Usuarios")
		self.raiz.iconbitmap("../logo2.ico")
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
		goldenmenu = Menu(menubar, tearoff=0)
		self.icoGolden = PhotoImage(file="imagenes/golden16x16.png")
		self.icoMaterial = PhotoImage(file="imagenes/material16x16.png")
		goldenmenu.config(font=("Calibri",12))
		goldenmenu.add_command(label="Registrar Material Golden", command=self.golden, accelerator="Ctrl+M", image=self.icoGolden, compound=LEFT)
		goldenmenu.add_command(label="Buscar PN Golden", command=self.bgolden, accelerator="Ctrl+G", image=self.icoMaterial, compound=LEFT)
		toolmenu = Menu(menubar, tearoff=0)
		self.icoEditar = PhotoImage(file="imagenes/edit16x16.png")
		toolmenu.config(font=("Calibri",12))
		toolmenu.add_command(label="Editar Usuario", command=self.editar, accelerator="Ctrl+E", image=self.icoEditar, compound=LEFT)
		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.config(font=("Calibri",12))
		helpmenu.add_command(label="Acerca de...", accelerator="Ctrl+C", command=self.ayuda)
		menubar.add_cascade(label="Usuarios", menu=filemenu)
		menubar.add_cascade(label="Herramientas", menu=toolmenu)
		menubar.add_cascade(label="Material Golden", menu=goldenmenu)
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
		self.raiz.bind("<Control-m>", lambda event: self.golden())
		self.raiz.bind("<Control-M>", lambda event: self.golden())
		self.raiz.bind("<Control-G>", lambda event: self.bgolden())
		self.raiz.bind("<Control-g>", lambda event: self.bgolden())
	#Barra de Herramientas
		self.btGuardar = PhotoImage(file="imagenes/id32x32.png")
		self.btBuscar = PhotoImage(file="imagenes/buscar32x32.png")
		self.btEditar = PhotoImage(file="imagenes/edit32x32.png")
		self.btGolden = PhotoImage(file="imagenes/golden32x32.png")
		self.btMaterial = PhotoImage(file="imagenes/material32x32.png")
		self.btSalir = PhotoImage(file="imagenes/salir32x32.png")
		self.btSwitch = PhotoImage(file="imagenes/switch32x32.png")
		self.barra = Frame(self.raiz, relief=RAISED, bd=2, bg="#E5E5E5")
		self.bot1 = Button(self.barra, image=self.btGuardar, command=self.registro)
		self.bot1.pack(side=LEFT, padx=1, pady=1)
		self.bot2 = Button(self.barra, image=self.btBuscar, command=self.opbuscar)
		self.bot2.pack(side=LEFT, padx=1, pady=1)
		self.bot3 = Button(self.barra, image=self.btEditar, command=self.editar)
		self.bot3.pack(side=LEFT, padx=1, pady=1)
		self.sepr = Label(self.barra, text="|", font=("Calibri",20))
		self.sepr.pack(side=LEFT, padx=10, pady=1)
		self.bot4 = Button(self.barra, image=self.btGolden, command=self.golden)
		self.bot4.pack(side=LEFT, padx=1, pady=1)
		self.bot5 = Button(self.barra, image=self.btMaterial, command=self.bgolden)
		self.bot5.pack(side=LEFT, padx=1, pady=1)
		self.bot6 = Button(self.barra, image=self.btSwitch, command=self.switch)
		self.bot6.pack(side=RIGHT, padx=1, pady=1)
		self.bot7 = Button(self.barra, image=self.btSalir, command=self.quit)
		self.bot7.pack(side=RIGHT, padx=1, pady=1)
		self.barra.pack(side=TOP, fill=X)
	#Calendario
		'''y = date.today().year 
		m = date.today().month
		calendario_mes = calendar.month(y,m)
		self.cal = ttk.Label(self.raiz, text=calendario_mes)
		self.cal.place(x=1750,y=100)'''
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

	#Login desde archivo
	'''def aceptar(self):
	#Leer archivo para obtener datos
		with open('import/admin.csv') as csvarchivo:
			entrada = csv.reader(csvarchivo)
			for reg in entrada:
				u = StringVar()
				p = StringVar()
				u = reg[0]
				p = reg[1]
			#Obtencion de datos para validar
				if self.usuario.get().lower() == u and self.passw.get().lower() == p:
					#Barra de Estado
					mensaje = "User: "+self.usuario.get().lower()+"  ::  "+str(datetime.now().strftime("%A %d %B %Y %I:%M"))
					self.barraest = Label(self.raiz, text=mensaje, bd=1, relief=SUNKEN, anchor=SE, font=("Calibri",14,"bold"))
					self.barraest.pack(side=BOTTOM, fill=X)
					logging.info("Entrando como "+self.usuario.get())
					print("El archivo admin fue cerrado con éxito...")
					self.login.destroy()
				else:
					logging.error("El nombre o password del usuario "+self.usuario.get()+" está intentando logguearse")
					self.e3.configure(foreground='red')
					self.mensaje.set("Access denied / Acceso No permitido")
		del u, p
		csvarchivo.close()
		del csvarchivo
	'''
	def aceptar(self):
		dicc = {'admin':'admin','nahumra':'nrm19nrm','josecard':'ibm33ibm'}
		if self.usuario.get().lower() == "" or self.passw.get().lower() == "":
			logging.error("El campo usuario o password estan vacíos")
			messagebox.showerror("Incompleto","Favor de rellenar los campos")
		else:
			valor = dicc.get(self.usuario.get().lower())
			if valor == None:
				logging.error("El usuario "+self.usuario.get()+" no existe")
				messagebox.showerror("No Existe","Este usuario no existe")
			elif valor != self.passw.get().lower():
				logging.error(self.usuario.get()+" puso su password incorrecto")
				messagebox.showwarning("REVISAR","Por favor revisa tu password.")
			else:
				#Barra de Estado
				mensaje = "User: "+self.usuario.get().lower()+"  ::  "+str(datetime.now().strftime("%A %d %B %Y %I:%M"))
				self.barraest = Label(self.raiz, text=mensaje, bd=1, relief=SUNKEN, anchor=SE, font=("Calibri",14,"bold"))
				self.barraest.pack(side=BOTTOM, fill=X)
				logging.info("Entrando como "+self.usuario.get())
				self.login.destroy()

	def onEnter(self, event):
		self.aceptar()

	def ayuda(self):
		messagebox.showinfo("Ayuda","Esta es la ayuda del Proyecto...\n\nMade by Nahum Rangel Magaña\n\n\t@ 2019")

	def bgolden(self):
	#Inicialización de Variables
		self.num_part = StringVar()
	#Creacion de la ventana Buscar un PN
		self.b_golden = Toplevel()
		self.b_golden.geometry("650x850+500+100")
		self.b_golden.resizable(0,0)
		self.b_golden.title("Buscar")
		self.b_golden.iconbitmap("../logo2.ico")
		self.ibuscar = PhotoImage(file="imagenes/material.png")
		Label(self.b_golden, image=self.ibuscar).place(x=30, y=35)
	#Componentes de la Ventana
		self.eti_tit = ttk.Label(self.b_golden, text="BUSQUEDA DE MATERIAL GOLDEN", font=("calibri",18,"bold")).place(x=230, y=50)
		self.eti_pn = ttk.Label(self.b_golden, text="Número de Parte", font=("calibri",14,"bold")).place(x=330, y=100)
		self.txt_buscar = ttk.Entry(self.b_golden, textvariable=self.num_part, font=("calibri",14), width=14).place(x=330, y=131)
		self.bt_buscar = ttk.Button(self.b_golden, text="Buscar", command=self.buscar_golden).place(x=480, y=136)
		self.r = scrolledtext.ScrolledText(self.b_golden, width=75, height=40)
		with open('import/golden.csv') as File:	
			reader = csv.reader(File, delimiter=',',quotechar=',',quoting=csv.QUOTE_MINIMAL)
			for elemento in reader:
				self.r.insert(INSERT,elemento[0]+"\t\t"+elemento[1]+"\t\t\t"+elemento[2]+"\t\t"+elemento[4]+"\n")
			logging.info("El archivo de material golden fue cerrado con éxito...")
		self.r.place(x=20, y=180)
		self.r.config(state=DISABLED)	

	def btbuscar(self):
		print("El usuario a buscar por "+self.campo_buscar.get()+" es "+self.buscar_per.get())
		logging.info("Se buscó la información de "+self.buscar_per.get())
	#Apertura del Archivo
		if self.buscar_per.get() == "":
			messagebox.showwarning("Datos incompletos","Por favor escribe el texto a buscar en el campo en blanco. Gracias")
			self.buscar.focus_set()
		else:
			with open('import/datos.csv') as File:	
				reader = csv.reader(File, delimiter=',',quotechar=',',quoting=csv.QUOTE_MINIMAL)
				for elemento in reader:
					if self.campo_buscar.get() == "User de Duluth":
						if self.buscar_per.get().lower() == elemento[1]:
							item = self.treeview.insert("", tk.END, text=elemento[1], values=(elemento[0],elemento[2],elemento[3],elemento[5],elemento[6],elemento[7]), tags=("mytag",))
							logging.warning("Se buscó la info por el campo User de Duluth")
					elif self.campo_buscar.get() == "Nombre":
						if self.buscar_per.get().upper() == elemento[3]:
							item = self.treeview.insert("", tk.END, text=elemento[1], values=(elemento[0],elemento[2],elemento[3],elemento[5],elemento[6],elemento[7]))
							logging.warning("Se buscó la info por el campo Nombre")
					elif self.campo_buscar.get() == "User de MFS":
						if self.buscar_per.get().upper() == elemento[2]:
							item = self.treeview.insert("", tk.END, text=elemento[1], values=(elemento[0],elemento[2],elemento[3],elemento[5],elemento[6],elemento[7]))
							logging.warning("Se buscó la info por el campo User de MFS")
					elif self.campo_buscar.get() == "Numero de Empleado":
						if self.buscar_per.get().upper() == elemento[0]:
							item = self.treeview.insert("", tk.END, text=elemento[1], values=(elemento[0],elemento[2],elemento[3],elemento[5],elemento[6],elemento[7]))
							logging.warning("Se buscó la info por el campo Numero de empleado")
		#self.buscar_per.set("")

	def btgolden(self):
	#Mandar llamar la función Validar datos del Material Golden.
		#self.valida_material()
	#Obtencion de Datos para registrar validando los campos de Número de Parte, Descripción y Cantidad que deben estar rellenados
		if self.np.get() != "" and self.descripcion.get() != "" and self.cantidad.get() != "":
			file = open('import/golden.csv','a', newline='')
			file.write("\n"+self.np.get()+","+self.descripcion.get()+","+self.cantidad.get()+","+self.gday.get()+"/"+self.gmes.get()+"/"+self.gyear.get()+","+self.bads.get())
			file.close()
			print("El archivo de material golden fue cerraro con éxito...")
			messagebox.showinfo("GUARDADO","La info fue guardada exitosamente")
			self.golden.destroy()
			logging.warning("Se registró el material con el Numero de Parte "+self.np.get())
		else:
			messagebox.showerror("Falta rellenar","Por favor, escriba datos en los campos de: \n\n\t*Número de parte\n\t*Descripción y\n\t*Cantidad")
			self.golden.focus_set()
			logging.error("No se han rellenado los campos correctamente para el Material con PN: "+self.np.get())

	def btregistrar(self):
		#Mandar llamar la función Validar datos.
		self.valida_datos()
		#Obtencion de Datos para registrar validando los campos de Numero de empleado, Nombre y Compañía que deben estar rellenados
		if self.num_emp.get() != "" and self.nom_user.get() != "" and self.compania.get() != "":
			file = open('import/datos.csv','a', newline='')
			file.write("\n"+self.num_emp.get()+","+self.user_duluth.get().lower()+","+self.user_mfs.get().upper()+","+self.nom_user.get().upper()+","+self.day.get()+"/"+self.mes.get()+"/"+self.year.get()+","+self.user_rol.get()+","+self.compania.get()+","+self.turno.get())
			file.close()
			logging.info("El archivo de datos se cerró")
			messagebox.showinfo("GUARDADO","La info fue guardada exitosamente")
			self.registrar.destroy()
			logging.warning("Se registró el Usuario con el Numero de empleado "+self.num_emp.get())
		else:
			messagebox.showerror("Falta rellenar","Por favor, al menos introduzca datos en los campos de: \n\n\t*Número de Empleado\n\t*Nombre\n\t*Compañía")
			self.registrar.focus_set()
			logging.error("No se rellenó correctamente los datos de: "+self.num_emp.get())

	def buscar_golden(self):
		if self.num_part.get() == "":
			messagebox.showwarning("Buscar","Escribe el PN a buscar")
			logging.warning("No se escribio el PN en el campo")
		else:
		#Abrir el archivo para leer los datos
			with open('import/golden.csv') as File:
				reader = csv.reader(File, delimiter=',',quotechar=',',quoting=csv.QUOTE_MINIMAL)
				for elemento in reader:
					if self.num_part.get() == elemento[0]:
						messagebox.showinfo("Elemento encontrado","Tenemos "+elemento[2]+" "+elemento[1]+" con el PN: "+elemento[0]+" y "+elemento[4]+" dañados.")
						logging.info("Se buscó la información del PN "+self.num_part.get())
						self.num_part.set("")
						self.r.focus_set()
			
	def golden(self):
	#Inicialización de Variables
		self.np = StringVar()
		self.descripcion = StringVar()
		self.cantidad = StringVar()
		self.bads = StringVar()
	#Creacion de la ventana Registrar Material Golden
		self.golden = Toplevel()
		self.golden.geometry("600x350+50+100")
		self.golden.resizable(0,0)
		self.golden.title("Golden")
		self.golden.iconbitmap("../logo2.ico")
		self.iregis = PhotoImage(file="imagenes/golden.png")
		Label(self.golden, image=self.iregis).place(x=20, y=5)
	#Componentes de la Ventana
		self.eti_tit = ttk.Label(self.golden, text="MATERIAL GOLDEN", font=("calibri",18,"bold")).place(x=250, y=35)
		self.eti_msj = ttk.Label(self.golden, text="* Campos requeridos").place(x=290, y=75)
		self.eti_np = ttk.Label(self.golden, text="*Número de Parte", font=self.fuente).place(x=20, y=140)
		self.txt_np = ttk.Entry(self.golden, textvariable=self.np, width=16, font=self.fuente).place(x=40, y=165)
		self.eti_desc = ttk.Label(self.golden, text="*Descripción", font=self.fuente).place(x=215, y=140)
		self.txt_desc = ttk.Entry(self.golden, textvariable=self.descripcion, width=16, font=self.fuente).place(x=225, y=165)
		self.eti_cant = ttk.Label(self.golden, text="*Cantidad", font=self.fuente).place(x=400, y=140)
		self.txt_cant = ttk.Entry(self.golden, textvariable=self.cantidad, width=16, font=self.fuente).place(x=410, y=165)
		self.eti_fechain = ttk.Label(self.golden, text="Fecha de registro ", font=self.fuente).place(x=100, y=230)
		golden_d=IntVar()
		golden_m=StringVar()
		golden_y=IntVar()
		golden_d.set(datetime.now().strftime("%d"))
		golden_m.set(datetime.now().strftime("%m"))
		golden_y.set(datetime.now().strftime("%Y"))
		self.gday = Spinbox(self.golden, from_=1, to=31, width=3, textvariable=golden_d)
		self.gday.place(x=267, y=230)
		self.gday.config(font=("calibri",14))
		self.gmes = Spinbox(self.golden, from_=1, to=12, width=4, textvariable=golden_m)
		self.gmes.place(x=320, y=230)
		self.gmes.config(font=("calibri",14))
		self.gyear = Spinbox(self.golden, from_=2013, to=2025, width=5, textvariable=golden_y)
		self.gyear.place(x=385, y=230)
		self.gyear.config(font=("calibri",14))
		self.eti_bad = ttk.Label(self.golden, text="Cantidad de dañados:", font=self.fuente).place(x=20, y=300)
		self.txt_bad = ttk.Entry(self.golden, textvariable=self.bads, width=10, font=self.fuente).place(x=200, y=300)
		self.btreg = ttk.Button(self.golden, text="Registrar", padding=(5,5), command=self.btgolden).place(x=490, y=300)

	def editar(self):
	#Creacion de la ventana Editar User
		self.editar = Toplevel()
		self.editar.geometry("650x400+700+300")
		self.editar.resizable(0,0)
		self.editar.title("Editar")
		self.editar.iconbitmap("../logo2.ico")
		self.ibuscar = PhotoImage(file="imagenes/edit.png")
		Label(self.editar, image=self.ibuscar).place(x=30, y=35)
	#Inicialización de variables
		self.num = StringVar()
		self.nom = StringVar()
		self.usm = StringVar()
		self.usd = StringVar()
		self.fei = StringVar()
		self.tur = StringVar()
	#Componentes de la Ventana
		self.lbltit = ttk.Label(self.editar, text="EDITAR USUARIO", font=("calibri",18,"bold")).place(x=280, y=30)
		self.lblNum = ttk.Label(self.editar, text="Número de Empleado: ", font=self.fuente).place(x=180, y=80)
		self.txtNum = ttk.Entry(self.editar, textvariable=self.num, width=16, font=self.fuente).place(x=380, y=80)
		self.lblNom = ttk.Label(self.editar, text="Nombre: ", font=self.fuente).place(x=180, y=130)
		self.txtNom = ttk.Entry(self.editar, textvariable=self.nom, width=27, font=self.fuente).place(x=270, y=130)
		self.lblUsM = ttk.Label(self.editar, text="User de MFS: ", font=self.fuente).place(x=180, y=180)
		self.txtUsM = ttk.Entry(self.editar, textvariable=self.usm, width=21, font=self.fuente).place(x=330, y=180)
		self.lblUsD = ttk.Label(self.editar, text="User de Duluth: ", font=self.fuente).place(x=180, y=230)
		self.txtUsD = ttk.Entry(self.editar, textvariable=self.usd, width=21, font=self.fuente).place(x=330, y=230)
		self.lblFeI = ttk.Label(self.editar, text="Fecha de ingreso: ", font=self.fuente).place(x=180, y=280)
		self.txtFeI = ttk.Entry(self.editar, textvariable=self.fei, width=20, font=self.fuente).place(x=340, y=280)
		self.lblTur = ttk.Label(self.editar, text="Turno: ", font=self.fuente).place(x=180, y=330)
		self.txtTur = ttk.Entry(self.editar, textvariable=self.tur, width=27, font=self.fuente).place(x=270, y=330)

	def opbuscar(self):
	#Inicialización de Variables
		self.campo_buscar = StringVar()
		self.buscar_per = StringVar()
	#Creacion de la ventana Buscar un User
		self.buscar = Toplevel()
		self.buscar.geometry("900x460+400+100")
		#self.buscar.resizable(0,0)
		self.buscar.title("Buscar")
		self.buscar.iconbitmap("../logo2.ico")
		self.ibuscar = PhotoImage(file="imagenes/buscar.png")
		Label(self.buscar, image=self.ibuscar).place(x=30, y=35)
	#Componentes de la Ventana
		self.campo_buscar.set("User de Duluth")
		self.eti_tit = ttk.Label(self.buscar, text="BUSQUEDA DE USUARIO", font=("calibri",18,"bold")).place(x=380, y=50)
		self.eti_buscar = ttk.Label(self.buscar, text=" Buscar por: ", font=self.fuente).place(x=330, y=100)
		self.combo_buscar = ttk.Combobox(self.buscar, textvariable=self.campo_buscar, values=("User de Duluth","Nombre","Numero de Empleado","User de MFS"), font=self.fuente).place(x=430, y=100)
		self.txt_buscar = ttk.Entry(self.buscar, textvariable=self.buscar_per, font=("calibri",14), width=14).place(x=430, y=131)
		self.bt_buscar = ttk.Button(self.buscar, text="Buscar", command=self.btbuscar).place(x=580, y=136)
		#self.bt_editar = ttk.Button(self.buscar, text="Editar", state=DISABLED).place(x=800, y=430)
		#Creación del Estilo para el Treeview(Vista árbol)
		self.styletree = ttk.Style()
		self.styletree.configure("mystyle.Treeview", highlighthickness=0, bd=0, font=("calibri",13))
		self.styletree.configure("mystyle.Treeview.Heading", font=("calibri",14,"bold"))
		#Creación del Treeview(Vista árbol)
		self.treeview = ttk.Treeview(self.buscar, columns=("1","2","3","4","5","6"), style="mystyle.Treeview")
		self.treeview.place(x=20, y=200)
		self.treeview.heading("#0", text="Duluth user")
		self.treeview.heading("1", text="Número ID")
		self.treeview.heading("2", text="MFS user")
		self.treeview.heading("3", text="Nombre")
		self.treeview.heading("4", text="Rol")
		self.treeview.heading("5", text="Compañía")
		self.treeview.heading("6", text="Turno")
		self.treeview.column("#0", width=100, minwidth=100, stretch=tk.NO)
		self.treeview.column("1", width=100, minwidth=100, stretch=tk.NO)
		self.treeview.column("2", width=100, minwidth=100, stretch=tk.NO)
		self.treeview.column("3", width=300, minwidth=300)
		self.treeview.column("4", width=90, minwidth=90, stretch=tk.NO)
		self.treeview.column("5", width=90, minwidth=90, stretch=tk.NO)
		self.treeview.column("6", width=70, minwidth=70, stretch=tk.NO)
		#Creación de etiqueta Seleccionado
		self.treeview.tag_bind("mytag", "<<TreeviewSelect>>",self.item_selected)

	def item_selected(self, event):
		self.bt_editar = ttk.Button(self.buscar, text="Editar", command=self.ejemplo).place(x=800, y=430)
		print("Se seleccionó un usuario ")

	def ejemplo(self):
		self.editar()
		resultado = []
		with open('import/admin.csv') as File:
			reader = csv.DictReader(File)
			for row in reader:
				resultado.append(row)
			print(resultado)

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
	#Creacion de la ventana Registrar User
		self.registrar = Toplevel()
		self.registrar.geometry("600x350+50+100")
		self.registrar.resizable(0,0)
		self.registrar.title("Registrar")
		self.registrar.iconbitmap("../logo2.ico")
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
		self.rolcb = ttk.Combobox(self.registrar, textvariable=self.user_rol, values=("TA","TT","ESP","TA Lead","TA Trainer"), font=("calibri",14), width=15).place(x=60, y=310)
		self.eti_turno = ttk.Label(self.registrar, text="Turno", font=self.fuente).place(x=250, y=310)
		self.rbturn1 = ttk.Radiobutton(self.registrar, text="1", variable=self.turno, value="1").place(x=300, y=315)
		self.rbturn2 = ttk.Radiobutton(self.registrar, text="2", variable=self.turno, value="2").place(x=330, y=315)
		self.rbturn3 = ttk.Radiobutton(self.registrar, text="3", variable=self.turno, value="3").place(x=360, y=315)
		self.btregis = ttk.Button(self.registrar, text="Registrar", padding=(5,5), command=self.btregistrar).place(x=490, y=300)

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
		m = self.user_mfs.get()
		data = pd.read_csv('import/datos.csv', encoding="ISO-8859–1")
		df = pd.DataFrame(data)
		res = df[df['USER_DUL'].str.contains(d, case=False)]
		print(res['USER_DUL'])
		if len(d) > 8 or len(m) > 8:
			messagebox.showerror("Verificar","Favor de checar que los usuarios de Duluth y MFS sean MÁXIMO de 8 caracteres.")
			logging.error("Uno de los campos User de Duluth o MFS no son de la longitud correcta")
			self.num_emp.set("")
		elif any(res['USER_DUL'] == d):
				messagebox.showerror("EXISTE","El usuario "+d.upper()+" ya existe\nFavor de utilizar otro")
				self.num_emp.set("")
				logging.error("El User de Duluth "+d.upper()+" ya está registrado")

	#def valida_material(self):
	#Validando el Material Golden los campos Numero de Parte y Descripcion


def main():
	inicio = Aplicacion()
	return(0)

if __name__ == '__main__':
	main()