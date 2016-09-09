<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1472745117424" ID="ID_1727416691" MODIFIED="1473431741496" TEXT="PRISM Data Extraction">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      new_raster_extract folder
    </p>
    <p>
      
    </p>
    <p>
      Documentation
    </p>
    <p>
      http://prism.oregonstate.edu/documents/PRISM_datasets_aug2013.pdf
    </p>
  </body>
</html>
</richcontent>
<node CREATED="1472745140356" ID="ID_1246395457" MODIFIED="1472745146179" POSITION="right" TEXT="Required Software">
<node CREATED="1472745147814" ID="ID_952382121" MODIFIED="1472745156739" TEXT="Python">
<node CREATED="1472745158252" ID="ID_944817703" MODIFIED="1472745187336" TEXT="Packages">
<node CREATED="1472745188733" ID="ID_1657039494" MODIFIED="1472745193545" TEXT="numpy"/>
<node CREATED="1472745194007" ID="ID_879130204" MODIFIED="1472745198139" TEXT="gdal"/>
</node>
</node>
</node>
<node CREATED="1472746884257" ID="ID_730313998" MODIFIED="1472746889412" POSITION="right" TEXT="Data">
<node CREATED="1472746891042" ID="ID_408401674" MODIFIED="1472749853746" TEXT="raster_mask">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Should be in the same folder as the once_year_extractor.py
    </p>
    <p>
      
    </p>
    <p>
      Projection GSC_NAD_1983_NSRS2007 (wkid: 4759)
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1472748165123" ID="ID_1989269542" MODIFIED="1472749918215" TEXT="tmax_189501">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      H:\NEW_NAD83_NSRS2007_PRISM_data\tmax\tmax\tmax_189501
    </p>
    <p>
      
    </p>
    <p>
      Projection NAD83_NSRS2007 (wkid: 4759)
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1473365840233" ID="ID_65788229" MODIFIED="1473365863590" TEXT="PRISM Datasets">
<node CREATED="1473435408968" ID="ID_1618845392" MODIFIED="1473435454564" TEXT="LT71 Data">
<node CREATED="1473365864742" ID="ID_1703166921" MODIFIED="1473435421892" TEXT="PPT">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Units should be reported in mm * 100. The default units appear to be in mm so I am going to multiply each cell by 100 and limit the precision to 1/10s
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1473365868293" ID="ID_751115672" MODIFIED="1473435421906" TEXT="TMAX">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Units should be reported in Deg C * 100. The default units appear to be in mm so I am going to multiply each cell by 100 and limit the precision to 1/10s
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1473365872021" ID="ID_1016315569" MODIFIED="1473435421918" TEXT="TMIN">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Units should be reported in Deg C * 100. The default units appear to be in mm so I am going to multiply each cell by 100 and limit the precision to 1/10s
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1473435484310" ID="ID_447068250" MODIFIED="1473437560945" TEXT="LT81 Data">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Data are not zipped and are in individual folders
    </p>
  </body>
</html>
</richcontent>
<node CREATED="1473437560931" ID="ID_1234122615" MODIFIED="1473437564047" TEXT="PPT"/>
<node CREATED="1473437564803" ID="ID_1564927642" MODIFIED="1473437568544" TEXT="TMAX"/>
<node CREATED="1473437569108" ID="ID_1775773747" MODIFIED="1473437572512" TEXT="TMEAN"/>
<node CREATED="1473437572771" ID="ID_1243559605" MODIFIED="1473437575743" TEXT="TMIN"/>
</node>
</node>
</node>
<node CREATED="1472748943196" ID="ID_883475689" MODIFIED="1472748947393" POSITION="left" TEXT="Process">
<node CREATED="1472751908764" ID="ID_1309271507" MODIFIED="1472751929431" TEXT="Unzip new PRISM data file"/>
<node CREATED="1472748951785" ID="ID_1852579400" MODIFIED="1473353953273" TEXT="Reproject/Resample New PRISM Data">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      PRISM data are projected in GCS_North_American_1983 (wkid: 4269) and the data we are matching to are in GSC_NAD_1983_NSRS2007 (wkid:&#160;4759)
    </p>
    <p>
      
    </p>
    <p>
      Reprojection Process http://stackoverflow.com/questions/10454316/how-to-project-and-resample-a-grid-to-match-another-grid-with-gdal-python
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1472749201558" ID="ID_1157997194" MODIFIED="1472749332960" TEXT="Run the Extraction Process">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      This process extracts the PRISM data from the GSC_NAD_1983_NSRS2007 projected PRISM data and generates a CSV file of the extracted information.
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1472750283881" ID="ID_918270722" MODIFIED="1472751961479" TEXT="Append data to historic data"/>
</node>
</node>
</map>
