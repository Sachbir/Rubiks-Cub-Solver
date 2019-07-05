from RubiksCube import RubiksCube

cube = RubiksCube()
cube.initialize_cube()
cube.print_cube()

print("\n\n\n")

cube.turn_r()
cube.print_cube()

print("\n\n\n")

cube.turn_r_inv()
cube.print_cube()