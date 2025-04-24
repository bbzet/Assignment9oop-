from shapes import Sphere, Cylinder, Cube
from abstract import Shape3D
import random

shapes = []
for i in range(10):
    shape_type = random.choice(['Sphere', 'Cylinder', 'Cube'])
    if shape_type == 'Sphere':
        radius = random.randint(1, 10)
        shapes.append(Sphere(radius))
    elif shape_type == 'Cylinder':
        radius = random.randint(1, 10)
        height = random.randint(5, 20)
        shapes.append(Cylinder(radius, height))
    elif shape_type == 'Cube':
        side_length = random.randint(1, 10)
        shapes.append(Cube(side_length))

for shape in shapes:
    print(f"Shape: {type(shape).__name__}")
    print(f"Surface Area: {shape.surface_area():.2f}")
    print(f"Volume: {shape.volume():.2f}")
    print()