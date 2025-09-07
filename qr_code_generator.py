# Using the library from  https://pypi.org/project/qrcode/ we are using to generate QR codes for a user after entering a URL link 
# and saving the file in the same location folder

import qrcode

# input data and filename
data = input("Enter some text or a URL: ").strip()
filename = input("Enter the filename: ").strip()

# QR code generator
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
# image creation and saving into file
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)

# print name
print(f"QR code saved as {filename}")
