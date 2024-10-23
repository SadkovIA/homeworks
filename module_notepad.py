import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Блокнот")
        self.root.geometry("600x400")

        self.text_area = tk.Text(self.root, wrap='word', undo=True)
        self.text_area.pack(expand=True, fill='both')

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Меню Файл
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Новый", command=self.new_file)
        self.file_menu.add_command(label="Открыть", command=self.open_file)
        self.file_menu.add_command(label="Сохранить", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=self.root.quit)

        # Меню Справка
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Справка", menu=self.help_menu)
        self.help_menu.add_command(label="О программе", command=self.show_about)
        self.help_menu.add_command(label="Создатель", command=self.show_creator)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Текстовые файлы", "*.txt"),
                                                           ("Все файлы", "*.*")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text_area.delete(1.0, tk.END)  # Очистить текущее содержимое
                self.text_area.insert(tk.END, file.read())  # Вставить содержимое файла

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Текстовые файлы", "*.txt"),
                                                              ("Все файлы", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.text_area.get(1.0, tk.END))  # Сохранить текущее содержимое
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

    def show_about(self):
        messagebox.showinfo("О программе", "Это простой блокнот на Python с использованием Tkinter.\n\n"
                                           "Версия: 1.0\n"
                                           "Эта программа предназначена для редактирования текстов.")

    def show_creator(self):
        messagebox.showinfo("Создатель", "Создатель: Багровый Фантомас\n"
                                         "Email: bendez2014@yandex.ru\n"
                                         "Дата создания: Октябрь 2024")

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()