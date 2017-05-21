import math

def area_square(length):
    return str(length*4)+" cm2" 

def area_circle(radius):
    return str(3.14*radius**2)+" cm2" 

def area_rectangle(width,height):
    return str(width*height)+" cm2" 

def area_triangle(base,height):
    return str((base*.5) * height)+" cm2" 

def area_parallelogram(base,height):
    return str(base*height)+" cm2" 

def area_trapezoid(a,b,height):
    return str((a+b)*(height)/2)+" cm2" 

def area_ellipse(Aaxis,Baxis):
    return str(3.14*Aaxis*Baxis)+" cm2" 

def area_trapezium(a,b,height):
    return str((a+b)*(height)/2)+" cm2" 

def area_cylinder(radius,height):
    a=6.28*(radius**2)
    b=6.28*radius*height
    return str(a+b)+" cm2" 

def area_rhombus(Pdiagonal,Qdiagonal):
    return str((Pdiagonal*Qdiagonal)/2)+" cm2" 

def area_sphere(radius):
    return str(12.56*(radius**2))+" cm2" 

def area_cube(edges):
    return str(6*(edges**2))+" cm2" 

def area_kite(Pdiagonal,Qdiagonal):
    return str((Pdiagonal*Qdiagonal)/2)+" cm2"

def area_octagon(sides):
    a = sides**2
    b = 4.828
    return str(a*b)+" cm2"

def area_hexagon(sides):
    return str(2.5980*sides**2)+" cm2"

def area_heptagon(sides):
    return str((1.75*sides**2)*2.0765)+ " cm2"

def area_cone(radius,height):
    a = 3.14 * radius
    b = radius + (math.sqrt((height ** 2)+(radius ** 2)))
    return a*b
    
