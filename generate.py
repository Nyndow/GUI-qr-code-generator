import segno
from datetime import datetime
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from pathlib import Path

# Folder to save QR codes
OUTPUT_FOLDER = Path("QR_Codes")
OUTPUT_FOLDER.mkdir(exist_ok=True)

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def generate_qr():
    data = text_input.get("1.0", "end").strip()
    if not data:
        messagebox.showwarning("Input required", "Please enter a link or text.")
        return

    fmt_choice = fmt_var.get()
    png_res_choice = res_var.get()

    try:
        if fmt_choice in (1, 3):  # PNG or Both
            scales = {1: 8, 2: 16, 3: 25, 4: 35}
            scale = scales.get(png_res_choice, 16)
            filename = OUTPUT_FOLDER / f"qr_{timestamp()}.png"
            qr = segno.make(data)
            qr.save(filename, scale=scale, border=4)
            print(f"PNG saved as {filename}")

        if fmt_choice in (2, 3):  # SVG or Both
            filename = OUTPUT_FOLDER / f"qr_{timestamp()}.svg"
            qr = segno.make(data)
            qr.save(filename, scale=10, border=4)
            print(f"SVG saved as {filename}")

        messagebox.showinfo("Success", f"QR code(s) saved in folder:\n{OUTPUT_FOLDER.resolve()}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR code:\n{e}")

# --------------------- GUI ---------------------
root = tb.Window(themename="pulse")
root.title("Modern QR Code Generator")
root.geometry("650x400")
root.resizable(False, False)

# Input label
tb.Label(root, text="Enter link or text:", font=("Segoe UI", 12)).pack(pady=(15,5))

# Adaptive Text widget for multi-line input
text_input = tb.Text(root, width=70, height=4, font=("Segoe UI", 12), wrap="word")
text_input.pack(pady=(0,10))

# Format choice
fmt_var = tb.IntVar(value=1)
tb.Label(root, text="Choose format:", font=("Segoe UI", 12)).pack(pady=(10,5))
frame_fmt = tb.Frame(root)
frame_fmt.pack()
tb.Radiobutton(frame_fmt, text="PNG", variable=fmt_var, value=1, bootstyle=PRIMARY).pack(side=LEFT, padx=10)
tb.Radiobutton(frame_fmt, text="SVG", variable=fmt_var, value=2, bootstyle=INFO).pack(side=LEFT, padx=10)
tb.Radiobutton(frame_fmt, text="Both", variable=fmt_var, value=3, bootstyle=SUCCESS).pack(side=LEFT, padx=10)

# PNG resolution choice
res_var = tb.IntVar(value=2)
tb.Label(root, text="PNG resolution:", font=("Segoe UI", 12)).pack(pady=(10,5))
frame_res = tb.Frame(root)
frame_res.pack()
tb.Radiobutton(frame_res, text="500 px (small)", variable=res_var, value=1, bootstyle=SECONDARY).pack(side=LEFT, padx=5)
tb.Radiobutton(frame_res, text="1000 px (medium)", variable=res_var, value=2, bootstyle=SECONDARY).pack(side=LEFT, padx=5)
tb.Radiobutton(frame_res, text="2000 px (large)", variable=res_var, value=3, bootstyle=SECONDARY).pack(side=LEFT, padx=5)
tb.Radiobutton(frame_res, text="3000 px (extra large)", variable=res_var, value=4, bootstyle=SECONDARY).pack(side=LEFT, padx=5)

# Generate button
tb.Button(root, text="Generate QR Code", command=generate_qr, bootstyle=SUCCESS, width=25).pack(pady=20)

root.mainloop()

