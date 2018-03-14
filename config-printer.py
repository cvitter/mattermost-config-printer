import sys
import json
from datetime import datetime

__doc__ = """\
config-printer.py
    Opens the Mattermost config.json file and generates a user friendly, printable
    output to make it easier for business people to understand how a server is configured
    
    By default the script looks for the config.json file in the current directory.
    
    You can pass the full path to the config.json file in the command line to parse a file
    located in another directory, e.g. "python config-printer.py /dir/mattermost/config/config.json"
    
    The script will output an HTML file named: mm-config-ddmmyyyy-hhmmss.html (where ddmmyyyy is
    the current day, month, and year and hhmmss is the current hour, minute, and secondthat the 
    script was run so that a record of changes to the configuration can be kept.
"""

"""
Parse the commandline arguments to get the file to parse
"""
try:
    configFile = sys.argv[1]
except:
    configFile = "config.json"

print ("Attempting to parse: " + configFile)

"""
Load the config.json file as JSON
"""
d = json.load( open( configFile ) )

"""
Create a list of the file sections
"""
sections = []
for section in d:
    sections.append( str(section) )

"""
Sort the list alphabetically so that they are listed in
a consistent order between runs of the script
"""
sections.sort(key=str.lower)

"""
Capture current time and create variables for the display date in the HTML file
and for the HTML file name
"""
dt = datetime.now()
dateStringHeader = dt.strftime('%B %d, %Y %I:%M%p')
htmlFileName = "mm-config-" + dt.strftime('%m%d%Y-%H%M%S') + ".html"

"""
Create document header
"""
print ( "Creating HTML Document" )
htmlOut = "<html>\n<head>\n<title>Mattermost Config as of " + dateStringHeader + "</title>\n</head>\n<body>"



"""

"""
htmlOut += "</body></html>"
print ( "Writing HTML Document to Disk as: " + htmlFileName )

"""
Write our HTML file to disk
"""
# fh = open(htmlFileName,"w")
# fh.write( htmlOut )
# fh.close()

print ( "Done!" )