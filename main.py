import PySimpleGUI as sg
import solve

def init():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Simple Integral Calculator+')],
        [sg.Text('Enter equation'), sg.InputText()],
        [sg.Text('Enter lower bound'), sg.InputText()],
        [sg.Text('Enter upper bound'), sg.InputText()],
        [sg.Text('Enter number of rectangles'), sg.InputText()],
        [sg.Button('OK'), sg.Button('Cancel')],
        [sg.Text('Result: ', size=(10,10), key='RES')],
    ]
    return sg.Window('Integrator', layout)


if __name__ == '__main__':
    window = init()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        res = (solve.integrate(values[0], int(values[1]), int(values[2]), int(values[3])))
        window.Element('RES').update('Result: ' + str(res))
    window.close()