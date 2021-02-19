import sys, PIL.Image

# ouvre et converti en N&B
# en (mode “L”), the library uses the ITU-R 601-2 luma transform:
# L = R * 299/1000 + G * 587/1000 + B * 114/1000

img = PIL.Image.open(sys.argv[-1]).convert('L')

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
