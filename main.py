from gui import *


def main():
    window = Tk()
    window.geometry('400x460')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
