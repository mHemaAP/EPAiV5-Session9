import math

class RegularPolygon:
    def __init__(self, num_edges, circum_radius):
        '''
        Initialize the convex polygon with its number of edges and circum radius.
        '''
        if not isinstance (num_edges, int):
            raise TypeError ('Polygons will have edges of type int')
        
        if not (isinstance(circum_radius, float) or isinstance(circum_radius, int)):
            raise TypeError ('Polygon circum radius must be either int or float')

        if circum_radius <= 0:
            raise ValueError ('Polygon\'s circum radius must a valid positive real number')
        
        if num_edges < 3:
            raise ValueError("A polygon must have at least 3 edges.")
        
        self.num_edges = num_edges
        self.circum_radius = circum_radius

    @property
    def vertices(self):
        '''
        Returns the number of vertices of the given polygon.
        '''
        return self.num_edges

    @property
    def edges(self):
        '''
        Returns the number of edges or sides of the given polygon.
        '''
        return self.num_edges

    @property
    def interior_angle(self):
        '''
        Returns the interior angle of the given polygon.
        '''
        return (self.num_edges - 2) * 180 / self.num_edges

    @property
    def edge_length(self):
        '''
        Returns the number of edge length of the given polygon.
        '''
        return 2 * self.circum_radius * math.sin(math.pi / self.num_edges)

    @property
    def apothem(self):
        '''
        Returns the apothem of the given polygon.
        '''
        return self.circum_radius * math.cos(math.pi / self.num_edges)

    @property
    def area(self):
        '''
        Returns the area of the given polygon.
        '''
        return 0.5 * self.num_edges * self.edge_length * self.apothem

    @property
    def perimeter(self):
        '''
        Returns the perimeter of the given polygon.
        '''
        return self.num_edges * self.edge_length

    def __repr__(self):
        '''
        String representation of the object.
        '''
        return (f'Polygon(n_edges={self.num_edges}, circum_radius={self.circum_radius}, '
                f'interior_angle={self.interior_angle:.2f}, edge_length={self.edge_length:.2f}, '
                f'apothem={self.apothem:.2f}, area={self.area:.2f}, perimeter={self.perimeter:.2f})')


    def __eq__(self, other):
        ''' 
        Checks if two RegularPolygon objects are equal
        '''
        if not isinstance(other, RegularPolygon):
            raise TypeError(f'Argument must be an instance of RegularPolygon, not {type(other).__name__}')

        if isinstance(other, RegularPolygon):
            return (self.num_edges == other.num_edges) and (self.circum_radius == other.circum_radius)
        return NotImplemented

    def __gt__(self, other):
        ''' 
        Checks if the current RegularPolygon object is greater than another RegularPolygon object
        '''
        if not isinstance(other, RegularPolygon):
            raise TypeError(f'Argument must be an instance of RegularPolygon, not {type(other).__name__}')

        if isinstance(other, RegularPolygon):
            return self.num_edges > other.num_edges
        return NotImplemented
