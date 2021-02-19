import PySimpleGUI as sg
import sys, PIL.Image

def Atkinson(filename):
  img = PIL.Image.open(filename).convert('L')

  # définiion d'un tableau 
  # retourne 0 (noir) pour 0 à 127 et 255 (blanc) pour 128 à 255
  threshold = 128*[0] + 128*[255]

  for y in range(img.size[1]):
      for x in range(img.size[0]):

          old = img.getpixel((x, y))
          new = threshold[old]
          # Atkinson 1/8ème de l'erreur à distribuer sur 6 pixels voisins
          err = (old - new) >> 3 # divide by 8
              
          img.putpixel((x, y), new) # pose un pixel blanc ou noir
          
          # 6 pixels voisins
          #                            X      1/8     1/8
          #                    1/8    1/8     1/8
          #                           1/8
          for nxy in [(x+1, y), (x+2, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x, y+2)]:
              try:
                  img.putpixel(nxy, img.getpixel(nxy) + err)
              except IndexError:
                  pass

  img.show()
  return img

pictureName = "femmes1000x700.png"
imageElem = sg.Image(filename=pictureName, size=(1000,700), key='__IMAGE__')

sg.theme("DarkTeal2")
layout = [
          [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")],
          [sg.Button("Conversion Atkinson", key="Submit"), sg.Button("Cat"), sg.Button("Quit")],
          [imageElem]
         ]

###Building Window
window = sg.Window('Atkinson conversion with PySimpleGUI', layout, size=(1200,800))
    
while True:
    event, values = window.read()
    if event == "Exit":
        break
    elif event == "Submit":
        #print(values["-IN-"])
        newImg = Atkinson(values["-IN-"])
    elif event == "Cat":
        pictureName = "cat.png"
        imageElem.Update(filename=pictureName)
    elif event == "Quit":
        break

