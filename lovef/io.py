import fileinput

def readFromClipboard():
    import tkinter
    return tkinter.Tk().clipboard_get()

def readFromStdin():
    text = ""
    for line in fileinput.input():
        text = text + line
    return text
