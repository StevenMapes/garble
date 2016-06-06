import gzip
import sys

import unidecode

from src.minify_slimit import garble_js

if len(sys.argv) < 3:
    print("please specify an input and output and if you would like to use compression.")
    quit()

inputPath = sys.argv[1]
outputPath = sys.argv[2]
compress = sys.argv[3]

# Fetch JS to garble
fileContents = open(inputPath, 'r').read()
fileContentsUnicoded = unicode(fileContents,'utf-8')
fileContentsUnunicoded = unidecode.unidecode(fileContentsUnicoded)

# Garble
js = garble_js(fileContentsUnunicoded)

# Write to file
outputFile = open(outputPath, 'w+')
outputFile.write(js)
outputFile.close()

# Handle Compression
if compress.lower() == "yes":
    f_in = open(outputPath, 'rb')
    f_out = gzip.open(outputPath+".gz", 'wb')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()
