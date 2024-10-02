import tkinter

ventana = tkinter.Tk()
ventana.title("Ventana ejercio")
ventana.geometry("1000x600+250+100")


frame1 = tkinter.Frame(ventana)
frame1.configure(bg="sky blue", bd=20)
frame1.place(x=10, y=10, width=480, height=280)

frame2 = tkinter.Frame(ventana)
frame2.configure(bg="snow", bd=20 )
frame2.place(x=510, y=10, width=480, height=280)

frame3 = tkinter.Frame(ventana)
frame3.configure(bg="sky blue", bd=20 )
frame3.place(x=10, y=310, width=480, height=280)

frame4 = tkinter.Frame(ventana)
frame4.configure(bg="sky blue", bd=20 )
frame4.place(x=510, y=310, width=480, height=280)

etiqueta = tkinter.Label(frame3, text="Preciona el botón")
etiqueta.configure(fg="black", bg="gold", font=("Arial", 16, "bold"))
etiqueta.place(x=10, y=30, width=400, height=20)

etiqueta = tkinter.Label(frame4, text="Etiqueta")
etiqueta.configure(fg="black", bg="gold", font=("Arial", 16, "bold"))
etiqueta.place(x=10, y=110, width=150, height=20)

boton1 = tkinter.Button(frame3, text="Botón", font=("arial", 16), bg="steel blue")
boton1.place(x=150, y=110, width=150, height=20)

boton2 = tkinter.Button(frame4, text="Botón",font=("arial", 16), bg="steel blue")
boton2.place(x=170, y=110, width=150, height=20)

ventana.configure(bg="peach puff")
ventana.mainloop()

