import tkinter as tk

form = tk.Tk()
form.title("my Form")

myLabel = tk.Label(form, text = "this is a label", width = 55, height = 5 , bg = "red" , fg= "white", font = "ariel").pack()
myStuff = tk.Label(form, text = "this is my stuff brah", width = 55, height = 25 , bg = "white").pack()



form.mainloop()