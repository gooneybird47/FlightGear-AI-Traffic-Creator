import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
# from tkinter.filedialog import askopenfile
import webbrowser
# import os
import sys

tg = ['<?xml version="1.0"?>', '<trafficlist>', '</trafficlist>', '    <aircraft>', '    </aircraft>',
      '        <model>', '</model>', '        <livery>', '</livery>', '        <airline>', '</airline>',
      '        <home-port>', '</home-port>', '        <required-aircraft>', '</required-aircraft>',
      '        <actype>', '</actype>', '        <offset>', '</offset>', '        <radius>', '</radius>',
      '        <flighttype>', '</flighttype>', '        <performance-class>', '</performance-class>',
      '        <registration>', '</registration>', '        <heavy>', '</heavy>', '    <flight>', '    </flight>',
      '        <callsign>', '</callsign>', '        <fltrules>', '</fltrules>', '        <departure>',
      '        </departure>', '            <port>', '</port>', '            <time>', '</time>',
      '        <cruise-alt>', '</cruise-alt>', '        <arrival>', '        </arrival>', '        <repeat>',
      '</repeat>'

      ]

# Clear The Output File

open("traffic_test.xml", "w").close()

root = tk.Tk()
root.geometry('1000x768')
root.title('AI Traffic File Creator For FlightGear')

# Redirect Print To File

sys.stdout = open('traffic_test.xml', 'a')

# Button click Counters

count_comment, count_aircraft, count_outbound_flight, count_return_flight = 0, 0, 0, 0


# close window

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?\n All data will be lost!"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)


# Close output - Save And Exit

def close_output():
    sys.stdout.close()

    # ("traffic_test.xml").close

    # if sys.platform == 'linux2':
    #     subprocess.call(["xdg-open", 'traffic_test.xml'])
    # else:
    #     os.startfile('traffic_test.xml')

    with open("traffic_test.xml", 'r+') as finp:
        outp = finp.read()
        out_all = '<?xml version="1.0"?>\n' + '<trafficlist>\n' + outp + '</trafficlist>'

        # print(out_all)

    save_traffic = filedialog.asksaveasfile(mode='w', defaultextension='.xml')

    if save_traffic:
        traffic_out = out_all
        save_traffic.write(traffic_out)
        save_traffic.close()

    else:
        pass
        # print('No File Saved')

    root.destroy()


txt_label = tk.Label(root, text='If you have never created a traffic before or unsure how to please refer to the Wiki\n'
                                'you can get there by pressing the "Wiki Link" button below.\n\n'
                                'Fill in all the sections then first press the "Create Aircraft" button\n'
                                'followed by the "Create Flight" buttons, this will create one\n'
                                'outbound and return flight for one aircraft. More aircraft and flights can be added\n'
                                'to the file by altering the required details and pressing the aircraft/flight\n'
                                'buttons again for each set of data before saving the file.\n\n '
                                'Any back slashes in the "path to Aircraft" must be replaced by forward slashes.\n\n'
                                'This program is designed to create small test or local traffic files '
                                'and cannot be used to\n'
                                'edit them, that is best done in a dedicated xml editor \n\n'
                                'Be warned,If you exit the program without saving all data will be lost. \n\n',
                     font=('Arial', 10), bg='powder blue', anchor="w", padx=10, justify='left')
txt_label.grid(row=16, rowspan=9, column=0, columnspan=3)


# Define Comment
def add_comment():
    print('<!-- ' + comment.get() + ' -->')

    # Count Comment Button clicks

    global count_comment

    count_comment = count_comment + 1

    comment_created.configure(text=f'Comment Created = {count_comment}', font=('Arial', 10))


# Define Aircraft


def mod():
    # model = m1.get()
    # liv = m2.get()
    # airl = m3.get()
    # hport = m4.get()
    # reqair = m5.get()
    # actype = m6.get()
    # ofset = m7.get()
    # rad = m8.get()
    # fltype = m9.get()
    # perclas = m10.get()
    # regi = m11.get()
    # heavy = m12.get()

    print(tg[3])
    print(tg[5] + m1.get() + tg[6])
    print(tg[7] + m2.get() + tg[8])
    print(tg[9] + m3.get() + tg[10])
    print(tg[11] + m4.get() + tg[12])
    print(tg[13] + m5.get() + tg[14])
    print(tg[15] + m6.get() + tg[16])
    print(tg[17] + m7.get() + tg[18])
    print(tg[19] + m8.get() + tg[20])
    print(tg[21] + m9.get() + tg[22])
    print(tg[23] + m10.get() + tg[24])
    print(tg[25] + m11.get() + tg[26])
    print(tg[27] + m12.get() + tg[28])
    print(tg[4])

    # Count Aircraft Button clicks

    global count_aircraft

    count_aircraft = count_aircraft + 1

    aircraft_created.configure(text=f'Aircraft Created = {count_aircraft}', font=('Arial', 10))


