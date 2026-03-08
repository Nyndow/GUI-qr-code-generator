from pathlib import Path

APP_TITLE = "QR Code Generator"

OUTPUT_FOLDER = Path("QR_Codes")
OUTPUT_FOLDER.mkdir(exist_ok=True)

DEFAULT_SCALE = 16