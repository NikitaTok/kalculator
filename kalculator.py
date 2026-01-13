import tkinter as tk
from tkinter import font
import math

current_input = ""
total_expression = ""
memory = 0

def on_button_click(button_text):
    global current_input, total_expression
    
    if button_text == "=":
        calculate()
    elif button_text == "C":
        clear_all()
    elif button_text == "CE":
        clear_entry()
    elif button_text == "Backspace":
        backspace()
    elif button_text == "%":
        percentage()
    elif button_text == "±":
        change_sign()
    elif button_text == "x²":
        square()
    elif button_text == "√":
        square_root()
    elif button_text == "sin":
        trigonometric_function("sin")
    elif button_text == "cos":
        trigonometric_function("cos")
    elif button_text == "tan":
        trigonometric_function("tan")
    elif button_text == "log":
        logarithm()
    elif button_text == "ln":
        natural_log()
    elif button_text == "π":
        add_pi()
    elif button_text == "e":
        add_e()
    elif button_text == "x!":
        factorial()
    elif button_text == "M+":
        memory_add()
    elif button_text == "MR":
        memory_recall()
    elif button_text == "MC":
        memory_clear()
    else:
        append_to_input(button_text)

def append_to_input(value):
    global current_input
    
    if value in '+-*/' and current_input and current_input[-1] in '+-*/':
        current_input = current_input[:-1] + value
    else:
        current_input += str(value)
    
    update_display()

def clear_all():
    global current_input, total_expression
    current_input = ""
    total_expression = ""
    update_display()

def clear_entry():
    global current_input
    current_input = ""
    update_display()

def backspace():
    global current_input
    if current_input:
        current_input = current_input[:-1]
        update_display()

def percentage():
    global current_input
    try:
        if current_input:
            value = float(eval(current_input)) / 100
            current_input = str(value)
            update_display()
    except:
        current_input = "Ошибка"
        update_display()

def change_sign():
    global current_input
    try:
        if current_input:
            if current_input[0] == '-':
                current_input = current_input[1:]
            else:
                current_input = '-' + current_input
            update_display()
    except:
        current_input = "Ошибка"
        update_display()

def square():
    global current_input
    try:
        if current_input:
            value = float(eval(current_input)) ** 2
            current_input = str(value)
            update_display()
    except:
        current_input = "Ошибка"
        update_display()

def square_root():
    global current_input
    try:
        if current_input:
            value = float(eval(current_input))
            if value < 0:
                current_input = "Ошибка: корень из отрицательного"
            else:
                value = math.sqrt(value)
                current_input = str(value)
            update_display()
    except:
        current_input = "Ошибка"
        update_display()

def trigonometric_function(func_name):
    global current_input
    try:
        if current_input:
            value = float(eval(current_input))
            radians = math.radians(value)
            
            if func_name == "sin":
                result = math.sin(radians)
            elif func_name == "cos":
                result = math.cos(radians)
            elif func_name == "tan":
                result = math.tan(radians)
            
            current_input = str(round(result, 10))
            update_display()
    except:
        current_input = "Ошибка"
        update_display()

def logarithm():
    global current_input
    try:
        if current_input:
            value = float(eval(current_input))
            if value <= 0:
                current_input = "Ошибка: логарифм ≤ 0"
            else:
                result = math.log10(value)
                current_input = str(round(result, 10))
            update_display()
    except:
        current_input = "Ошибка"
        update_display()

def natural_log():
    global current_input
    try:
        if current_input:
            value = float(eval(current_input))
            if value <= 0:
                current_input = "Ошибка: ln ≤ 0"
            else:
                result = math.log(value)
                current_input = str(round(result, 10))
            update_display()
    except:
        current_input = "Ошибка"
        update_display()

def add_pi():
    global current_input
    current_input += str(math.pi)
    update_display()

def add_e():
    global current_input
    current_input += str(math.e)
    update_display()

def factorial():
    global current_input
    try:
        if current_input:
            value = int(float(eval(current_input)))
            if value < 0:
                current_input = "Ошибка: факториал < 0"
            elif value > 50:
                current_input = "Слишком большое число"
            else:
                result = math.factorial(value)
                current_input = str(result)
            update_display()
    except:
        current_input = "Ошибка"
        update_display()

