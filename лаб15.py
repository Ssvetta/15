
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor

# Функції для файлових операцій
def new_file():
    text_area.delete(1.0, END)

def open_file():
    file = askopenfile(mode="r", defaultextension=".txt")
    if file is not None:
        text_area.delete(1.0, END)
        content = file.read()
        text_area.insert(END, content)
        file.close()

def save_file():
    file = asksaveasfile(mode="w", defaultextension=".txt")
    if file is not None:
        data = text_area.get(1.0, END)
        file.write(data)
        file.close()

def exit_app():
    if askyesno("Закрити", "Закрити програму?"):
        root.destroy()

# Функції для формату
def change_text_color():
    color = askcolor(color=text_area["fg"])[1]
    if color:
        text_area.configure(fg=color)

def change_background_color():
    color = askcolor(color=text_area["bg"])[1]
    if color:
        text_area.config(bg=color)

# Функції для редагування
def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

# Функції для довідки
def show_about():
    showinfo("Про програму", "Блокнот .\nВерсія 1.0\nАвтор: Світлана")

def show_help():
    showinfo("Довідка", "Документація про діалогові вікна: \nhttps://docs.python.org/uk/3/library/dialog.html")

# 4. Створити головне вікно.
root = Tk()
root.title("Блокнот")

# 6. Створити текстову область, використовуючи віджет Text
text_area = Text(root, undo=True)
text_area.pack(expand=True, fill=BOTH)

# 5. Створити головне меню.
menu_bar = Menu(root)
root.config(menu=menu_bar)

# 8. Пункт меню Файл
file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Новий", command=new_file)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Вийти", command=exit_app)

# 9. Додайте пункт меню Редагувати
edit_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Редагувати", menu=edit_menu)
edit_menu.add_command(label="Вирізати", command=cut_text)
edit_menu.add_command(label="Копіювати", command=copy_text)
edit_menu.add_command(label="Вставити", command=paste_text)

# 10. Додайте пункт меню Формат
format_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Формат", menu=format_menu)
format_menu.add_command(label="Колір тексту", command=change_text_color)
format_menu.add_command(label="Колір фону", command=change_background_color)

# 12. Додайте пункт меню Довідка
help_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Довідка", menu=help_menu)
help_menu.add_command(label="Про програму", command=show_about)
help_menu.add_command(label="Довідка по діалогові вікна", command=show_help)

# 26. Створіть контекстне меню для віджета Text.
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Вирізати", command=cut_text)
context_menu.add_command(label="Копіювати", command=copy_text)
context_menu.add_command(label="Вставити", command=paste_text)
context_menu.add_separator()
context_menu.add_command(label="Колір тексту", command=change_text_color)
context_menu.add_command(label="Колір фону", command=change_background_color)
context_menu.add_command(label="Зберегти", command=save_file)

def show_context_menu(event):
    try:
        context_menu.tk_popup(event.x_root, event.y_root)
    finally:
        context_menu.grab_release()

text_area.bind("<Button-3>", show_context_menu)

root.mainloop()
