import mcschematic
import math



def spiral(stop, spacing, vert_spacing, size):
    blocks = set()
    
    for x in range(-size, size+1):
        for y in range(-size, size+1):
            for z in range(-size, size+1):
                r = (math.dist((x,z), (0,0)) + .5)
                theta = math.atan2(x, z) + math.pi

                level = (y+size)/vert_spacing - theta/(2*math.pi)
                if r/spacing%1 < theta/(2*math.pi):
                    level += 1

                size_level = level * spacing + stop

                r_rounded = r//spacing*spacing
                if r_rounded > size_level and not r_rounded > size+spacing:
                    blocks.add((x, y, z))
    
    # r = a*theta+stop
    # a = spacing/2pi

    # 0 = a*theta+stop-r

    return blocks

walls = mcschematic.MCStructure()
# for i in hollow(circle((0,0),56/2+.5)):
#     walls.setBlock((i[0],0,i[1]), "minecraft:cobblestone")
    
schem = mcschematic.MCSchematic()
for i in spiral(8, 4, 16, 32):
    schem.setBlock(i, "minecraft:cobblestone")
schem.setBlock((0,0,0), "minecraft:diamond_block")


# for i in range(64, 64+6):
#     schem.placeStructure(walls, (0, i, 0))

# for i in range(64, 64+8):
#     schem.placeStructure(pillars, (0, i, 0))

schem.save(".", "a", mcschematic.Version.JE_1_20_1)