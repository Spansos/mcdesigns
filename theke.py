import math
import mcschematic

center = (-3193, -1193)

blocks = set([
    (-3193, -1244),
    (-3192, -1244),
    (-3191, -1244),
    (-3190, -1244),
    (-3189, -1245),
    (-3188, -1245),
    (-3187, -1246),
    (-3186, -1246),
    (-3185, -1247),
    (-3184, -1248),
    (-3183, -1249),
    (-3182, -1250),
    (-3182, -1251),
    (-3181, -1252),
    (-3181, -1253),
    (-3180, -1254),
    (-3180, -1255),
    (-3179, -1254),
    (-3178, -1254),
    (-3177, -1254),
    (-3176, -1254),
    (-3175, -1253),
    (-3174, -1253),
    (-3173, -1253),
    (-3173, -1252),
    (-3174, -1251),
    (-3174, -1250),
    (-3174, -1249),
    (-3174, -1248),
    (-3174, -1247),
    (-3174, -1246),
    (-3174, -1245),
    (-3173, -1244),
    (-3173, -1243),
    (-3172, -1242),
    (-3172, -1241),
    (-3171, -1240),
    (-3170, -1239),
    (-3169, -1238),
    (-3168, -1237),
    (-3167, -1237),
    (-3166, -1236),
    (-3165, -1236),
    (-3164, -1235),
    (-3163, -1235),
    (-3162, -1235),
    (-3161, -1235),
    (-3160, -1235),
    (-3159, -1235),
    (-3158, -1235),
    (-3157, -1236),
    (-3156, -1236),
    (-3155, -1237),
    (-3154, -1237),
    (-3153, -1238),
    (-3152, -1239),
    (-3151, -1240),
    (-3150, -1240),
    (-3149, -1239),
    (-3148, -1238),
])

def line_low(x0, y0, x1, y1):
    blocks = set()

    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy

    D = (2 * dy) - dx
    y = y0

    for x in range(x0, x1+1):
        blocks.add((x, y))
        if D > 0:
            y = y + yi
            D = D + (2 * (dy - dx))
        else:
            D = D + 2*dy

    return blocks

def line_high(x0, y0, x1, y1):
    blocks = set()

    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx

    D = (2 * dx) - dy
    x = x0

    for y in range(y0, y1+1):
        blocks.add((x, y))
        if D > 0:
            x = x + xi
            D = D + (2 * (dx - dy))
        else:
            D = D + 2*dx
    
    return blocks

def line(point1, point2):
    x0, y0 = point1[0], point1[1]
    x1, y1 = point2[0], point2[1]

    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            return line_low(x1, y1, x0, y0)
        else:
            return line_low(x0, y0, x1, y1)
    else:
        if y0 > y1:
            return line_high(x1, y1, x0, y0)
        else:
            return line_high(x0, y0, x1, y1)

def fill(coords, start):
    doing = set([start])
    done = coords.copy()

    while doing:
        cur = doing.pop()
        
        if (cur[0]+1, cur[1]) not in done: doing.add((cur[0]+1, cur[1]))
        if (cur[0]-1, cur[1]) not in done: doing.add((cur[0]-1, cur[1]))
        if (cur[0], cur[1]+1) not in done: doing.add((cur[0], cur[1]+1))
        if (cur[0], cur[1]-1) not in done: doing.add((cur[0], cur[1]-1))

        done.add(cur)

    
    return done.difference(coords)

# outer outline
outline = mcschematic.MCStructure()

for i in blocks:
    outline.setBlock((i[0], 0, i[1]), "minecraft:cobblestone")
outline.placeStructure(outline.makeCopy().flip((center[0], 0, center[1]), 'xy'), (0, 0, 0))
outline.placeStructure(outline.makeCopy().flip((center[0], 0, center[1]), 'yz'), (0, 0, 0))
outline.placeStructure(outline.makeCopy().rotateDegrees((center[0], 0, center[1]), yaw=90), (0,0,0))
outline.center(outline.getBounds())

# outer walls
walls = mcschematic.MCStructure()
for i in range(12):
    walls.placeStructure(outline, (0, i, 0))

# second outline
radius = 44
pointc = 8
points = [(round(math.cos(i/pointc*math.pi*2)*radius), round(math.sin(i/pointc*math.pi*2)*radius)) for i in range(pointc)]
outline2 = set()
for i in range(pointc):
    for block in line(points[i], points[(i+1)%pointc]):
        outline2.add((block[0], block[1]))

