import qrcode
import PIL
import os

def cls():
    print('\n'*50)

cls()

FolderName='QRCOdes'

if not os.path.exists(FolderName):
    os.makedirs(FolderName)

InputVariable = input("Add Text, URL, Or Referece to me converted to a QR Code:")
img = qrcode.make(InputVariable)
FileName = input("Enter a name for the QR Image file:")

FilePath = os.path.join(FolderName,FileName+'.jpg')

FileNotExists = 0
if os.path.exists(FilePath):
    print('File Exists - Overwriting Existing File')

img.save(FilePath)

os.startfile(FilePath)
