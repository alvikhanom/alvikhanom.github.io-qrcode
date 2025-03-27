import os
import qrcode

website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color='black', back_color='white')
file_path = 'youtube_qr.png'
img.save(file_path)

# Debugging information
print("QR code saved to:", os.path.abspath(file_path))
if os.path.exists(file_path):
    print("File exists:", file_path)
else:
    print("File not found:", file_path)
