from tkinter import ttk

import PIL
import win32ui
from PIL import Image, ImageWin
import win32print
from tkinter import *

PHYSICAL_WIDTH = 200
PHYSICAL_HEIGHT = 200

root = Tk()
root.geometry("500x500")
root.title("Printer Test")

printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)

printer_combobox = ttk.Combobox(root, values=[printer[2] for printer in printers])
printer_combobox.pack()


def get_selected_printer():
    selected_printer = printer_combobox.get()
    print("Selected printer:", selected_printer)
    for printer in printers:
        if printer[2] == selected_printer:
            for i in range(0, 9):
                try:
                    if printer[i] is not None:
                        print(printer[i])
                except IndexError:
                    break
            with open("example.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    if line.__contains__("<image>"):
                        line = line.replace("<image>", "")
                        line = line.replace("</image>", "")
                        print_image(printer[2], line.strip("\n"))
                    else:
                        print_text(printer[2], f"{line}".encode(encoding="utf-8"))


def print_text(selected_printer, text):
    printer_handle = win32print.OpenPrinter(selected_printer)
    win32print.GetPrinter(printer_handle, 2)
    win32print.StartDocPrinter(printer_handle, 1, ("test of raw data", None, "RAW"))
    win32print.StartPagePrinter(printer_handle)
    win32print.WritePrinter(printer_handle, text)
    win32print.EndPagePrinter(printer_handle)
    win32print.EndDocPrinter(printer_handle)
    win32print.ClosePrinter(printer_handle)


def print_image(selected_printer, file_path):
    printer_dc = win32ui.CreateDC()
    printer_dc.CreatePrinterDC(selected_printer)
    printer_size = (PHYSICAL_WIDTH, PHYSICAL_HEIGHT)

    bmp = PIL.Image.open(file_path).convert("RGB")
    if bmp.size[0] < bmp.size[1]:
        bmp = bmp.rotate(90)

    printer_dc.StartDoc(file_path)
    printer_dc.StartPage()

    dib = ImageWin.Dib(bmp)
    dib.draw(printer_dc.GetHandleOutput(), (0, 0, printer_size[0], printer_size[1]))

    printer_dc.EndPage()
    printer_dc.EndDoc()
    printer_dc.DeleteDC()


printer_button = Button(root, text="Print Example", command=get_selected_printer)
printer_button.pack()
root.mainloop()
