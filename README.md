# Mattermost - Configuration Printer

This GitHub repo contains a simple python script that is desigend to read a Mattermost (https://mattermost.com) config.json file and print it out in a user friendly HTML based format. 

**Note**: This script has been tested on Python 2.7.10 (MacOS), 2.7.12 (Ubuntu 16.04.3 LTS), 3.6.1 (MacOS), and 3.5.2 (Ubuntu 16.04.3 LTS). I cannot promise that it will work with all operating systems and Python version combinations. If you find a bug please report via issues: https://github.com/cvitter/mattermost-config-printer/issues.

To use the script:

1. Create a directory to copy the script to and contain the HTML files it will generate.
2. Download the file to the directory: `wget https://raw.githubusercontent.com/cvitter/mattermost-config-printer/master/config-printer.py`
3. Execute the script passing the path to your config.json file as a command line argument as shown below:

```
python2 config-printer.py /opt/mattermost/config/config.json
```
or

```
python3 config-printer.py /opt/mattermost/config/config.json
```

**Note**: Depending on your user account you may need to use `sudo` to execute the script.

When the script is completed you should see the following output (where the name of the file will reflect the date and time that the script was executed):

```
Attempting to parse: /opt/mattermost/config/config.json
Creating HTML Document
Writing HTML Document to Disk as: mm-config-03152018-182231.html
Done!
``` 

# Make this Project Better (Questions, Feedback, Pull Requests Etc.)

**Help!** If you like this project and want to make it even more awesome please contribute your ideas,
code, etc.

If you have any questions, feedback, suggestions, etc. please submit them via issues here: https://github.com/cvitter/mattermost-jenkins-slash/issues

If you find errors please feel to submit pull requests. Any help in improving this resource is appreciated!

# License
The content in this repository is Open Source material released under the MIT License. Please see the [LICENSE](LICENSE) file for full license details.

# Disclaimer

The code in this repository is not sponsored or supported by Mattermost, Inc.

# Authors
* Author: [Craig Vitter](https://github.com/cvitter)

# Contributors 
Please submit Issues and/or Pull Requests.


