# getyoutubevideo
Python script that runs in the Mac terminal. It requests a YT URL within the terminal, you paste the video url into the terminal when prompted and it will download the video if it is not blocked by age restrictions.

## Included Files
1. GetYTVideo.command
2. GetYTVideo.py

## Purpose of Files
The .command file is a script made for mac to easily run the script in the terminal (Mac Only)  
The .py file is a script that utilizes the pytube library and

## Changes That Need To Be Made To The Files To Run
First you will need to open the .command file in the text editor of choice.  
Add in the file path to the python scipt.  
_Don't Forget to Update the .py file name in the .command file if you change the name._  
After modifying the .command file, ensure it's saved and that you've made it executable with the **'chmod +x /path/to/your/file.command'** command in the Terminal.

## Other Items
The .py script also checks to make sure that the pip library is up-to-date and if not, it will run the update before requesting for the youtube url.
