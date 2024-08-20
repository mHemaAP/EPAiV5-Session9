from regularpolygon import RegularPolygon

class PolygonSequence:
    def __init__(self, largest_polygon_vertices: int, circum_radius: float) -> None:
        ''' 
        Initializes the class PolygonSequence to calculate area to perimeters ratio 
        of sequence of numbers starting from 3 to "largest_polygon"
        '''
        if not isinstance(largest_polygon_vertices, int):
            raise TypeError('Expected largest_polygon_vertices as type int')

        if not (isinstance(circum_radius, float) or isinstance(circum_radius, int)):
            raise TypeError ('Polygon circum_radius must be either int or float')

        if circum_radius <=0 :
            raise ValueError('Circum Radius must a valid positive number')

        if largest_polygon_vertices < 3:
            raise ValueError('Polygons are defined with at least 3 or more edges')


        self.largest_polygon_vertices = largest_polygon_vertices
        self.circum_radius = circum_radius
        self._polygons = [RegularPolygon(i, circum_radius) for i in range(3, largest_polygon_vertices + 1)]
        self.polygon_data = []
        self.calculate_polygon_sequences()

    def calculate_polygon_sequences(self):
        '''
        Calculates the area to perimeter ratio for all polygons from 3 to largest polygon 
        provided by user
        '''
        for edge_count in range(3, self.largest_polygon_vertices + 1):

            # Create a RegularPolygon instance for each edge count
            polygon = RegularPolygon(edge_count, self.circum_radius)

            # Append to the list of polygon data
            self.polygon_data.append(round((polygon.area/polygon.perimeter), 2))

    def max_efficiency_polygon(self):
        '''
        Returns a tuple containing, 
        max value of area to perimeter ratio and index at which it has occured
        Note: index will be the polygon number at which max area to perimeter ratio has occured rather 
        than index of the array
        '''
        print(max(self.polygon_data), self.polygon_data.index(max(self.polygon_data)))

    def __len__(self) -> int:
        ''' 
        Returns the length of the Calculated Sequences stored in memory
        '''
        return (len(self.polygon_data))

    def __getitem__(self, index: int) -> int:
        '''
        returns the area to perimeter ratio stored at a index 
        '''
        if isinstance(index, int):
            if index < 0:
                index += len(self)  # Adjust negative index
            if index < 0 or index >= len(self):
                raise IndexError("Index out of range.")
            return self.polygon_data[index]
        elif isinstance(index, slice):
            return self.polygon_data[index]
        else:
            raise TypeError("Invalid index type.")

    def __repr__(self) -> str:
        '''
        String representation of the Polygon Sequence object, including details of all polygons in the sequence.
        '''
        polygon_reprs = ', '.join(repr(p) for p in self.polygon_data)
        return (f'PolygonSequence(largest_polygon_vertices={self.largest_polygon_vertices}, '
                f'Polygon with area to perimeter ratio from 3 to {self.largest_polygon_vertices}=[{polygon_reprs}], '
                f'circum_radius={self.circum_radius}')
