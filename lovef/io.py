import sys

def readFromClipboard():
    import tkinter
    return tkinter.Tk().clipboard_get()

def readFromStdin():
    return "".join(sys.stdin.readlines())
