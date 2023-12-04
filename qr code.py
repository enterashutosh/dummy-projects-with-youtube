import qrcode as qr
from PIL import Image
link = "text-a-random"

'''
excuse the primitive way:

img = qr.make(link)
img.save("random qr.jpg")
'''

my_qr = qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_L, box_size=10, border=4)

my_qr.add_data(link)
my_qr.make(fit=True)

img = my_qr.make_image(fill_color="red", back_color="white")

img.save("my_qr3.png")

img.show()