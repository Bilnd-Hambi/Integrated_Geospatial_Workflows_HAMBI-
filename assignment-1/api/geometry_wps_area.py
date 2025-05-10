# ---------------------
# Area Calculation function using WPS-like structure
# ---------------------
from osgeo import ogr, osr

def title():
    return "Geometry Area"

def abstract():
    return "Calculates the area of a geometry in square meters."

def inputs():
    return [
        ['feature', 'Input feature','The geometry whose area will be calculated.','application/json', True],
        ['srid', 'SRID', 'The spatial reference ID of the input geometry.', 'integer', True]
    ]

def outputs():
    return [['area', 'Calculated area','Area of the geometry in square meters.','application/json']]

def execute(parameters):
    feature = parameters.get('feature')
    srid = parameters.get('srid')
    
    if (feature is not None) and (srid is not None):
        feature = feature['value']
        srid = int(srid['value'])

    # Load geometry
    geom = ogr.CreateGeometryFromJson(feature)

    # Create spatial reference
    source = osr.SpatialReference()
    source.ImportFromEPSG(srid)

    # Project to EPSG:3857 for area in meters if not already
    if srid != 28992:
        target = osr.SpatialReference()
        target.ImportFromEPSG(28992)
        transform = osr.CoordinateTransformation(source, target)
        geom.Transform(transform)

    area = geom.GetArea()

    print("Content-type: application/json")
    print()
    print(f'{{"area": {area}}}')
