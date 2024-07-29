import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        
        # Bloquear el redimensionamiento de la ventana
        self.master.resizable(False, False)
        
        # Crear la entrada de texto (display) para la calculadora
        self.display = tk.Entry(master, width=14, font=("Arial", 24), bd=10, insertwidth=2, bg="#e0f7fa", fg="black", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Variables de estado
        self.current = ''
        self.op = ''  # Código de operación
        self.total = 0.0
        self.chivato = False  # Indicador de si hay una operación en curso

        # Definir los botones de la calculadora
        buttons = [
            "7", "8", "9", "/", 
            "4", "5", "6", "*", 
            "1", "2", "3", "-", 
            "C", "0", ".", "+", 
            "="
        ]
        
        # Posición inicial para los botones
        row=1 
        col=0
        
        # Crear los botones
        for button in buttons:
            self.build_button(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Vincular eventos de teclado
        self.master.bind("<Key>", self.key_press)
    
    def key_press(self, evento):
        # Control de eventos de teclado.
        key = evento.char
        if key == "\r":
            self.calculate()
        elif key == "\x08":
            self.clear_display()
        elif key == "\x1b":
            self.master.quit()
        elif key in "0123456789./*-+":
            self.click(key)
    
    def clear_display(self):
        # Limpiar el display de la calculadora.
        self.display.delete(0, tk.END)
        self.current = ''
        self.op = ''
        self.total = 0.0
        self.chivato = False
    
    def calculate(self):
        # Realizar el cálculo basado en la operación actual.
        try:
            if self.current and self.op:
                if self.op == "/":
                    if float(self.current) == 0:
                        raise ZeroDivisionError
                    self.total /= float(self.current)
                elif self.op == "*":
                    self.total *= float(self.current)
                elif self.op == "+":
                    self.total += float(self.current)
                elif self.op == "-":
                    self.total -= float(self.current)
            
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, round(self.total, 3))
        
        except ZeroDivisionError:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
    
    def click(self, key):
        # Manejar el clic de un botón.
        if self.chivato:
            self.chivato = False
        
        self.display.insert(tk.END, key)
        
        if key in "0123456789.":
            self.current += key
        else:
            if self.current:
                if not self.op:
                    self.total = float(self.current)
                self.current = ''
                self.op = key
                self.chivato = True
        

    def build_button(self, button, row, col):
        # Crear un botón de la calculadora y colocarlo en la cuadrícula.
        if button == "C":
            b = tk.Button(self.master, text=button, width=4, height=1, command=self.clear_display, bg="#ffab99", font=("Arial", 18))
        elif button == "=":
            b = tk.Button(self.master, text=button, width=4, height=1, command=self.calculate, bg="#4caf50", font=("Arial", 18))
        else:
            b = tk.Button(self.master, text=button, width=4, height=1, command=lambda: self.click(button), bg="#e0f7fa", font=("Arial", 18))
        
        b.grid(row=row, column=col, padx=5, pady=5)


# Configurar la ventana principal de la aplicación
root = tk.Tk()
root.title("Calculadora")
gui = Calculadora(root)
root.mainloop()
