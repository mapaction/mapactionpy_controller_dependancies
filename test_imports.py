import unittest

class TestImports(unittest.TestCase):
    def setUp(self):
        pass

    def test_imports(self):
        # Test PyProj
        import pyproj

        # Test Shapely
        from shapely.geometry import box

        # Test GDAL
        from osgeo import gdal
        from osgeo import ogr
        from osgeo import osr
        from osgeo import gdal_array
        from osgeo import gdalconst

        # Test Fiona
        import fiona

        # Test RTree
        from rtree import index

        # Test geopandas
        import geopandas

        print('imported everything without error')
        # If we've got this far without an error then that's a pass
        self.assertTrue(True, msg='imported everything without error')


if __name__ == "__main__":
    unittest.main()
