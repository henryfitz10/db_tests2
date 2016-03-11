#'normal' tuple
pt1= (1.0, 2.6, 2.0)

print pt1[0]

# named tuple
from collections import namedtuple

Point = namedtuple('Point', 'x_coordinate,y_coordinate, z_coordinate')

pt2 = Point(1.2, 3.4, 2.0)

print pt2.z_coordinates