# Define Flights

# Outbound Flight

def outbound_flt():
    # calsig = f1.get()
    # reqair = f2.get()
    # fltrrule = f3.get()
    # dep_port = f4.get()
    # dep_time = f5.get()
    # dep_c_alt = f6.get()
    # ar_port = f7.get()
    # ar_time = f8.get()
    # repeat = f9.get()

    print(tg[29])
    print(tg[31] + f1.get() + tg[32])
    print(tg[13] + f2.get() + tg[14])
    print(tg[33] + f3.get() + tg[34])
    print(tg[35])
    print(tg[37] + f4.get() + tg[38])
    print(tg[39] + f5.get() + tg[40])
    print(tg[36])
    print(tg[41] + f6.get() + tg[42])
    print(tg[43])
    print(tg[37] + f7.get() + tg[38])
    print(tg[39] + f8.get() + tg[40])
    print(tg[44])
    print(tg[45] + f9.get() + tg[46])
    print(tg[30])

    # Count Outbound Flight Button clicks

    global count_outbound_flight

    count_outbound_flight = count_outbound_flight + 1

    outbound_flights_created.configure(text=f'Outbound Flights Created = {count_outbound_flight}', font=('Arial', 10))


# Return Flight

def return_flt():
    # calsig_r = rf1.get()
    # reqair_r = rf2.get()
    # fltrrule_r = rf3.get()
    # dep_port_r = rf4.get()
    # dep_time_r = rf5.get()
    # dep_c_alt_r = rf6.get()
    # ar_port_r = rf7.get()
    # ar_time_r = rf8.get()
    # repeat_r = rf9.get()

    print(tg[29])
    print(tg[31] + rf1.get() + tg[32])
    print(tg[13] + rf2.get() + tg[14])
    print(tg[33] + rf3.get() + tg[34])
    print(tg[35])
    print(tg[37] + rf4.get() + tg[38])
    print(tg[39] + rf5.get() + tg[40])
    print(tg[36])
    print(tg[41] + rf6.get() + tg[42])
    print(tg[43])
    print(tg[37] + rf7.get() + tg[38])
    print(tg[39] + rf8.get() + tg[40])
    print(tg[44])
    print(tg[45] + rf9.get() + tg[46])
    print(tg[30])

    # Count Return Flight Button clicks

    global count_return_flight

    count_return_flight = count_return_flight + 1

    return_flights_created.configure(text=f'Return Flights Created = {count_return_flight}', font=('Arial', 10))


# text variables

# Required Aircraft Insert

rqf = tk.StringVar()

# Insert Departure port from Arrival For Return Flight

port = tk.StringVar()

# Add Comment

comment_label = tk.Label(root, text='Comment', font=('Arial', 12, 'bold'), width='20', fg='blue')
comment_label.grid(row=1, column=2)
comment = tk.Entry(root, font=('Arial', 10))
comment.grid(row=3, column=2, padx=5, pady=5)
comment_button = tk.Button(root, font=('Arial', 10), text='Add Comment', command=add_comment)
comment_button.grid(row=4, column=2)

# Set up Aircraft Selection

Aircraft_label = tk.Label(root, text='Aircraft Selection', font=('Arial', 12, 'bold'), width='20', fg='blue')
Aircraft_label.grid(row=1, column=1)

m1_label = tk.Label(root, text='Path To Aircraft File', font=('Arial', 10), width='20', anchor="e")
m1_label.grid(row=3, column=0)
m1 = tk.Entry(root, font=('Arial', 10))
m1.insert(0, "Aircraft/")
m1.grid(row=3, column=1, padx=5, pady=5)

m2_label = tk.Label(root, text='Airline Livery', font=('Arial', 10), width='20', anchor="e")
m2_label.grid(row=4, column=0)
m2 = tk.Entry(root, font=('Arial', 10))
m2.grid(row=4, column=1, padx=5, pady=5)

m3_label = tk.Label(root, text='Airline Code', font=('Arial', 10), width='20', anchor="e")
m3_label.grid(row=5, column=0)
m3 = tk.Entry(root, font=('Arial', 10))
m3.grid(row=5, column=1, padx=5, pady=5)

m4_label = tk.Label(root, text='Home Port', font=('Arial', 10), width='20', anchor="e")
m4_label.grid(row=6, column=0)
m4 = tk.Entry(root, font=('Arial', 10))
m4.grid(row=6, column=1, padx=5, pady=5)

m5_label = tk.Label(root, text='Required Aircraft', font=('Arial', 10), width='20', anchor="e")
m5_label.grid(row=7, column=0)
m5 = tk.Entry(root, textvariable=rqf, font=('Arial', 10))
m5.grid(row=7, column=1, padx=5, pady=5)