# third outline
radius -= 8
pointc = 8
points = [(round(math.cos(i/pointc*math.pi*2)*radius), round(math.sin(i/pointc*math.pi*2)*radius)) for i in range(pointc)]
outline3 = set()
for i in range(pointc):
    for block in line(points[i], points[(i+1)%pointc]):
        outline3.add((block[0], block[1]))

# fourth outline
radius -= 8
pointc = 8
points = [(round(math.cos(i/pointc*math.pi*2)*radius), round(math.sin(i/pointc*math.pi*2)*radius)) for i in range(pointc)]
outline4 = set()
for i in range(pointc):
    for block in line(points[i], points[(i+1)%pointc]):
        outline4.add((block[0], block[1]))

# fifth outline
radius -= 8
pointc = 8
points = [(round(math.cos(i/pointc*math.pi*2)*radius), round(math.sin(i/pointc*math.pi*2)*radius)) for i in range(pointc)]
outline5 = set()
for i in range(pointc):
    for block in line(points[i], points[(i+1)%pointc]):
        outline5.add((block[0], block[1]))

# sixth outline
radius -= 8
pointc = 8
points = [(round(math.cos(i/pointc*math.pi*2)*radius), round(math.sin(i/pointc*math.pi*2)*radius)) for i in range(pointc)]
outline6 = set()
for i in range(pointc):
    for block in line(points[i], points[(i+1)%pointc]):
        outline6.add((block[0], block[1]))

# first floor
level = 0
blocks = set([(i[0], i[2]) for i in outline.getBlockStates().keys()]).union(outline2)
floor_blocks = fill(blocks, (46, 0))
floor1 = mcschematic.MCStructure()
for block in floor_blocks:
    floor1.setBlock((block[0], level, block[1]), "minecraft:cobblestone_slab")

# second floor
level -= 6
blocks = outline2.union(outline3)
floor_blocks = fill(blocks, (38, 0))
floor2 = mcschematic.MCStructure()
for block in floor_blocks:
    floor2.setBlock((block[0], level, block[1]), "minecraft:cobblestone_slab")

# third floor
level -= 6
blocks = outline3.union(outline4)
floor_blocks = fill(blocks, (30, 0))
floor3 = mcschematic.MCStructure()
for block in floor_blocks:
    floor3.setBlock((block[0], level, block[1]), "minecraft:cobblestone_slab")

# fourth floor
level -= 6
blocks = outline4.union(outline5)
floor_blocks = fill(blocks, (24, 0))
floor4 = mcschematic.MCStructure()
for block in floor_blocks:
    floor4.setBlock((block[0], level, block[1]), "minecraft:cobblestone_slab")

# fifth floor
level -= 6
blocks = outline5.union(outline6)
floor_blocks = fill(blocks, (14, 0))
floor5 = mcschematic.MCStructure()
for block in floor_blocks:
    floor5.setBlock((block[0], level, block[1]), "minecraft:cobblestone_slab")

# sixth floor
level -= 6
floor_blocks = fill(outline6, (0, 0))
floor6 = mcschematic.MCStructure()
for block in floor_blocks:
    floor6.setBlock((block[0], level, block[1]), "minecraft:cobblestone_slab")

for i, o in enumerate((outline2, outline3, outline4, outline5, outline6)):
    for b in o:
        for y in range(i*-6-6, i*-6+1):
            walls.setBlock((b[0], y, b[1]), "minecraft:cobblestone")
        walls.setBlock((b[0], i*-6+1, b[1]), "minecraft:cobblestone_slab")
        

# floor_blocks = fill(blocks, (49,0,0))
# floor = mcschematic.MCStructure()

# for i in floor_blocks:
#     floor.setBlock((i[0], 0, i[1]), "minecraft:cobblestone_slab")

# def distance(coord1, coord2):
#     return math.sqrt(sum([(i-j)**2 for i, j in zip(coord1, coord2)]))

final = mcschematic.MCStructure()
final.placeStructure(walls, (0,0,0))
final.placeStructure(floor1, (0,0,0))
final.placeStructure(floor2, (0,0,0))
final.placeStructure(floor3, (0,0,0))
final.placeStructure(floor4, (0,0,0))
final.placeStructure(floor5, (0,0,0))
final.placeStructure(floor6, (0,0,0))
# final.placeStructure(outline, (0,0,0))
# final.placeStructure(outline_2, (0,0,0))

schem = mcschematic.MCSchematic(final)
schem.getStructure().center(schem.getStructure().getBounds())
schem.save(".", "a", mcschematic.Version.JE_1_20_1)