#Importing
import tkinter, decimal, math, string

root = tkinter.Tk()
root.title('calc')
root.resizable(0, 0)
root.geometry('320x350')
global vartext
global temp

result = notation = None
# Text input field
vartext = tkinter.StringVar()
# To store data temporarily
temp = []


class buttonEvent:
    def __init__(self, buttonEvent):
        self.buttonEvent = buttonEvent

    def write(self):
        temp.append(self.buttonEvent)
        vartext.set(''.join(temp))

    def tui(self):
        temp.pop()
        vartext.set(''.join(temp))

    def clear(self):
        temp.clear()
        vartext.set('')
        result = None
        notation = None

    def PN(self):
        if temp[0]:
            if temp[0] == '-':
                temp[0] = '+'
            elif temp[0] == '+':
                temp[0] = '-'
            else:
                temp.insert(0, '-')
            vartext.set(''.join(temp))

    def point(self):
        if temp.count('.') >= 1:
            pass
        else:
            if temp == []:
                temp.append('0')
            temp.append('.')
        vartext.set(''.join(temp))

    def deal(self):
        global result, notation, result
        if vartext.get() == '':
            pass
        else:
            get1 = decimal.Decimal(vartext.get())
        if self.buttonEvent in ('+', '-', '×', '÷', '='):
            if notation is not None:
                get1 = decimal.Decimal(result)
                get2 = decimal.Decimal(vartext.get())
                if notation == '+':
                    result = get1 + get2
                elif notation == '-':
                    result = get1 - get2
                elif notation == '×':
                    result = get1 * get2
                elif notation == '÷':
                    result = get1 / get2
            else:
                result = get1
            if self.buttonEvent == '=':
                notation = None
            else:
                notation = self.buttonEvent
        print(notation)
        print(result)
        vartext.set(str(result))
        temp.clear()


def layOut(root):
    global vartext
    entry1 = tkinter.Label(root, width=45, height=3, background='white', anchor='se', textvariable=vartext)
    entry1.grid(row=0, columnspan=5)
    # First row
    buttonCE = tkinter.Button(root, text='CE', width=10, height=2)
    buttonC = tkinter.Button(root, text='C', width=10, height=2, command=buttonEvent('C').clear)
    buttonDelete = tkinter.Button(root, text='DEL', width=10, height=2, command=buttonEvent('DEL').tui)
    buttonDivide = tkinter.Button(root, text='÷', width=10, height=2, command=buttonEvent('÷').deal)
    buttonCE.grid(row=1, column=0)
    buttonC.grid(row=1, column=1)
    buttonDelete.grid(row=1, column=2)
    buttonDivide.grid(row=1, column=3)
    # Seсond row
    button7 = tkinter.Button(root, text='7', width=10, height=2, command=buttonEvent('7').write)
    button8 = tkinter.Button(root, text='8', width=10, height=2, command=buttonEvent('8').write)
    button9 = tkinter.Button(root, text='9', width=10, height=2, command=buttonEvent('9').write)
    buttonMutiply = tkinter.Button(root, text='×', width=10, height=2, command=buttonEvent('×').deal)
    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)
    buttonMutiply.grid(row=2, column=3)
    # Third row
    button4 = tkinter.Button(root, text='4', width=10, height=2, command=buttonEvent('4').write)
    button5 = tkinter.Button(root, text='5', width=10, height=2, command=buttonEvent('5').write)
    button6 = tkinter.Button(root, text='6', width=10, height=2, command=buttonEvent('6').write)
    buttonSub = tkinter.Button(root, text='-', width=10, height=2, command=buttonEvent('-').deal)
    button4.grid(row=3, column=0)
    button5.grid(row=3, column=1)
    button6.grid(row=3, column=2)
    buttonSub.grid(row=3, column=3)
    # Fourth row
    button1 = tkinter.Button(root, text='1', width=10, height=2, command=buttonEvent('1').write)
    button2 = tkinter.Button(root, text='2', width=10, height=2, command=buttonEvent('2').write)
    button3 = tkinter.Button(root, text='3', width=10, height=2, command=buttonEvent('3').write)
    buttonPlus = tkinter.Button(root, text='+', width=10, height=2, command=buttonEvent('+').deal)
    button1.grid(row=4, column=0)
    button2.grid(row=4, column=1)
    button3.grid(row=4, column=2)
    buttonPlus.grid(row=4, column=3)
    # Fifth row
    button_ = tkinter.Button(root, text='+/-', width=10, height=2, command=buttonEvent('+/-').PN)
    button0 = tkinter.Button(root, text='0', width=10, height=2, command=buttonEvent('0').write)
    buttonPoint = tkinter.Button(root, text='.', width=10, height=2, command=buttonEvent('.').point)
    buttonEqual = tkinter.Button(root, text='=', width=10, height=2, command=buttonEvent('=').deal)
    button_.grid(row=5, column=0)
    button0.grid(row=5, column=1)
    buttonPoint.grid(row=5, column=2)
    buttonEqual.grid(row=5, column=3)

if __name__ == '__main__':
    layOut(root)
    root.mainloop()