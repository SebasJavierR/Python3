def diferencia_AB(xa, ya, za, xb, yb, zb):
    dif_x_AB = xa - xb
    dif_y_AB = ya - yb
    dif_z_AB = za - zb
    return dif_x_AB, dif_y_AB, dif_z_AB

def diferencia_AC(xa, ya, za, xc, yc, zc):
    dif_x_AC = xa - xc
    dif_y_AC = ya - yc
    dif_z_AC = za - zc
    return dif_x_AC, dif_y_AC, dif_z_AC

def producto_vectorial(x1, y1, z1, x2, y2, z2):
    pv1 = y1*z2 - z1*y2
    pv2 = z1*x2 - x1*z2 
    pv3 = x1*y2 - y1*x2
    return pv1, pv2, pv3

def area(x, y, z):
    return ((x**2 + y**2 + z**2) ** 0.5)/2

def area_triangulos(xa , ya , za , xb , yb , zb , xc , yc , zc):
    x1 , y1 , z1 = diferencia_AB(xa, ya, za, xb, yb, zb)
    x2 , y2 , z2 = diferencia_AC(xa, ya, za, xc, yc, zc)
    x , y , z = producto_vectorial(x1, y1, z1, x2, y2, z2)
    AreaT = area(x, y, z)
    return AreaT

assert area_triangulos(0,0,0,0,2,0,2,0,0) == 2
assert area_triangulos(7,2,0,7,12,0,17,0,0) == 50
assert area_triangulos(-3,8,0,-3,18,0,7,0,0) == 50
assert area_triangulos(5,-3,0,5,1,0,5,-3,4) == 8
assert area_triangulos(21,-17,4,21,-17,16,21,-5,4) == 72