import mcschematic

def disk(radius):
    # can be improved with different algorithm
    schem = mcschematic.MCSchematic()
    for x in range(-radius, radius+1):
        for z in range(-radius, radius+1):
            if x**2 + z**2 < radius**2:
                schem.setBlock((x, 0, z), "minecraft:cobblestone")
    return schem

def hollow(schem : mcschematic.MCSchematic, axiis=(True,True,True)):
    # doesnt actually work how it should since not full axis if off is filled
    bounds = schem.getStructure().getBounds()
    bounds = (tuple([i-1 for i in bounds[0]]), tuple([i+1 for i in bounds[1]]))
    
    doing = set([bounds[0]])
    done = set()
    structure = set()

    while doing:
        cur = doing.pop()

        for axis in range(3):
            for way in (-1, 1):
                new = list(cur)
                new[axis] += way
                new = tuple(new)

                if axiis[axis] and new not in done and new[0] >= bounds[0][0] and new[0] <= bounds[1][0] and new[1] >= bounds[0][1] and new[1] <= bounds[1][1] and new[2] >= bounds[0][2] and new[2] <= bounds[1][2]:
                    if schem.getBlockDataAt(new) != 'minecraft:air':
                        structure.add(new)
                    else:
                        doing.add(new)
        
        done.add(cur)
    
    r_schem = mcschematic.MCSchematic()
    for block in structure:
        r_schem.setBlock(block, schem.getBlockDataAt(block))
    
    return r_schem
    

                    


schem = hollow(disk(25), (True, False, True))
# schem.setBlock((0, 0, 0), "minecraft:cobblestone")
# schem.save(".", "a", mcschematic.Version.JE_1_18_2)

for i in range(-50, 51):
    for j in range(-50, 51):
        print('.' if schem.getBlockDataAt((i, 0, j)) == 'minecraft:air' else '#', end='')
    print()