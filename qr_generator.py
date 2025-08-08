import qrcode
print("Welcome to QR code Generator\n")
data = "https://www.youtube.com"
qr=qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="red",back_color="yellow")
img.save("myqr.png")
print("succesfully qr code is generated\n")