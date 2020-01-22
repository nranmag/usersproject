import csv, operator
import pandas as pd

def statusActivos():
	archivo = open('import/datos.csv')
	data = csv.reader(archivo)
	#col = ["NUM_EMP","USER_DUL","USER_MFS","NOMBRE","FECHA_IN","ROL","COMPANIA","TURNO","STATUS"]
	df = pd.DataFrame(data)
	archivo.close()
	activos = df[df[8] == "1"]
	c = "Tenemos "+str(activos[8].count())+" users en Status Activo"
	return activos, c

def statusInactivos():
	archivo = open('import/datos.csv')
	data = csv.reader(archivo)
	df = pd.DataFrame(data)
	archivo.close()
	inactivos = df[df[8] == "0"]
	c = "Tenemos "+str(inactivos[8].count())+" users Inactivos"
	return inactivos, c

def statusTurno1():
	archivo = open('import/datos.csv')
	data = csv.reader(archivo)
	df = pd.DataFrame(data)
	archivo.close()
	turno1 = df[(df[7] == "1") & (df[8] == "1")]
	c = "Tenemos "+str(turno1[7].count())+" en el turno 1."
	return turno1, c

def statusTurno2():
	archivo = open('import/datos.csv')
	data = csv.reader(archivo)
	df = pd.DataFrame(data)
	archivo.close()
	turno2 = df[(df[7] == "2") & (df[8] == "1")]
	c = "Tenemos "+str(turno2[7].count())+" en el turno 2."
	return turno2, c

def statusTurno3():
	archivo = open('import/datos.csv')
	data = csv.reader(archivo)
	df = pd.DataFrame(data)
	archivo.close()
	turno3 = df[(df[7] == "3") & (df[8] == "1")]
	c = "Tenemos "+str(turno3[7].count())+" en el turno 3."
	return turno3, c