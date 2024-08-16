import tkinter as tk

window =tk.Tk()
window.title('Miles to Km Converter')
window.minsize()
window.config(padx=10, pady=10)


input = tk.Entry()
input.grid(column=1, row=0)

miles = tk.Label(text='Miles')
miles.grid(column=2, row=0)

is_equal_to = tk.Label(text='is Equal to')
is_equal_to.grid(column=0, row=1)

result = tk.Label(text=0)
result.grid(column=1, row=1)

km = tk.Label(text='Km')
km.grid(column=2, row=1)

def calculate():
  miles = float(input.get())
  km = round(miles * 1.60934)
  result.config(text=km)

button = tk.Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)






window.mainloop()