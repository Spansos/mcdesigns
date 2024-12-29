import xml.etree.ElementTree as ET
from pygame import image
import mcschematic

font = "fonts/thick_8x8"
text = "BIG HOLE\nin progress"

color_block_mappings = {
    (255, 255, 255, 0): "minecraft:air",
    (255, 255, 255, 255): "minecraft:dirt",
    (220, 220, 220, 0): "minecraft:air",
}

png = image.load(f'{font}.png')
xml = ET.parse(f'{font}.xml')

lineheight = int(xml.find('common').get('lineHeight'))

chars = {}
for char in xml.findall('chars/char'):
    ch, x, y, width, height, advance = chr(int(char.get('id'))), char.get('x'), char.get('y'), char.get('width'), char.get('height'), char.get('xadvance')
    chars[ch] = {'pos': (int(x), int(y)), 'size': (int(width), int(height)), 'advance': int(advance)}


schem = mcschematic.MCSchematic()

curser = [0, 0]
for char in text:
    if char == '\n':
        curser[1] += lineheight
        curser[0] = 0
        continue

    ch = chars[char]
    for x in range(ch['size'][0]):
        for y in range(ch['size'][1]):
            block = color_block_mappings[tuple(png.get_at((ch['pos'][0]+x, ch['pos'][1]+y)))]
            px, py = curser[0]+x, curser[1]+y
            schem.setBlock((px, 0, py), block)

    curser[0] += ch['advance']

schem.save(".", "a", mcschematic.Version.JE_1_20_1)