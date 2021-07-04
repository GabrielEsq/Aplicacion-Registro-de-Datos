from tkinter import * 
from tkinter import messagebox 
import sqlite3 

#--------------- Funciones----------------------

def conexionBBDD():
    miConexion = sqlite3.connect("usuarios")
    miCursor=miConexion.cursor()

    try: 

        miCursor.execute('''
    
            CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(20),
            DIRECCION VARCHAR(50), 
            COMENTARIOS VARCHAR(150))
      
        ''')
        messagebox.showinfo("BBDD", "Base de datos creada con éxito")

    except:
        messagebox.showwarning("Atención", "La BBDD ya existe")

def saliraplicacion():

    valor=messagebox.askquestion("Salir", "Deseas salir de la aplicación")

    if valor=="yes":
        root.destroy()


def limpiarCampos():

    miNombre.set("")
    miId.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    textoComentario.delete(1.0, END)

def crear():

    miConexion=sqlite3.connect("usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("Insert into DATOSUSUARIOS VALUES(NULL,'" + miNombre.get()+
    "','" + miPass.get() +
    "','" + miApellido.get() +
    "','" + miDireccion.get() + 
    "','" + textoComentario.get("1.0", END) + "')")

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro insertado con éxito")

def leer():

    miConexion=sqlite3.connect("usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("Select * from DATOSUSUARIOS WHERE id = " + miId.get())

    elUsuario = miCursor.fetchall()

    for usuarios in elUsuario:

        miId.set(usuarios[0])
        miNombre.set(usuarios[1])
        miPass.set(usuarios[2])
        miApellido.set(usuarios[3])
        miDireccion.set(usuarios[4])
        textoComentario.insert(1.0, usuarios[5])

    miConexion.commit()

##

def actualizar():

    miConexion=sqlite3.connect("usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO = '"+ miNombre.get()+
    "', PASSWORD='" + miPass.get()+
    "', Apellido='" + miApellido.get()+
    "', Direccion='" + miDireccion.get()+ 
    "', Comentarios='" + textoComentario.get("1.0", END)+ 
    "' WHERE ID=" + miId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado con éxito")


def eliminar():

    miConexion=sqlite3.connect("usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID ="+ miId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro borrado con éxito")


root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Connectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command= saliraplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

CRUDMenu = Menu(barraMenu, tearoff=0)
CRUDMenu.add_command(label="Crear", command=crear)
CRUDMenu.add_command(label="Leer", command=leer)
CRUDMenu.add_command(label="Actualizar", command=actualizar)
CRUDMenu.add_command(label="Borrar", command=eliminar)

AyudaMenu = Menu(barraMenu, tearoff=0)
AyudaMenu.add_command(label="Licencia")
AyudaMenu.add_command(label="Acerca")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=CRUDMenu)
barraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)

##------------------- Comienzo de campos-------------------------------

miFrame = Frame(root)
miFrame.pack()


miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()


cuadroID = Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass = Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)


textoComentario = Text(miFrame, width=15, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
ScrollVer = Scrollbar(miFrame, command=textoComentario.yview)
ScrollVer.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=ScrollVer.set)

##---------------- Aquí comienzan los label-----------------

idLabel = Label(miFrame, text="Id:")
idLabel.grid(row=0,column=0, sticky="e", padx=10, pady=10)

nombrelabel = Label(miFrame, text="Nombre:")
nombrelabel.grid(row=1,column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Password:")
passLabel.grid(row=2,column=0, sticky="e", padx=10, pady=10)

ApellidoLabel = Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=3,column=0, sticky="e", padx=10, pady=10)

DireccionLabel = Label(miFrame, text="Direccion:")
DireccionLabel.grid(row=4,column=0, sticky="e", padx=10, pady=10)

ComentariosLabel = Label(miFrame, text="Comentarios:")
ComentariosLabel.grid(row=5,column=0, sticky="e", padx=10, pady=10)

#----------------Los botonoes ----------
 
miFrame2 = Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonleer=Button(miFrame2, text="Leer", command=leer)
botonleer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Borrar", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


root.mainloop()