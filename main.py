import random, requests
import numpy as np

import imageio as iio
from cmath import sqrt

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def getrandomlab():
    seed = ""
    for i in range(10):
        seed += str(random.randint(0, 9))
    print(seed)
    url = f'https://donjon.bin.sh/fantasy/dungeon/preview.cgi?seed={seed}&dungeon_layout=Square&peripheral_egress=Many&room_layout=&room_size=Medium&room_polymorph=Yes&door_set=Standard&corridor_layout=Labyrinth&remove_deadends=&add_stairs=&map_style=Standard&grid=None&dungeon_size=Preview'

    with open('lab.png', 'wb') as file:
        file.write(requests.get(url).content)

def getvertex(lab):
    vertex = 0
    
    for lang in range(10):
        coords = lab[lang, lang]
        if coords.all() == 255:
            break
        if coords.all() == 0:
            vertex += 1
        else:
            print(f'NOT BLACK OR WHITE! COLOR: {coords}')
    return vertex
    
    

    

# Initialize essentials
cell_width = (6)
pic = iio.imread('./lab.png')
fig, ax = plt.subplots()
pathrect = patches.Rectangle((0, 0), cell_width, cell_width, facecolor='g')
ax.imshow(pic)
ax.add_patch(pathrect)
plt.show()
