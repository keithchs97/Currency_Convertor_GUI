import apis
import PySimpleGUI as sg
import time
import os

if not os.path.exists("symbols.txt"):
    with open("symbols.txt", "w", encoding="utf-8") as file:
        for k, v in apis.symbols_result['symbols'].items():
            file.writelines(f"{k} ({v})"'\n')
        pass

sg.theme("DarkGrey6")

symbols = apis.read_file()
symbols_array = [i.replace('\n', '') for i in symbols]

clock = sg.Text('', key='Clock')
label1 = sg.Text("Convert from (currency): ")
combobox1 = sg.Combo(symbols_array, default_value=symbols_array[0], size=(30, 6),
                     enable_events=True, key='combo1')

label2 = sg.Text("Convert to (currency): ")
combobox2 = sg.Combo(symbols_array, default_value=symbols_array[1], size=(30, 6),
                     enable_events=True, key='combo2')

label3 = sg.Text("Enter amount to convert: ")
input_box = sg.InputText(key='amount')

button_convert = sg.Button("Convert")

result_display = sg.Multiline(size=(50, 6), key='results')

window = sg.Window("My Currency Convertor App",
                   layout=[[clock],
                           [label1], [combobox1],
                           [label2], [combobox2],
                           [label3], [input_box, button_convert],
                           [result_display]],
                   font=('Helvetica', 10)
                   )

while True:
    event, values = window.read(timeout=10)  # 'values' is a dictionary
    window["Clock"].update(value=time.strftime("%d-%b-%Y, %H:%M:%S %p"))

    match event:

        case 'Convert':
            base_currency = values['combo1'][:3].upper()
            target_currency = values['combo2'][:3].upper()
            base_amount = int(values['amount'])
            result = apis.currency_convertor(base_currency, target_currency, base_amount)
            window['results'].update(result)
            window['amount'].update(value='')

        case sg.WIN_CLOSED:

            break

window.close()
