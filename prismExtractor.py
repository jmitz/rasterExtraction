import numpy as np
from osgeo import gdal
from osgeo import gdalconst
from osgeo import osr
import os
import re
import fnmatch
import zipfile
import tempfile


def fileRetrieve(inDir, inFilters):
    returnFileInfos = []
    includes = r'|'.join([fnmatch.translate('*.' + x.upper()) for x in inFilters])
    for root, dirs, files in os.walk(inDir):
        files = [(root, f) for f in files]
        files = [f for f in files if re.match(includes, f[1].upper())]
        returnFileInfos.extend(files)
    return returnFileInfos

def filterFileInfoList(inFileInfos, inFilters):
    includes = r'|'.join([fnmatch.translate('*' + x.upper() + '*') for x in inFilters])
    returnFileInfos = [f for f in inFileInfos if re.match(includes, f[1].upper())]
    return returnFileInfos

# Adapted from http://stackoverflow.com/questions/10454316/how-to-project-and-resample-a-grid-to-match-another-grid-with-gdal-python
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

def getZipFileContents(inFileInfo, inTempDirName):
    fullFilePath = '/'.join(inFileInfo)
    zipFile = zipfile.ZipFile(fullFilePath)
    zipFile.extractall(inTempDirName)
    return fileRetrieve(inTempDirName, ['bil'])

def setupTempFolder():
    return tempfile.mkdtemp()

def cleanTempFolder(inTempDirName):
    fileList = os.listdir(inTempDirName)
    for file in fileList:
        os.remove(inTempDirName + '/' + file)

def removeTempFolder(inTempDirName):
    cleanTempFolder(inTempDirName)
    os.removedirs(inTempDirName)

def fileNameSplitter(inFileInfo):
    fileSplit = inFileInfo[1].split('.')
    return fileSplit[0].split('_')

def main(
    fileTypeList = ['ppt', 'tmax', 'tmin'],
    rasterMask = 'H:/rasterExtraction/raster_mask',
    workingDir = 'H:/rasterExtraction',
    prismFiles = 'H:/2015_updates'
    ):

    zipFileInfos = filterFileInfoList(fileRetrieve(prismFiles, ['zip']), fileTypeList)
    tempDir = setupTempFolder()
    for zipFile in zipFileInfos:
        getZipFileContents(zipFile, tempDir)
        dataFileInfos = fileRetrieve(tempDir, ['bil'])
        dataFileSplit = fileNameSplitter(zipFile)
        outputFileName = "{0}/GYE_{1}.csv".format(workingDir, dataFileSplit[1].upper())
        outputFile = open(outputFileName, 'w')
        for dataFile in dataFileInfos:
            projectedLayer = projectFile('/'.join(dataFile), 4269, rasterMask, 4759, '', 'MEM')
            outputArray = projectedLayer.GetRasterBand(1).ReadAsArray().ravel().tolist()
            roundedArray = np.round(np.multiply(outputArray, 100), 1)
            splitFileName = fileNameSplitter(dataFile)
            recordName = '{0[1]}_{0[5]}'.format(splitFileName)
            print recordName
            outputFile.write(recordName + ',')
            roundedArray.tofile(outputFile, sep=',')
            outputFile.write('\n')
        outputFile.close()
        cleanTempFolder(tempDir)
    removeTempFolder(tempDir)

main()
