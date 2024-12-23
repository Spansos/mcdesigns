import mcschematic
from pygame.math import Vector3

def is_cube(coord, side_length, pitch, yaw, roll):
    vec = Vector3(coord)
    vec.rotate_x_ip(pitch)
    vec.rotate_y_ip(yaw)
    vec.rotate_z_ip(roll)
    if vec.x < side_length/2 and vec.x > -side_length/2 and vec.y < side_length/2 and vec.y > -side_length/2 and vec.z < side_length/2 and vec.z > -side_length/2:
        return True
    return False

schem = mcschematic.MCSchematic()

for x in range(-50, 50):
    for y in range(-50, 50):
        for z in range(-50, 50):
            if is_cube((x, y, z), 32, 30, 45, 15):
                schem.setBlock((x, y, z), "minecraft:granite")

schem.save(".", "a", mcschematic.Version.JE_1_20_1)