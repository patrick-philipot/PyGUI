import PySimpleGUI as sg

def sample_layout():
    return [[sg.Text('Text element'), sg.InputText('Input data here', size=(12,1))],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

layout =   [[sg.Text('My Theme Previewer', font='Default 18', background_color='black')]]

row = []
for count, theme in enumerate(sg.theme_list()):
    sg.theme(theme)
    print("count {} count % 10 {}".format(count, bool(count % 10)))
    if not count % 10:
        layout += [row]
        row = []
    row += [sg.Frame(theme, sample_layout())]
if row:
    layout += [row]
print(layout)
sg.Window('Window Title', layout).read()