import ttkbootstrap as tb
from ui import QRApp
from config import APP_TITLE


def main():

    root = tb.Window(themename="pulse")

    root.title(APP_TITLE)

    QRApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()