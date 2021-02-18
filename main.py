import password
import PySimpleGUI as sg


# simboli=input('da li zelite simbole: ')
# brojevi=input('da li zelite brojeve: ')
# duzina=int(input('unesite duzinu: '))




f = open('file.csv', 'w+')


# Add a touch of color
# All the stuff inside your window.
layout = [  
            [sg.Checkbox('da li zelite simbole: ')],
            [sg.Checkbox('da li zelite brojeve: ')],
            [sg.Text('unesite duzinu: '), sg.InputText()],

            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    f.write(f'{values[0]},{values[1]},{values[2]}')
    window[0].update('')
    window[1].update('')
    window[2].update('')


f.close()
window.close()




