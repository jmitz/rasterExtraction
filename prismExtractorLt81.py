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

def sortPrismLt81Files(inVal):
    fileNameArray = fileNameSplitter(inVal)
    if len(fileNameArray[4]) == 4:
        fileNameArray[4] += '14'
    return fileNameArray[4]

def main(
    fileTypeList = ['ppt', 'tmax', 'tmin'],
    rasterMask = 'K:/Climate_Data_PRISM_800m/rasterExtraction/raster_mask',
    workingDir = 'K:/Climate_Data_PRISM_800m/rasterExtraction',
    prismFiles = 'E:/PRISM_data/LT81',
    addHeader = true
    ):
    maskData = gdal.Open(rasterMask)
    maskArray = maskData.GetRasterBand(1).ReadAsArray().ravel()
    del maskData
    for fileType in fileTypeList:
        dataDir = "{0}/{1}".format(prismFiles, fileType)
        rawDataFileInfos = fileRetrieve(dataDir, ['bil'])
        dataFileInfos = sorted(rawDataFileInfos, key=sortPrismLt81Files)
        outputFileName = "{0}/GYE_{1}.csv".format(workingDir, fileType.upper())
        outputFile = open(outputFileName, 'w')
        if addHeader:
            outputFile.write('point number -> ,')
            maskArray.tofile(outputFile, sep=',')
            outputFile.write('\n')
        for dataFile in dataFileInfos:
            projectedLayer = projectFile('/'.join(dataFile), 4269, rasterMask, 4759, '', 'MEM')
            outputArray = projectedLayer.GetRasterBand(1).ReadAsArray().ravel().tolist()
            roundedArray = np.round(np.multiply(outputArray, 100), 1)
            splitFileName = fileNameSplitter(dataFile)
            recordName = '{0[1]}_{0[4]}'.format(splitFileName)
            print recordName
            # Adding 14 to the end of recordName if the length is less than the length of fileType + 7.
            # This is to allow the data file to match the LT71 filename.
            # This should be removed when the programs that use these data are modified.
            if (len(recordName) < (len(fileType) + 7)):
                recordName = recordName + '14'
            outputFile.write(recordName + ',')
            roundedArray.tofile(outputFile, sep=',')
            outputFile.write('\n')
        outputFile.close()

main()
