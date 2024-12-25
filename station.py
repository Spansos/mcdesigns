import mcschematic
import math



def hole(stop, spacing, vert_spacing, layerc):
    blocks = set()
    
    height = layerc*vert_spacing+1
    radius = stop + spacing*(layerc+1)+1

    print(f"big hole depth: {height}, radius: {radius}")

    for x in range(math.floor(-radius), math.ceil(radius+1)):
        for y in range(height):
            for z in range(math.floor(-radius), math.ceil(radius+1)):
                r = (math.dist((x,z), (0,0)) + .5)
                theta = math.atan2(x, z) % (math.pi*2)

                level = y/vert_spacing - theta/(2*math.pi)
                if r/spacing%1 < theta/(2*math.pi):
                    level += 1

                size_level = level * spacing + stop

                r_rounded = r//spacing*spacing
                if r_rounded > size_level and not r > radius:
                    blocks.add((x, y, z))

    return blocks

# should continue later with roof + outside platform + actual station, but for now ill leave it as a big hole
def outer_floor(level, tube_height, inner_radius, outer_radius, half_width, half_length, floor_height):
    blocks = set()

    for x in range(math.floor(-outer_radius), math.ceil(outer_radius+1)):
        for z in range(math.floor(-outer_radius), math.ceil(outer_radius+1)):
            for y in range(-tube_height+1, 0+1):
                if inner_radius < math.dist((x,z), (0,0)) < outer_radius:
                    blocks.add((x, level+y, z))

    # for x in range(math.floor(-half_width), math.ceil(half_width+1)):
    #     for z in range(math.floor(-half_length), math.ceil(half_length+1)):
    #         for y in range(-floor_height+1, 0+1):
    #             if math.dist((x,z), (0,0)) >= outer_radius:
    #                 blocks.add((x, level-12+y, z))

    return blocks

    
schem = mcschematic.MCSchematic()
for i in hole(16, 4, 16, 5):
    schem.setBlock(i, "minecraft:cobblestone")

# for i in outer_floor(80, 12, 40.5, 45, 64, 128, 8):
#     schem.setBlock(i, "minecraft:cobblestone")

struc = schem.getStructure()
slabs = set()
for i in struc.blockStateIterator():
    pos = i[0]
    if struc.getBlockDataAt((pos[0], pos[1]+1, pos[2])) == "minecraft:air":
        slabs.add((pos[0], pos[1]+1, pos[2]))
for slab in slabs:
    schem.setBlock(slab, "minecraft:cobblestone_slab")

schem.setBlock((0,0,0), "minecraft:diamond_block")


# for i in range(64, 64+6):
#     schem.placeStructure(walls, (0, i, 0))

# for i in range(64, 64+8):
#     schem.placeStructure(pillars, (0, i, 0))

schem.save(".", "a", mcschematic.Version.JE_1_20_1)