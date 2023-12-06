from tkinter import *
from tkinter import ttk

#colors
co0 = "#ffffff" #white
co1 = "#000000" #black
co2 = "#7DB1FA" #blue
co3 = "#FA7516" #orange
co4 = "#C3DEF7" #light_blue
co5 = "#E4E4F0" #gray

window = Tk()
window.title('BaseConverterGUI')
window.geometry('350x310')
window.configure(bg = co0)
window.resizable(width = False, height = False)

style = ttk.Style()
style.theme_use('clam')

ttk.Separator(window, orient = HORIZONTAL).grid(row = 0, columnspan = 1, ipadx = 190)

def converter():
    def number_to_decimal(number, base):
        decimal = int(number, base)
        binary = bin(decimal)
        octal = oct(decimal)
        hexadecimal = hex(decimal)
        
        l_binary['text'] = str(binary[2:])
        l_octal['text'] = str(octal[2:])
        l_decimal['text'] = str(decimal)
        l_hexadecimal['text'] = str(hexadecimal[2:]).upper()
        
    base = combo.get()
    number = e_value.get()
    
    if base == "BINARY":
        base = 2
    elif base == "OCATL":
        base = 8
    elif base == "DECIMAL":
        base = 10
    elif base == "HEXADECIMAL":
        base = 16
        
    number_to_decimal(number, base)
    

#frames
frame_up = Frame(window, width = 400, height = 60, bg = co0, pady = 0, padx = 10)
frame_up.grid(row = 1, column = 0)

frame_down = Frame(window, width = 400, height = 300, bg = co0, pady = 12, padx = 0)
frame_down.grid(row = 2, column = 0)

app_title = Label(frame_up, text = "Numeric Base Converter", anchor = "center", font = ("System 20"), bg = co2, fg = co1)
app_title.place(x = 0, y = 15)

bases = ['BINARY', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']

combo = ttk.Combobox(frame_down, width = 12, justify = "center", font = ('Ivy 12 bold'))
combo['values'] = (bases)
combo.place(x = 35, y = 10)

e_value = Entry(frame_down, width = 10, justify = "center", font = ("", 13), highlightthickness = 1, relief = SOLID)
e_value.place(x = 160, y = 10)

b_converter = Button(frame_down, command = converter, text = "CONVERT", height = 1, bg = co4, fg = co1, font = ('Ivy 8 bold'), relief = RAISED, overrelief = RIDGE)
b_converter.place(x = 255, y = 10)

l_binary = Label(frame_down, text = "BINARY", width = 12, height = 1, relief = "flat", anchor = 'nw', font = ('Verdana 13'), bg = co3, fg = co0)
l_binary.place(x = 35, y = 60)
l_binary = Label(frame_down, text = "", width = 12, height = 1, relief = "flat", anchor = 'nw', font = ('Verdana 13'), bg = co5, fg = co1)
l_binary.place(x = 170, y = 60)

l_octal = Label(frame_down, text = "OCTAL", width = 12, height = 1, relief = "flat", anchor = 'nw', font = ('Verdana 13'), bg = co3, fg = co0)
l_octal.place(x = 35, y = 100)
l_octal = Label(frame_down, text = "", width = 12, height = 1, relief = "flat", anchor = 'nw', font = ('Verdana 13'), bg = co5, fg = co1)
l_octal.place(x = 170, y = 100)

l_decimal = Label(frame_down, text = "DECIMAL", width = 12, height = 1, relief = "flat", anchor = 'nw', font = ('Verdana 13'), bg = co3, fg = co0)
l_decimal.place(x = 35, y = 140)
l_decimal = Label(frame_down, text = "", width = 12, height = 1, relief = "flat", anchor = 'nw', font = ('Verdana 13'), bg = co5, fg = co1)
l_decimal.place(x = 170, y = 140)

l_hexadecimal = Label(frame_down, text = "HEXADECIMAL", width = 12, height = 1, relief = "flat", anchor = 'nw', font = ('Verdana 13'), bg = co3, fg = co0)
l_hexadecimal.place(x = 35, y = 180)
l_hexadecimal = Label(frame_down, text = "", width = 12, height = 1, relief = "flat", anchor = 'nw', font = ('Verdana 13'), bg = co5, fg = co1)
l_hexadecimal.place(x = 170, y = 180)

window.mainloop()

