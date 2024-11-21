import mcschematic

def disk(radius):
    # can be improved with different algorithm
    schem = mcschematic.MCSchematic()
    for x in range(-radius, radius+1):
        for z in range(-radius, radius+1):
            if x**2 + z**2 < radius**2:
                schem.setBlock((x, 0, z), "minecraft:cobblestone")
    return schem


def hollow(schem, axiis=(True,True,True)):
    pass


schem = disk(25)
# schem.setBlock((0, 0, 0), "minecraft:cobblestone")
# schem.save(".", "a", mcschematic.Version.JE_1_18_2)

# for i in range(-50, 51):
#     for j in range(-50, 51):
#         print('.' if schem.getBlockDataAt((i, 0, j)) == 'minecraft:air' else '#', end='')
#     print()

print(len(schem))