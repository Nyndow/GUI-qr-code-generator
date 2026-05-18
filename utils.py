import segno
from datetime import datetime
from config import OUTPUT_FOLDER, PNG_SCALES
import re


def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def detect_url(text: str) -> str:
    text = text.strip()

    if re.match(r'^[a-zA-Z][a-zA-Z0-9+\-.]*://', text):
        return text

    if text.startswith("//"):
        return "https:" + text

    if ' ' not in text and re.match(
        r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?::\d+)?(?:[/?#]\S*)?$',
        text, re.IGNORECASE
    ):
        return "https://" + text

    return text


def generate_qr(data, res_choice, fmt_choice): ##

    data = detect_url(data)

    files = []

    qr = segno.make(data)

    scale = PNG_SCALES.get(res_choice, 16)

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