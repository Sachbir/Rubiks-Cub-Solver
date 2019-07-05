from RubiksCube import RubiksCube
from Cubelet import Cubelet

cube = RubiksCube()
cube.initialize_cube()
cube.print_cube()

print("\n\n\n")

cube.rotate_face_cw(cube.get_back_cubelets(), Cubelet.turn_f_ccw, cube.set_back_cubelets)
cube.print_cube()

print("\n\n\n")

cube.rotate_face_ccw(cube.get_back_cubelets(), Cubelet.turn_f_cw, cube.set_back_cubelets)
cube.print_cube()
