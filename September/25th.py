# Regular tuple
point = (10, 20)

print(point[0]) # 10
print(point[1]) # 20

# Named tuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
point = Point(x=10, y=20)

print(point.x) # 10
print(point.y) # 20

# Access by index still works
print(point[0]) # 10

# Unpacking works for both
x, y = point
print(x, y) # 10 20

# Methods
print(point._asdict()) # OrderedDict([('x', 10), ('y', 20)])

new_point = point._replace(x=5)
print(new_point) # Point(x=5, y=20)