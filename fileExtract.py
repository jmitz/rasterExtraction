#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jmitzelfelt
#
# Created:     08/09/2016
# Copyright:   (c) jmitzelfelt 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from osgeo import gdal
from osgeo import gdalconst
from osgeo import osr

def projectFile(inDataLayer, inDataEpsg, inMaskLayer, inMaskEpsg, inOutLayer, inDriverType):
    dataLayer = gdal.Open(inDataLayer, gdalconst.GA_ReadOnly)
    dataProj = osr.SpatialReference()
    dataProj.ImportFromEPSG(inDataEpsg)
    dataGeoTrans = dataLayer.GetGeoTransform()
    maskLayer = gdal.Open(inMaskLayer, gdalconst.GA_ReadOnly)
    maskProj = osr.SpatialReference()
    maskProj.ImportFromEPSG(inMaskEpsg)
    maskGeoTrans = maskLayer.GetGeoTransform()
    xSize = maskLayer.RasterXSize
    ySize = maskLayer.RasterYSize
    destLayer = gdal.GetDriverByName(inDriverType).Create(inOutLayer, xSize, ySize, 1, gdalconst.GDT_Float32)
    destLayer.SetGeoTransform(maskGeoTrans)
    destLayer.SetProjection(maskProj.ExportToWkt())
    gdal.ReprojectImage(dataLayer, destLayer, dataProj.ExportToWkt(), maskProj.ExportToWkt(), gdalconst.GRA_NearestNeighbour)
    return destLayer

if __name__ == '__main__':
    projectedFile = projectFile(r'H:\2015_Updates\LT71_ppt_2015\cai_ppt_us_us_30s_201501.bil', 4269, r'H:\rasterExtraction\raster_mask', 4759, r'H:\test.tif', 'GTiff')
    del projectedFile
