import qrcode 

qr =qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=10,
	border=4,	
	)

# qr.add_data ('https://www.google.com')#pagina web
qr.add_data ('https://api.whatsapp.com/send?phone=+5400000000')#whatsapp
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

img.save("whatsapp.png")