m6_label = tk.Label(root, text='Aircraft Type', font=('Arial', 10), width='20', anchor="e")
m6_label.grid(row=8, column=0)
m6 = tk.Entry(root, font=('Arial', 10))
m6.grid(row=8, column=1, padx=5, pady=5)

m7_label = tk.Label(root, text='Offset', font=('Arial', 10), width='20', anchor="e")
m7_label.grid(row=9, column=0)
m7 = tk.Entry(root, font=('Arial', 10))
m7.insert(0, "0")
m7.grid(row=9, column=1, padx=5, pady=5)

m8_label = tk.Label(root, text='Radius', font=('Arial', 10), width='20', anchor="e")
m8_label.grid(row=10, column=0)
m8 = tk.Entry(root, font=('Arial', 10))
m8.grid(row=10, column=1, padx=5, pady=5)

m9_label = tk.Label(root, text='Flight Type', font=('Arial', 10), width='20', anchor="e")
m9_label.grid(row=11, column=0)

m9 = ttk.Combobox(root, font=('Arial', 10), values=['ga', 'cargo', 'gate', 'mil-fighter', 'mil-cargo'])
m9.grid(row=11, column=1, padx=5, pady=5)
m9.current(0)

m10_label = tk.Label(root, text='Performance Class', font=('Arial', 10), width='20', anchor="e")
m10_label.grid(row=12, column=0)

m10 = ttk.Combobox(font=('Arial', 10),
                   values=['light_aircraft', 'turboprop_transport', 'jet_transport', 'heavy_jet', 'ww2_fighter',
                           'jet_fighter', 'tanker', 'ufo'])
m10.grid(row=12, column=1, padx=5, pady=10)
m10.current(0)

m11_label = tk.Label(root, text='Registration', font=('Arial', 10), width='20', anchor="e")
m11_label.grid(row=13, column=0)
m11 = tk.Entry(root, font=('Arial', 10))
m11.grid(row=13, column=1, padx=5, pady=5)

m12_label = tk.Label(root, text='Heavy Aircraft', font=('Arial', 10), width='20', anchor="e")
m12_label.grid(row=14, column=0)

m12 = ttk.Combobox(font=('Arial', 10), values=['false', 'true'])
m12.grid(row=14, column=1, padx=5, pady=5)
m12.current(0)

# Create Aircraft section button


but_e1 = tk.Button(root, font=('Arial', 10), text='1 - Create Aircraft', command=mod)
but_e1.grid(row=6, column=2)

# Set Up Outbound Flight

flight_label = tk.Label(root, text='Outbound Flight', font=('Arial', 12, 'bold'), width='20', fg='blue')
flight_label.grid(row=1, column=5)

f1_label = tk.Label(root, text='Call Sign', font=('Arial', 10), width='20', anchor="e")
f1_label.grid(row=3, column=4)
f1 = tk.Entry(root, font=('Arial', 10))
f1.grid(row=3, column=5, padx=5, pady=5)

f2_label = tk.Label(root, text='Required Aircraft', font=('Arial', 10), width='20', anchor="e")
f2_label.grid(row=4, column=4)
f2 = tk.Entry(root, textvariable=rqf, font=('Arial', 10))
f2.grid(row=4, column=5, padx=5, pady=5)

f3_label = tk.Label(root, text='Flight Rules', font=('Arial', 10), width='20', anchor="e")
f3_label.grid(row=5, column=4)
f3 = ttk.Combobox(root, font=('Arial', 10), values=['IFR', 'VFR'])
f3.grid(row=5, column=5, padx=5, pady=5)
f3.current(0)

f4_label = tk.Label(root, text='Departure Port', font=('Arial', 10), width='20', anchor="e")
f4_label.grid(row=6, column=4)
f4 = tk.Entry(root, font=('Arial', 10))
f4.grid(row=6, column=5, padx=5, pady=5)

f5_label = tk.Label(root, text='Departure Time', font=('Arial', 10), width='20', anchor="e")
f5_label.grid(row=7, column=4)
f5 = tk.Entry(root, font=('Arial', 10))
f5.grid(row=7, column=5, padx=5, pady=5)

f6_label = tk.Label(root, text='Cruise Altitude', font=('Arial', 10), width='20', anchor="e")
f6_label.grid(row=8, column=4)
f6 = tk.Entry(root, font=('Arial', 10))
f6.grid(row=8, column=5, padx=5, pady=5)

f7_label = tk.Label(root, text='Arrival Port', font=('Arial', 10), width='20', anchor="e")
f7_label.grid(row=9, column=4)
f7 = tk.Entry(root, textvariable=port, font=('Arial', 10))
f7.grid(row=9, column=5, padx=5, pady=5)

