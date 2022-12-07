import atheris
import sys
from image_to_ascii import ImageToAscii

atheris.instrument_all()

def TestOneInput(data):
  try:
    decompressed = Image.frombuffer("L", (20, 20), data, "raw", "L", 0, 1)
    decompressed.save("input.png", "PNG")
   except:
    return
   
   save_stdout = sys.stdout
   sys.stdout = open('trash', 'w')
   ImageToAscii(imagePath="input.png", outputFile="output.txt")
   sys.stdout = save_stdout
  
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
