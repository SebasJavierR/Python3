def mi_funcion(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve el producto vectorial"""
    var1 = y1*z2 - z1*y2
    var2 = z1*x2 - x1*z2 
    var3 = x1*y2 - y1*x2
    return var1, var2, var3

assert mi_funcion(54, 12, 29, 1, 11, 12) == (-175, -619, 582)
assert mi_funcion(71, 52, 24, 1, 11, 6) == (48, -402, 729)
assert mi_funcion(726, 434, 110, 488, 962, 820) == (250060, -541640, 486620)
assert mi_funcion(62, 12, 198, 380, 334, 490) == (-60252, 44860, 16148)
assert mi_funcion(-85, 807, 964, 462, 101, 474) == (285154, 485658, -381419)
assert mi_funcion(746, 466, 396, 910, 138, 289) == (80026, 144766, -321112)
assert mi_funcion(-15, 53, 105, 413, 149, 270) == (-1335, 47415, -24124)
assert mi_funcion(291, 413, 227, 166, 638, 284) == (-27534, -44962, 117100)
assert mi_funcion(192, 362, 397, 249, 598, 50) == (-219306, 89253, 24678)
assert mi_funcion(781, 520, 996, 348, 68, 215) == (44072, 178693, -127852)
assert mi_funcion(459, 971, 201, 582, 569, 703) == (568244, -205695, -303951)
assert mi_funcion(754, 968, 956, 231, 901, -31) == (-891364, 244210, 455746)

