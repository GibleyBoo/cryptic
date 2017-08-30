import urllib
import shutil
import re
import sys

def downloadPage (targetUrl, targetFile):
	urllib.urlretrieve("http://www." + targetUrl, targetFile)
	fileLocation = "files/" + targetFile
	shutil.move(targetFile, fileLocation)
	print("Downloaded: " + str(targetFile) + " to: " + str(fileLocation))
	return
if (len(sys.argv) > 3):
	downloadPage(sys.argv[1], sys.argv[2])
else:
	print("Page or file hasnt been declared")
