from pathlib import Path

APP_TITLE = "QR Code Generator"

OUTPUT_FOLDER = Path("QR_Codes")
OUTPUT_FOLDER.mkdir(exist_ok=True)

PNG_SCALES = {
    1: 8,
    2: 16,
    3: 25,
    4: 35
}

PREVIEW_SIZES = {
    1: 120,
    2: 180,
    3: 240,
    4: 300
}