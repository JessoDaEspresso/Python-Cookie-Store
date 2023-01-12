# This is a simple gui program that allows you to purchase only one cookie
# at a time. It also allows you to add ice cream to your cookie.
# With some updates, the program could be setup for the user to purchase multiple cookies.
# This program was only written to support the updating of one cookie as the main focus was to
# learn who classes and guis operate in python
# the program will also generate an invoice to a CSV file.

# Written by Jesse Pirrotta
# Date 2023-01-12
# Version 0.5 (one cookie)
# Updates (future): add support for multiple cookies

import PySimpleGUI as sg

import cookie_store_back_end

# Creating Cookie

newCookie = cookie_store_back_end.Cookie()

total = sg.Text("Your total is: $0.00")
yes_btn = sg.Button("Yes")
no_btn = sg.Button("No")
# Create the windows layout
layout = [[sg.Text("Which type of cookie would you like:")],
          [sg.Text("Chocolate Chip (C), Oatmeal Raisin (O), or Sugar (S)?")],
          [sg.Button('Chocolate Chip'), sg.Button('Oatmeal Raisin'), sg.Button('Sugar')],
          [sg.Text("Would you like ice cream on that?")],
          [yes_btn, no_btn],
          [total],
          [sg.Button('Generate Recipt')]]

# Create the window
window = sg.Window('Cookie Store', layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or generates their recipt
    # update the price

    if event == sg.WIN_CLOSED or event == 'Generate Recipt':
        newCookie.generate_recipt()
        break
    elif event == 'Chocolate Chip':
        newCookie.type_selector("C")
        # newCookie.update_price()
        total.update("Your total is: $" + str(newCookie.price))
    elif event == 'Oatmeal Raisin':
        newCookie.type_selector("O")
        newCookie.update_price()
        total.update("Your total is: $" + str(newCookie.price))
    elif event == 'Sugar':
        newCookie.type_selector("S")
        newCookie.update_price()
        total.update("Your total is: $" + str(newCookie.price))
    elif event == 'Yes':
        newCookie.add_ice_cream("Yes")
        total.update("Your total is: $" + str(newCookie.price))
        yes_btn.update(disabled=True)
        no_btn.update(disabled=True)
    elif event == 'No':
        newCookie.add_ice_cream("No")
        total.update("Your total is: $" + str(newCookie.price))
        yes_btn.update(disabled=True)
        no_btn.update(disabled=True)

# Old Non GUI Version
# # Selecting Cookie Type
# print("Which type of cookie would you like:")
# userSelection = input("Chocolate Chip (C), Oatmeal Raisin (O), or Sugar (S)?\n")
#
# # Updating Cookie Type
# newCookie.type_selector(userSelection)
# # Updating Cookie Price
# newCookie.update_price()
#
# # Ice Cream Query
# print("Would you like ice cream on that?")
# userSelection = input("Yes or No?\n")
# newCookie.add_ice_cream(userSelection);
#
# # Generate a recipt as a csv file
# newCookie.generate_recipt()
