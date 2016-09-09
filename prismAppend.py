#-------------------------------------------------------------------------------
# Name:        prismAppend
# Purpose:     Append prism file to historic prism file
#
# Author:      jmitzelfelt
#
# Created:     09/09/2016
# Copyright:   (c) jmitzelfelt 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main(
        inPrismLog = 'PRISM_GYE_PPT.csv',
        inPrismYearFile = 'GYE_PPT.csv'
    ):
    prismWrite = open(inPrismLog, 'a')
    readFile = open(inPrismYearFile, 'r')
    for line in readFile:
        prismWrite.write(line)

    readFile.close()
    prismWrite.close()

if __name__ == '__main__':
    main()
