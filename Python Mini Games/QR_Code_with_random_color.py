import random
import qrcode
import uuid

# Generate a random color
def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

# Generate a QR code with a random color
qr = qrcode.QRCode()
# qr.add_data('www.youtube.com')
# qr.add_data('www.verge.com')
qr.add_data('www.instagram.com')

qr.make()
img = qr.make_image(fill_color="darkred", back_color="white")
file_name = (str(uuid.uuid1())).split("-")

# Change User_name = Your username in computer.
img.save(f'c:/Users/User_name/Desktop/{file_name[0]}.png')