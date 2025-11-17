import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class BookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Viewer — Tkinter (Chapter 2)")
        self.root.geometry("400x550")
        self.root.configure(bg="white")

        # метка для изображения
        self.cover_label = tk.Label(root, bg="white")
        self.cover_label.pack(pady=15)

        # название книги
        self.title_label = tk.Label(
            root,
            text="Студаент МАИ",
            font=("Arial", 16, "bold"),
            bg="white"
        )
        self.title_label.pack(pady=5)

        # автор
        self.author_label = tk.Label(
            root,
            text="Шиневский Савелий Андреевич",
            font=("Arial", 12),
            bg="white"
        )
        self.author_label.pack(pady=5)

        # кнопка
        self.upload_button = tk.Button(
            root,
            text="Загрузить фотографию обложки",
            command=self.upload_photo
        )
        self.upload_button.pack(pady=10)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Изображения", "*.jpg *.jpeg *.png *.gif")]
        )
        if file_path:
            # открываем и масштабируем
            image = Image.open(file_path)
            image.thumbnail((250, 300))  # ограничиваем размер, но сохраняем пропорции

            photo = ImageTk.PhotoImage(image)
            self.cover_label.config(image=photo)
            self.cover_label.image = photo  # сохраняем ссылку, чтобы не удалилось


root = tk.Tk()
app = BookApp(root)
root.mainloop()

