import qrcode

black = '#000000'
white = '#ffffff'
red = '#ff0000'
green = '#00ff00'
blue = '#0000ff'

data = input("Enter website/data to encode: ")
fill_color_choice = input("Enter fill color (black, white, red, green, blue, or custom hex code): ")


if fill_color_choice.lower() == 'black':
    fill_color = black
elif fill_color_choice.lower() == 'white':
    fill_color = white
elif fill_color_choice.lower() == 'red':
    fill_color = red
elif fill_color_choice.lower() == 'green':
    fill_color = green
elif fill_color_choice.lower() == 'blue':
    fill_color = blue
else:
    # If not a preset variable, assume custom hex code input
    fill_color = fill_color_choice

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color=fill_color, back_color=white)

filename = input("Enter filename to save QR code as (include .png extension): ")
img.save(filename)

print("QR code saved as", filename, "in the same directory.")