def memory_add():
    global memory, current_input
    try:
        if current_input:
            value = float(eval(current_input))
            memory += value
            memory_label.config(text=f"M: {memory}")
    except:
        pass

def memory_recall():
    global current_input, memory
    current_input += str(memory)
    update_display()

def memory_clear():
    global memory
    memory = 0
    memory_label.config(text="M: 0")

def calculate():
    global current_input, total_expression
    
    try:
        total_expression = current_input
        
        result = eval(current_input)
        
        if isinstance(result, float):
            if result.is_integer():
                result = int(result)
            else:
                result = round(result, 10)
        
        current_input = str(result)
        
    except ZeroDivisionError:
        current_input = "Ошибка: деление на 0"
    except:
        current_input = "Ошибка"
    
    update_display()

def update_display():
    if total_expression and not total_expression.startswith("Ошибка"):
        total_label.config(text=total_expression)
    else:
        total_label.config(text="")
    
    input_label.config(text=current_input or "0")

def get_button_color(text):
    if text in ['C', 'CE']:
        return "#ff6b6b"  # Красный
    elif text in ['=', '+', '-', '*', '/', '(', ')']:
        return "#4ecdc4"  # Бирюзовый
    elif text in ['Backspace', '%', '±', 'x²', '√', 'x!']:
        return "#45b7d1"  # Голубой
    elif text in ['sin', 'cos', 'tan', 'log', 'ln', 'π', 'e']:
        return "#96ceb4"  # Зеленый
    elif text in ['M+', 'MR', 'MC']:
        return "#ffcc5c"  # Желтый
    else:
        return "#f7f7f7"  # Светло-серый

def create_button(frame, text, row, col):
    button = tk.Button(
        frame,
        text=text,
        font=button_font,
        bg=get_button_color(text),
        fg="white" if text in ['C', 'CE', 'Backspace', '=', '%', '/', '*', '-', '+', '(', ')', 
                               '±', 'x²', '√', 'sin', 'cos', 'tan', 'log', 'ln',
                               'π', 'e', 'x!', 'M+', 'MR', 'MC'] else "black",
        height=2,
        width=6,
        command=lambda t=text: on_button_click(t)
    )
    button.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
    return button

root = tk.Tk()
root.title("Калькулятор")
root.geometry("500x600")
root.resizable(False, False)

display_font = font.Font(size=24)
button_font = font.Font(size=12)

display_frame = tk.Frame(root, height=100)
display_frame.pack(fill="both", padx=10, pady=(10, 5))

memory_label = tk.Label(
    display_frame,
    text="M: 0",
    font=("Arial", 10),
    fg="gray",
    anchor="w"
)
memory_label.pack(fill="x")

total_label = tk.Label(
    display_frame, 
    text="", 
    anchor="e", 
    font=display_font,
    fg="gray",
    height=1
)
total_label.pack(fill="both")

input_label = tk.Label(
    display_frame, 
    text="0", 
    anchor="e", 
    font=display_font,
    height=2
)
input_label.pack(fill="both")

buttons_frame = tk.Frame(root)
buttons_frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))

basic_buttons = [
    ('C', 0, 0), ('CE', 0, 1), ('Backspace', 0, 2),('M+', 0, 3), ('MR', 0, 4), ('MC', 0, 5),
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4), ('cos', 1, 5),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('tan', 2, 4), ('log', 2, 5),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('ln', 3, 4), ('π', 3, 5),
    ('0', 4, 0), ('.', 4, 1), ('±', 4, 2), ('+', 4, 3), ('=', 4, 4), ('e', 4, 5),
    ('%', 5, 0), ('x²', 5, 1), ('√', 5, 2), ('x!', 5, 3), ('(', 5, 4), (')', 5, 5),
]

for button_data in basic_buttons:
    text, row, col = button_data
    create_button(buttons_frame, text, row, col)

for i in range(6):
    buttons_frame.grid_rowconfigure(i, weight=1)

for i in range(6):
    buttons_frame.grid_columnconfigure(i, weight=1)

def on_key_press(event):
    key = event.char
    
    if key.isdigit() or key in '+-*/.%()':
        on_button_click(key)
    elif key == '\r':  # Enter
        on_button_click('=')
    elif key == '\x08':  # Backspace
        on_button_click('Backspace')
    elif key == '\x1b':  # Escape
        clear_all()

root.bind('<Key>', on_key_press)

root.mainloop()