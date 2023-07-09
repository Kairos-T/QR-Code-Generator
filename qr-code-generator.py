import qrcode
import re

def generate_qr_code(data, fill_color_choice='black', filename='qr_code.png'):
    color_mapping = {
        'black': '#000000',
        'white': '#ffffff',
        'red': '#ff0000',
        'green': '#00ff00',
        'blue': '#0000ff',
    }

    fill_color = color_mapping.get(fill_color_choice.lower(), fill_color_choice)

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color='#ffffff')
    img.save(filename)

    print("QR code saved as", filename, "in the same directory.")

data = input("Enter website/data to encode: ")
fill_color_choice = input("Enter fill color (black, white, red, green, blue, or custom hex code): ")
filename = input("Enter filename to save QR code as (include .png extension): ")

# Validate inputs and provide default values if necessary
if not data:
    print("Data cannot be empty.")
    exit()

if not fill_color_choice:
    fill_color_choice = 'black'

if not re.match(r'^[a-fA-F0-9]{6}$', fill_color_choice):
    print("Invalid custom hex code.")
    exit()

if not filename:
    filename = 'qr_code.png'

generate_qr_code(data, fill_color_choice, filename)
