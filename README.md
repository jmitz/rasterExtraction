rasterExtraction
================
Purpose: This is a tool to extract point values from a PRISM raster dataset using Python and various Python related libraries.

Required Libraries:
- os
- osgeo - gdal
- osgeo - osr
- re
- numpy
- fnmatch
- zipfile
- tempfile

This was based on work done by Mike Tercek (miketercek@yahoo.com)
The file structure of the CSV files integrate with extraction and analysis tools developed for the Yellowstone Center for Resources, Yellowstone National Park.

prismExtractor.py
- This script retrieves the PRISM LT71 data from zip files storing the data into a temporary directory. Each PRISM raster for the particular parameter is reprojected and clipped to a raster mask (representing the Greater Yellowstone Ecosystem). The resulting raster is then converted to an array of appropriately scaled values which are written to a file

prismAppend.py
- This script appends the output of prismExtractor.py to the file containing the historic raster data, which is used in the extraction and analysis tools mentioned previously

PRISMDataExtractionMindMap.mm
- This is a mind map of the process and data that were used in this developement. Mind map can be read with [FreeMind](http://freemind.sourceforge.net/wiki/index.php/Main_Page).