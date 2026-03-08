import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk

from utils import generate_qr, generate_preview
from config import OUTPUT_FOLDER


class QRApp:

    def __init__(self, root):

        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("850x600")
        self.root.minsize(700, 500)

        self.dark_mode = False
        self.preview_job = None

        self.build_ui()

    def build_ui(self):

        main = tb.Frame(self.root, padding=20)
        main.pack(fill=BOTH, expand=True)

        title = tb.Label(
            main,
            text="QR Code Generator",
            font=("Segoe UI", 22, "bold")
        )
        title.pack(pady=10)

        # INPUT
        tb.Label(main, text="Enter text or URL").pack(anchor=W)

        self.text_input = tb.Text(main, height=3, font=("Segoe UI", 11))
        self.text_input.pack(fill=X, pady=5)

        # live preview when typing
        self.text_input.bind("<KeyRelease>", self.schedule_preview)

        # PREVIEW IMAGE
        self.preview_label = tb.Label(main)
        self.preview_label.pack(pady=15)

        # FORMAT
        tb.Label(main, text="Format").pack(anchor=W)

        self.fmt_var = tb.IntVar(value=1)

        fmt_frame = tb.Frame(main)
        fmt_frame.pack(anchor=W)

        tb.Radiobutton(fmt_frame, text="PNG", variable=self.fmt_var, value=1).pack(side=LEFT, padx=5)
        tb.Radiobutton(fmt_frame, text="SVG", variable=self.fmt_var, value=2).pack(side=LEFT, padx=5)
        tb.Radiobutton(fmt_frame, text="Both", variable=self.fmt_var, value=3).pack(side=LEFT, padx=5)

        # SIZE SLIDER
        tb.Label(main, text="QR Size").pack(anchor=W, pady=(15, 0))

        slider_frame = tb.Frame(main)
        slider_frame.pack(fill=X)

        # NUMBER DISPLAY FIRST
        self.size_label = tb.Label(slider_frame, text="16", width=4)
        self.size_label.pack(side=RIGHT)

        # SLIDER
        self.scale_slider = tb.Scale(
            slider_frame,
            from_=5,
            to=40,
            orient=HORIZONTAL,
            command=self.slider_changed
        )

        self.scale_slider.set(16)
        self.scale_slider.pack(side=LEFT, fill=X, expand=True)

        # NUMBER DISPLAY
        self.size_label = tb.Label(slider_frame, text="16", width=4)
        self.size_label.pack(side=RIGHT)

        # BUTTONS
        btn_frame = tb.Frame(main)
        btn_frame.pack(pady=20)

        tb.Button(
            btn_frame,
            text="Generate QR",
            bootstyle=SUCCESS,
            width=18,
            command=self.generate
        ).pack(side=LEFT, padx=10)

        tb.Button(
            btn_frame,
            text="Dark Mode",
            bootstyle=SECONDARY,
            command=self.toggle_dark
        ).pack(side=LEFT)

    # -------------------------

    def slider_changed(self, value):

        value = int(float(value))
        self.size_label.config(text=str(value))

        self.update_preview()

    # -------------------------

    def schedule_preview(self, event=None):

        if self.preview_job:
            self.root.after_cancel(self.preview_job)

        self.preview_job = self.root.after(300, self.update_preview)

    # -------------------------

    def toggle_dark(self):

        if self.dark_mode:
            self.root.style.theme_use("pulse")
        else:
            self.root.style.theme_use("darkly")

        self.dark_mode = not self.dark_mode

    # -------------------------

    def update_preview(self):

        data = self.text_input.get("1.0", "end").strip()

        if not data:
            self.preview_label.config(image="")
            return

        try:

            preview_file = generate_preview(data)

            img = Image.open(preview_file)

            size = int(self.scale_slider.get()) * 10
            img = img.resize((size, size))

            self.tk_img = ImageTk.PhotoImage(img)

            self.preview_label.configure(image=self.tk_img)

        except Exception as e:
            print(e)

    # -------------------------

    def generate(self):

        data = self.text_input.get("1.0", "end").strip()

        if not data:
            messagebox.showwarning("Input required", "Enter text or URL")
            return

        try:

            files = generate_qr(
                data,
                int(self.scale_slider.get()),
                self.fmt_var.get()
            )

            messagebox.showinfo(
                "Success",
                f"Saved in:\n{OUTPUT_FOLDER.resolve()}"
            )

        except Exception as e:

            messagebox.showerror("Error", str(e))