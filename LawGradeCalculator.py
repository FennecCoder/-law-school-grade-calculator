import PySimpleGUI as sg
import sys

# Set theme and font
sg.theme('LightBlue2')
sg.set_options(font=('Arial', 12))

def create_unit_rate_window():
    layout = [
        [sg.Text("Unit Rate Calculation", font=('Arial', 14, 'bold'))],
        [sg.Text("Module Name:"), sg.Input(key='-MODULE-', size=(20,1))],
        [sg.Text("Does this module have TD?", size=(20,1)), 
         sg.Radio("Yes", "TD_GROUP", key='-HAS_TD-', default=True), 
         sg.Radio("No", "TD_GROUP")],
        [sg.Text("Module Point:", size=(15,1)), sg.Input(key='-MOD_POINT-', size=(10,1))],
        [sg.Text("TD Point:", size=(15,1), visible=True, key='-TD_TEXT-'), 
         sg.Input(key='-TD_POINT-', size=(10,1), visible=True)],
        [sg.Button("Calculate", button_color=('white', 'green'), size=(10,1)),
         sg.Button("Back", button_color=('white', 'gray'), size=(10,1))],
        [sg.Text("", size=(30,2), key='-UNIT_RESULT-', font=('Arial', 12, 'bold'))]
    ]
    return sg.Window("Unit Rate Calculator", layout, finalize=True)

def create_semester1_window():
    layout = [
        [sg.Text("First Semester Calculation", font=('Arial', 14, 'bold'))],
        [sg.Text("Constitutional:", size=(20,1)), sg.Input(key='-DOS-', size=(10,1))],
        [sg.Text("TD Mark:", size=(20,1)), sg.Input(key='-TD_DOS-', size=(10,1))],
        [sg.Text("Sciences juridiques:", size=(20,1)), sg.Input(key='-JURI-', size=(10,1))],
        [sg.Text("TD Mark:", size=(20,1)), sg.Input(key='-TD_JURI-', size=(10,1))],
        [sg.Text("Administratif:", size=(20,1)), sg.Input(key='-ADMI-', size=(10,1))],
        [sg.Text("TD Mark:", size=(20,1)), sg.Input(key='-TD_IDAE-', size=(10,1))],
        [sg.Text("Méthodologie:", size=(20,1)), sg.Input(key='-MENH-', size=(10,1))],
        [sg.Text("Histoire juridiques:", size=(20,1)), sg.Input(key='-TARIKH-', size=(10,1))],
        [sg.Text("Communauté inter:", size=(20,1)), sg.Input(key='-MOJTAME-', size=(10,1))],
        [sg.Text("Terminologie:", size=(20,1)), sg.Input(key='-TERM-', size=(10,1))],
        [sg.Button("Calculate", button_color=('white', 'blue'), size=(10,1)),
         sg.Button("Back", button_color=('white', 'gray'), size=(10,1))],
        [sg.Text("", size=(30,2), key='-SEM1_RESULT-', font=('Arial', 12, 'bold'))]
    ]
    return sg.Window("First Semester Calculator", layout, finalize=True)

def create_semester2_window():
    layout = [
        [sg.Text("Second Semester Calculation", font=('Arial', 14, 'bold'))],
        [sg.Text("Constitutional:", size=(20,1)), sg.Input(key='-DOS2-', size=(10,1))],
        [sg.Text("TD Mark:", size=(20,1)), sg.Input(key='-TD_DOS2-', size=(10,1))],
        [sg.Text("Sciences juridiques:", size=(20,1)), sg.Input(key='-JURI2-', size=(10,1))],
        [sg.Text("TD Mark:", size=(20,1)), sg.Input(key='-TD_JURI2-', size=(10,1))],
        [sg.Text("Administratif:", size=(20,1)), sg.Input(key='-ADMI2-', size=(10,1))],
        [sg.Text("TD Mark:", size=(20,1)), sg.Input(key='-TD_IDAE2-', size=(10,1))],
        [sg.Text("Méthodologie:", size=(20,1)), sg.Input(key='-MENH2-', size=(10,1))],
        [sg.Text("Charia:", size=(20,1)), sg.Input(key='-CHARI-', size=(10,1))],
        [sg.Text("Political Economy:", size=(20,1)), sg.Input(key='-I9TISAD-', size=(10,1))],
        [sg.Text("Terminologie:", size=(20,1)), sg.Input(key='-TERM2-', size=(10,1))],
        [sg.Button("Calculate", button_color=('white', 'blue'), size=(10,1)),
         sg.Button("Back", button_color=('white', 'gray'), size=(10,1))],
        [sg.Text("", size=(30,2), key='-SEM2_RESULT-', font=('Arial', 12, 'bold'))]
    ]
    return sg.Window("Second Semester Calculator", layout, finalize=True)

def create_total_window():
    layout = [
        [sg.Text("Annual GPA Calculation", font=('Arial', 14, 'bold'))],
        [sg.Text("First Semester Average:", size=(20,1)), sg.Input(key='-SEM1-', size=(10,1))],
        [sg.Text("Second Semester Average:", size=(20,1)), sg.Input(key='-SEM2-', size=(10,1))],
        [sg.Button("Calculate", button_color=('white', 'green'), size=(10,1)),
         sg.Button("Back", button_color=('white', 'gray'), size=(10,1))],
        [sg.Text("", size=(30,2), key='-TOTAL_RESULT-', font=('Arial', 12, 'bold'))]
    ]
    return sg.Window("Annual GPA Calculator", layout, finalize=True)

