# Modern QR Code Generator

![Python](https://img.shields.io/badge/Python-3.7%2B-blue) 
![License](https://img.shields.io/badge/License-MIT-green)

A **simple QR code generator with a modern GUI** built with Python and [ttkbootstrap](https://pypi.org/project/ttkbootstrap/).  
Generate **PNG, SVG, or both formats** for any link or text, with customizable resolution, adaptive input, and theme selector. All generated files are saved in a dedicated `QR_Codes` folder.

---

## Features

- Generate **QR codes** in **PNG**, **SVG**, or **both formats**.  
- **Select PNG resolution** (500px → 3000px).  
- **Adaptive text input** for long URLs or multi-line text.  
- **Theme selector** with 20+ modern themes (dark/light).  
- Auto **timestamped filenames** and organized in a `QR_Codes` folder.  
- Easy-to-use **GUI** – no command line needed.  

---

## Installation && Usage

1. Make sure you have **Python 3.7+** installed.  
2. Install required packages and run:

```bash
pip install segno ttkbootstrap

python generate.py
