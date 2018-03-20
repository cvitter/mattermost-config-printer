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
htmlOut = "<html>\n\t<head>\n\t\t<title>Mattermost Config as of " + dateStringHeader + "</title>"
htmlOut += """
        <style>
            table { font-family: arial, sans-serif; border-collapse: collapse; width: 100%; }
            td, th { border: 1px solid #0066cc; text-align: left; padding: 8px; }
            tr:nth-child(even) { background-color: #cce6ff; }
        </style>
"""
htmlOut += "\t</head>\n\t<body>\n"
htmlOut += "\t\t<table>\n"
htmlOut += "\t\t\t<tr><td colspan=2 bgcolor='#000000'><font color='white'><b>Mattermost Config as of " + dateStringHeader + "</b></font></td></tr>\n"

"""
Iterate over each section in the configuration file, output a section header 
(a table column that spans two columns and has white text)
"""
for section in sections:
    htmlOut += "\t\t\t<tr><td colspan=2 bgcolor='#003366'><font color='white'>" + section + "</font></td></tr>\n"
    
    """
    Create a list of the attribute names and sort
    """
    attributeNames = []
    for key in d[section]:
        attributeNames.append( str(key) )
    attributeNames.sort(key=str.lower)
    
    """
    Iterate over the attributes in the section and out a row in the table for each
    """
    for name in attributeNames:
        htmlOut += "\t\t\t<tr><td>" + name + "</td><td>" + str ( d[section][name] ) + "</td></tr>\n"

    
"""
Complete the HTML output for the documents
"""
htmlOut += "\n\t\t</table>"
htmlOut += "\n\t</body>\n</html>"
print ( "Writing HTML Document to Disk as: " + htmlFileName )

"""
Write our HTML file to disk
"""
fh = open(htmlFileName,"w")
fh.write( htmlOut )
fh.close()

print ( "Done!" )