f8_label = tk.Label(root, text='Arrival Time', font=('Arial', 10), width='20', anchor="e")
f8_label.grid(row=10, column=4)
f8 = tk.Entry(root, font=('Arial', 10))
f8.grid(row=10, column=5, padx=5, pady=5)

f9_label = tk.Label(root, text='Repeat', font=('Arial', 10), width='20', anchor="e")
f9_label.grid(row=11, column=4)
f9 = tk.Entry(root, font=('Arial', 10))
f9.grid(row=11, column=5, padx=5, pady=5)

# Set Up Return Flight

returnflight_label = tk.Label(root, text='Return Flight', font=('Arial', 12, 'bold'), width='20', fg='blue')
returnflight_label.grid(row=12, column=5, columnspan=2, padx=5, pady=5)

rf1_label = tk.Label(root, text='Call Sign', font=('Arial', 10), width='20', anchor="e")
rf1_label.grid(row=13, column=4)
rf1 = tk.Entry(root, font=('Arial', 10))
rf1.grid(row=13, column=5, padx=5, pady=5)

rf2_label = tk.Label(root, text='Required Aircraft', font=('Arial', 10), width='20', anchor="e")
rf2_label.grid(row=14, column=4)
rf2 = tk.Entry(root, textvariable=rqf, font=('Arial', 10))
rf2.grid(row=14, column=5, padx=5, pady=5)

rf3_label = tk.Label(root, text='Flight Rules', font=('Arial', 10), width='20', anchor="e")
rf3_label.grid(row=15, column=4)
rf3 = ttk.Combobox(root, font=('Arial', 10), values=['IFR', 'VFR'])
rf3.grid(row=15, column=5, padx=5, pady=5)
rf3.current(0)

rf4_label = tk.Label(root, text='Departure Port', font=('Arial', 10), width='20', anchor="e")
rf4_label.grid(row=16, column=4)
rf4 = tk.Entry(root, textvariable=port, font=('Arial', 10))
rf4.grid(row=16, column=5, padx=5, pady=5)

rf5_label = tk.Label(root, text='Departure Time', font=('Arial', 10), width='20', anchor="e")
rf5_label.grid(row=17, column=4)
rf5 = tk.Entry(root, font=('Arial', 10))
rf5.grid(row=17, column=5, padx=5, pady=5)

rf6_label = tk.Label(root, text='Cruise Altitude', font=('Arial', 10), width='20', anchor="e")
rf6_label.grid(row=18, column=4)
rf6 = tk.Entry(root, font=('Arial', 10))
rf6.grid(row=18, column=5, padx=5, pady=5)

rf7_label = tk.Label(root, text='Arrival Port', font=('Arial', 10), width='20', anchor="e")
rf7_label.grid(row=19, column=4)
rf7 = tk.Entry(root, font=('Arial', 10))
rf7.grid(row=19, column=5, padx=5, pady=5)

rf8_label = tk.Label(root, text='Arrival Time', font=('Arial', 10), width='20', anchor="e")
rf8_label.grid(row=20, column=4)
rf8 = tk.Entry(root, font=('Arial', 10))
rf8.grid(row=20, column=5, padx=5, pady=5)

rf9_label = tk.Label(root, text='Repeat', font=('Arial', 10), width='20', anchor="e")
rf9_label.grid(row=21, column=4)
rf9 = tk.Entry(root, font=('Arial', 10))
rf9.grid(row=21, column=5, padx=5, pady=5)

# Create Flight Sections

but_e2 = tk.Button(root, font=('Arial', 10), text='2 - Create Outbound Flight', command=outbound_flt)
but_e2.grid(row=8, column=2)

but_e3 = tk.Button(root, font=('Arial', 10), text='3 - Create Return Flight', command=return_flt)
but_e3.grid(row=10, column=2)

# Number Of Comments, Aircraft and Flights created

comment_created = tk.Label(root, fg='red')
comment_created.grid(row=5, column=2)

aircraft_created = tk.Label(root, fg='red')
aircraft_created.grid(row=7, column=2)

outbound_flights_created = tk.Label(root, fg='red')
outbound_flights_created.grid(row=9, column=2)

return_flights_created = tk.Label(root, fg='red')
return_flights_created.grid(row=11, column=2)

# Wiki Link

new = 1

wiki_url = 'http://wiki.flightgear.org/AI_Traffic'


def openweb():
    webbrowser.open(wiki_url, new=new)


but_wiki = tk.Button(root, font=('Arial', 12, 'bold'), width='10', fg='green', text='Wiki Link', command=openweb)
but_wiki.grid(row=27, column=1)

# Close Button

but_close = tk.Button(root, text='Save And Exit', fg='blue', font="Helvetica 12 bold", command=close_output)
but_close.grid(row=14, column=2)

root.mainloop()
