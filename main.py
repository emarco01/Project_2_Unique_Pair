from gui import *


def main():
    """
    Function that creates and defines the GUI window.
    """
    window = Tk()
    window.title('Unique Groups')
    window.geometry('400x550')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
