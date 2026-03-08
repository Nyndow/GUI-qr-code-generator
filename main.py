import ttkbootstrap as tb
from ui import QRApp


def main():

    root = tb.Window(themename="pulse")

    QRApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()