import tkinter as tk


class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("300x300")
        self.master.resizable(False, False)
        self.master.eval('tk::PlaceWindow . center')
        self.pack()
        self.create_widgets()
        self.current_value = ""

    def create_widgets(self):
        # Create the display
        self.display = tk.Entry(self, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        # Create the buttons
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        for i, symbol in enumerate(buttons):
            button = tk.Button(self, text=symbol, width=5, height=2,
                               command=lambda symbol=symbol: self.button_click(symbol))
            row = i // 4 + 1
            col = i % 4
            button.grid(row=row, column=col, padx=5, pady=5)

        # Create the clear button
        clear_button = tk.Button(
            self, text="Clear", width=5, height=2, command=self.clear)
        clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def button_click(self, symbol):
        if symbol == "=":
            self.evaluate()
        else:
            self.current_value += symbol
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_value)

    def evaluate(self):
        try:
            result = eval(self.current_value)
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
            self.current_value = str(result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.current_value = ""

    def clear(self):
        self.display.delete(0, tk.END)
        self.current_value = ""


if __name__ == '__main__':
    root = tk.Tk()
    app = Calculator(master=root)
    app.mainloop()
