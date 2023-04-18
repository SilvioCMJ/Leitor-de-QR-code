from PIL import Image
from pyzbar.pyzbar import decode

read = decode(Image.open('qrcodeexemplo.png'))
print(read[0].data)