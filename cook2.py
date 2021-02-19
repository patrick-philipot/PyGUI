import PySimpleGUI as sg
import sys

if len(sys.argv) == 1:
    layout = [[sg.Text('Document to open')],
             [sg.In(), sg.FileBrowse()],
             [sg.Open(), sg.Cancel()]]

    window = sg.Window('My Script', layout)
    event, values = window.read()
    window.close()

    fname = values[0]
    print(event, values)
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:
    sg.popup('The filename you chose was', fname)