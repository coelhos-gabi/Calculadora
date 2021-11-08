from typing import Type
import PySimpleGUI as sg
import sys


class Calculadora:
    def __init__(self):
        layout = [
            [sg.Output(30, 5)],
            [sg.Button('7', size=(5, 0), key='7'), sg.Button('8', size=(5, 0), key='8'), sg.Button(
                '9', size=(5, 0), key='9'), sg.Button('+', size=(5, 0), key='+')],
            [sg.Button('4', size=(5, 0), key='4'), sg.Button('5', size=(5, 0), key='5'), sg.Button(
                '6', size=(5, 0), key='6'), sg.Button('-', size=(5, 0), key='-')],
            [sg.Button('1', size=(5, 0), key='1'), sg.Button('2', size=(5, 0), key='2'), sg.Button(
                '3', size=(5, 0), key='3'), sg.Button('x', size=(5, 0), key='x')],
            [sg.Button('0', size=(5, 0), key='0'), sg.Button('=', size=(5, 0), key='='),
             sg.Button('C', size=(5, 0), key='c'), sg.Button('/', size=(5, 0), key='/')]
        ]

        janela = sg.Window('Calculadora', resizable=True).layout(layout)
        self.button, self.values = janela.Read()

    def Iniciar(self):

        try:
            a = int(input(self.button))
            b = input(self.button)
            c = int(input(self.button))
            if b == '+':
                resultado = operadores.soma(a, b)
                return resultado
        except ValueError:
            sys.exit(1)
        except TypeError:
            sys.exit(1)


if __name__ == '__main__':
    tela = Calculadora()
    tela.Iniciar()
