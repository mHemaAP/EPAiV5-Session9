# EPAiV5-Session9 - Regular strictly Convex Polygon - Functionality

## Overview
This repository contains two Python modules, regularpolygon.py and polygonsequence.py, that are designed to work with regular polygons. These modules provide classes to represent individual regular polygons and sequences of polygons, with functionality to calculate various properties and compare polygons based on their characteristics.

## Modules
**regularpolygon.py**: Defines the '**RegularPolygon**' class, which represents a single regular polygon with methods to calculate its geometric properties like the area and perimeter (and also other parameters) given the number of edges and circum radius.

**polygonsequence.py**: Defines the '**PolygonSequence**' class, which represents a sequence of regular polygons, allowing for calculations of area-to-perimeter ratios, comparisons between polygons, and maximum efficiency polygon (highest area to perimeter ratio), given the circum radius and the vertex count for the largest polygon fed. It uses the functional properties of '**RegularPolygon**'. 

## "Regular Polygon" & Properties

### **Definition**

A **Regular Convex Polygon** is a special type of polygon that satisfies the following conditions:

1.  **Equal Side Lengths**: All sides of the polygon are of the same length. This means the distance between any two adjacent vertices (corners) of the polygon is identical.
    
2.  **Equal Angles**: All interior angles (the angles inside the polygon) are equal. This uniformity ensures the symmetry of the shape.
    
3.  **Convexity**: The polygon is convex, which means that all its interior angles are less than 180 degrees. In other words, no part of the polygon is "indented" or "caved in"; the line segment between any two points on the polygon's boundary always lies inside or on the polygon.
    

#### **Examples**

-   **Equilateral Triangle**: A triangle with three equal sides and three equal angles of 60 degrees each.
-   **Square**: A four-sided polygon with equal sides and four equal 90-degree angles.
-   **Regular Pentagon**: A five-sided polygon with equal sides and equal angles, each of 108 degrees.

#### **Properties of Regular Convex Polygons**

1.  **Number of Sides (n)**: The number of sides (or edges) of a regular polygon is denoted by $n$. This also equals the number of vertices.
    
2.  **Interior Angle**: The measure of each interior angle $\theta$ of a regular polygon is given by:
   
    $$
    {Interior Angle, \theta} = \frac{(n - 2) \times 180^\circ}{n}
    $$
    
    This formula comes from dividing the total interior angle sum of a polygon which is $(n-2) \times 180^\circ$ by the number of angles $n$.
    
3.  **Edge Length**: The exterior angle of a regular polygon (the angle between one side of the polygon and the extension of an adjacent side) is:
    $$
    {Edge Length, s} = 2 \times R \times \sin\left(\frac{\pi}{n}\right)
    $$   
    
4.  **Circumradius**: The circumradius $R$ is the radius of the circle that passes through all the vertices of the polygon. 
    
5.  **Apothem**: The apothem is the distance from the center of the polygon to the midpoint of one of its sides. It is also the radius of the inscribed circle within the polygon. The apothem $r$ can be calculated using:
    
    $$
    {Apothem, a} = R \times \cos\left(\frac{\pi}{n}\right)
    $$
6.  **Area**: The area $A$ of a regular convex polygon can be computed using:
    $$
    {Area, A} = \frac{1}{2} \times n \times s \times a
    $$     
7.  **Perimeter**: The perimeter $P$ of a regular polygon is simply the number of sides multiplied by the side length:
    $$
    {Perimeter, P} = n \times s
    $$ 


## Class Descriptions
### RegularPolygon (in regularpolygon.py)
The RegularPolygon class provides methods to calculate and return various properties of a regular polygon, including:

- **__init__**: Initializes the class local variables and also does validation of class arguments
- **vertices**, **edges** : Returns the number of vertices, edges of the polygon.
- **interior_angle**: Returns the interior angle of the polygon.
- **edge_length**: Returns the length of each edge of the polygon.
- **apothem**: Returns the apothem of the polygon.
- **area**: Returns the area of the polygon.
- **perimeter**: Returns the perimeter of the polygon.
- **__repr__**: Returns a string representation of the polygon object.
- **__eq__**: Checks if two polygons are equal based on the number of edges and circumradius.
- **__gt__**: Compares two polygons based on the number of edges.

### PolygonSequence (in polygonsequence.py)
The PolygonSequence class represents a sequence of regular polygons and provides the following functionality:

- **__init__**: Initializes the sequence with a given maximum number of vertices and a common circumradius. It also validates the class arguments
- **calculate_polygon_sequences**: Calculates the area-to-perimeter ratio for all polygons in the sequence.
- **max_efficiency_polygon**: Returns the polygon with the highest area-to-perimeter ratio.
- **__len__**: Returns the number of polygons in the sequence.
- **__getitem__**: Allows access to the area-to-perimeter ratio by index.
- **__repr__**: Returns a string representation of the polygon sequence.

## Usage

**Example (RegularPolygon)**:

```
from regularpolygon import RegularPolygon

# Create a RegularPolygon object with 5 edges and a circumradius of 10
polygon = RegularPolygon(5, 10)

# Access various properties
print(polygon.vertices)          # 5
print(polygon.interior_angle)    # 108.0
print(polygon.edge_length)       # 11.755705045849464
print(polygon.apothem)           # 8.090169943749475
print(polygon.area)              # 237.76412907378838
print(polygon.perimeter)         # 58.77852522924732

# String representation
print(polygon)                   # Polygon(n_edges=5, circum_radius=10, interior_angle=108.00, edge_length=11.76, apothem=8.09, area=237.76, perimeter=58.78)

# Equality and comparison
polygon2 = RegularPolygon(7, 10)
print(polygon == polygon2)       # False
print(polygon > polygon2)        # False
```

**Example (PolygonSequence)**:

```
from polygonsequence import PolygonSequence

# Create a PolygonSequence object with up to 10 vertices and a circumradius of 15
sequence = PolygonSequence(10, 15)

# Access properties and methods
print(len(sequence))                        # 8 (sequence from 3 to 10 vertices)
print(sequence[0])                          # Area-to-perimeter ratio for the polygon with 3 edges
print(sequence[-1])                         # Area-to-perimeter ratio for the polygon with 10 edges

# Find the most efficient polygon (with max area-to-perimeter ratio)
sequence.max_efficiency_polygon()           # Prints the max ratio and corresponding polygon vertex count

# String representation
print(sequence)                             # PolygonSequence with area-to-perimeter ratios for polygons with 3 to 10 vertices

```

## Testing
Both classes are tested in a Python environment by importing the modules and creating instances of '**RegularPolygon**' and '**PolygonSequence**'. This reporsitory contains a Jupyter Notebook where the functionality of both the classes are tested. The provided examples in the usage section demonstrate how to create objects and access the various properties and methods.


## Applications

Regular convex polygons appear in various fields, including:

-   **Geometry**: Studying the properties and relationships between angles, sides, and other geometric elements.
-   **Architecture**: Designing buildings, tiling patterns, and structures with symmetrical shapes.
-   **Computer Graphics**: Rendering shapes with uniformity and symmetry in digital art and animation.
-   **Tessellations**: Filling a plane with no gaps using identical regular polygons.

### Common Regular Convex Polygons

-   **Equilateral Triangle** (3 sides)
-   **Square** (4 sides)
-   **Regular Pentagon** (5 sides)
-   **Regular Hexagon** (6 sides)
-   **Regular Octagon** (8 sides)

---------------------------------------------------------------------------------------------------------------------------------------------------

**Submission by** - Hema Aparna M

**mail id** - mhema.aprai@gmail.com

---------------------------------------------------------------------------------------------------------------------------------------------------