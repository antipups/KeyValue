import tkinter as tk
from openpyxl import load_workbook


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.btn = tk.Button(self,
                             text="Пошук",
                             command=self.say_hi)

        self.entr1 = tk.Entry(self)
        self.entr2 = tk.Entry(self)

        self.label1 = tk.Label(self, text='Впишіть код')
        self.label2 = tk.Label(self, text='Назва коду')

        self.label1.grid(row=0, column=0)
        self.label2.grid(row=0, column=1)
        self.entr1.grid(row=1, column=0)
        self.entr2.grid(row=1, column=1)
        self.btn.grid(columnspan=2)

    def say_hi(self):
        wb = load_workbook('HTOP.xlsx', read_only=True)
        for string in wb.active:
            if string[0].value == self.entr1.get():
                self.entr2.insert(0, string[1].value)
                break


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
