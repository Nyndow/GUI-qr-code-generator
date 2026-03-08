import segno
from datetime import datetime
from config import OUTPUT_FOLDER


def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def detect_url(text: str):
    text = text.strip()

    if text.startswith(("http://", "https://")):
        return text

    if "." in text and " " not in text:
        return "https://" + text

    return text


def generate_qr(data, scale, fmt_choice):

    data = detect_url(data)

    files = []

    qr = segno.make(data)

    if fmt_choice in (1, 3):
        png_file = OUTPUT_FOLDER / f"qr_{timestamp()}.png"
        qr.save(png_file, scale=scale, border=4)
        files.append(png_file)

    if fmt_choice in (2, 3):
        svg_file = OUTPUT_FOLDER / f"qr_{timestamp()}.svg"
        qr.save(svg_file, scale=scale, border=4)
        files.append(svg_file)

    return files


def generate_preview(data):

    data = detect_url(data)

    qr = segno.make(data)

    preview_file = OUTPUT_FOLDER / "preview.png"

    qr.save(preview_file, scale=6)

    return preview_file