def about_window():
    layout = [
        [sg.Text("Law School GPA Calculator", font=('Arial', 14, 'bold'))],
        [sg.Text("Version 1.0", font=('Arial', 12))],
        [sg.Text("Developed by Sami Remili", font=('Arial', 12))],
        [sg.Text("For First Year Law Students", font=('Arial', 12))],
        [sg.Text("University of Constantine 1", font=('Arial', 12))],
        [sg.Button("OK", button_color=('white', 'blue'), size=(10,1))]
    ]
    return sg.Window("About", layout, finalize=True)

def main_window():
    menu_layout = [
        [sg.Button("Unit Rate Calculation", size=(20,2), button_color=('white', 'darkorange'))],
        [sg.Button("First Semester GPA", size=(20,2), button_color=('white', 'royalblue'))],
        [sg.Button("Second Semester GPA", size=(20,2), button_color=('white', 'royalblue'))],
        [sg.Button("Annual GPA Calculation", size=(20,2), button_color=('white', 'darkgreen'))],
        [sg.Button("About", size=(20,2), button_color=('white', 'purple'))],
        [sg.Button("Exit", size=(20,2), button_color=('white', 'firebrick'))]
    ]
    
    layout = [
        [sg.Text("Faculty of Law and Political Science", font=('Arial', 16, 'bold'))],
        [sg.Text("University of Constantine 1", font=('Arial', 14))],
        [sg.Text("Grade Calculator", font=('Arial', 14, 'italic'))],
        [sg.VerticalSeparator()],
        [sg.Column(menu_layout, element_justification='center')],
        [sg.Text("", size=(30,1), key='-STATUS-', font=('Arial', 10))]
    ]
    
    return sg.Window("Law School GPA Calculator", layout, finalize=True)

def main():
    main_win = main_window()
    current_window = None
    
    while True:
        window, event, values = sg.read_all_windows()
        
        if event == sg.WIN_CLOSED or event == "Exit" or event == "OK":
            if window == main_win:
                break
            else:
                window.close()
                if window != about_window:  # Don't make main window visible for about window
                    main_win.un_hide()
        
        elif event == "Back":
            window.close()
            main_win.un_hide()
        
        elif event == "Unit Rate Calculation":
            main_win.hide()
            current_window = create_unit_rate_window()
        
        elif event == "First Semester GPA":
            main_win.hide()
            current_window = create_semester1_window()
        
        elif event == "Second Semester GPA":
            main_win.hide()
            current_window = create_semester2_window()
        
        elif event == "Annual GPA Calculation":
            main_win.hide()
            current_window = create_total_window()
        
        elif event == "About":
            main_win.hide()
            current_window = about_window()
        
        # Calculation logic
        elif event == "Calculate":
            if window == current_window and current_window.Title == "Unit Rate Calculator":
                try:
                    module = values['-MODULE-'].upper()
                    has_td = values['-HAS_TD-']
                    mod_point = float(values['-MOD_POINT-'])
                    
                    if has_td:
                        td_point = float(values['-TD_POINT-'])
                        average = (mod_point + td_point) / 2
                        window['-UNIT_RESULT-'].update(f"The average of {module} is: {average:.2f}")
                    else:
                        window['-UNIT_RESULT-'].update(f"The average of {module} is: {mod_point:.2f}")
                except ValueError:
                    window['-UNIT_RESULT-'].update("Please enter valid numbers!")
            
            elif window == current_window and current_window.Title == "First Semester Calculator":
                try:
                    coef = 9
                    dos = float(values['-DOS-'])
                    td_do = float(values['-TD_DOS-'])
                    juri = float(values['-JURI-'])
                    td_juri = float(values['-TD_JURI-'])
                    admi = float(values['-ADMI-'])
                    td_idae = float(values['-TD_IDAE-'])
                    menh = float(values['-MENH-'])
                    tarikh = float(values['-TARIKH-'])
                    mojtame = float(values['-MOJTAME-'])
                    term = float(values['-TERM-'])
                    
                    doss = (dos + td_do)/2 * 2
                    jurii = (juri + td_juri)/2 * 2
                    admii = (admi + td_idae)/2 * 1
                    
                    total = (doss + jurii + admii + menh + tarikh + mojtame + term) / coef
                    window['-SEM1_RESULT-'].update(f"First Semester Average: {total:.2f}")
                except ValueError:
                    window['-SEM1_RESULT-'].update("Please enter valid numbers!")
            
            elif window == current_window and current_window.Title == "Second Semester Calculator":
                try:
                    coef = 9
                    dos = float(values['-DOS2-'])
                    td_do = float(values['-TD_DOS2-'])
                    juri = float(values['-JURI2-'])
                    td_juri = float(values['-TD_JURI2-'])
                    admi = float(values['-ADMI2-'])
                    td_idae = float(values['-TD_IDAE2-'])
                    menh = float(values['-MENH2-'])
                    chari = float(values['-CHARI-'])
                    i9tisad = float(values['-I9TISAD-'])
                    term = float(values['-TERM2-'])
                    
                    doss = (dos + td_do)/2 * 2
                    jurii = (juri + td_juri)/2 * 2
                    admii = (admi + td_idae)/2 * 1
                    
                    total = (doss + jurii + admii + menh + chari + i9tisad + term) / coef
                    window['-SEM2_RESULT-'].update(f"Second Semester Average: {total:.2f}")
                except ValueError:
                    window['-SEM2_RESULT-'].update("Please enter valid numbers!")
            
            elif window == current_window and current_window.Title == "Annual GPA Calculator":
                try:
                    sem1 = float(values['-SEM1-'])
                    sem2 = float(values['-SEM2-'])
                    total = (sem1 + sem2) / 2
                    window['-TOTAL_RESULT-'].update(f"Annual GPA: {total:.2f}")
                except ValueError:
                    window['-TOTAL_RESULT-'].update("Please enter valid numbers!")
    
    main_win.close()

if __name__ == "__main__":
    main()
