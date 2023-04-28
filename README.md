# Printer Test

This program allows you to test printing with a selected printer on Windows operating system. You can print both text and image files with this program. 

## Requirements

This program requires the following libraries to run:
- tkinter
- ttk
- PIL
- win32ui
- win32print

## Installation

You can install the required libraries using pip with the following command:

csharp
Copy code
# README.md

## Printer Test

This program allows you to test printing with a selected printer on Windows operating system. You can print both text and image files with this program. 

## Requirements

This program requires the following libraries to run:
- tkinter
- ttk
- PIL
- win32ui
- win32print

## Installation

You can install the required libraries using pip with the following command:

```pip install tkinter ttk Pillow pywin32```


## Usage

To use this program, simply run the `printer_test.py` file. A window will appear with a combobox that lists all the local printers available on your system. Select the printer you want to test from the combobox and click the "Print Example" button to print the example text and image files.

If you want to print your own text or image files, you can modify the `example.txt` file provided with the program. Replace `<image>` and `</image>` tags with the file path of the image you want to print. 

Note that the image file should be in RGB format and should be rotated to fit the physical dimensions of the printer.

## Credits

This program is created by using the following libraries:
- tkinter: for creating the GUI
- ttk: for creating the combobox
- PIL: for opening and manipulating image files
- win32ui: for creating a device context for the printer
- win32print: for printing text and images.
