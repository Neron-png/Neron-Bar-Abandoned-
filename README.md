# Neron Bar

Neron Bar is an alternative to warp bar that works with Mario Maker 2.

![](https://i.imgur.com/ti25OmG.png)

## Installation

**If you encounter any issues, dm me on twitter @theripstikerpro**

Install [Python 3.6](https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64-webinstall.exe) (no newer, no earlier) And maker sure you  click "Add python 3.6 to PATH" In the installer

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the needed modules.

Type the bellow in the windows shell (cmd)
```bash
pip install Pillow
pip install pytesseract
pip install keyboard
```

Make sure you have OBS Installed.

Download the neron bar.msi from [releases](https://github.com/Ripstikerpro/Neron-Bar/releases) and run it when it's installed.


## Setup

Step 1:

Open up OBS, select your Mario Maker video Input. `Right click` it and select `filters`. Hit the `+`. Then Select `Screenshot Filter`   and hit `ok`.
While in the same screen, look to the right and click browse next to `Destination` , type `%TEMP%` in the top bar and `snapshot.png`     in the bottom one. Like so ![](https://i.imgur.com/L0kjOoR.png)
Then hit save.
Before closing the window, make sure that `interval` (below `Destination`) is set to `1` second or less.


Step 2:

In the main OBS screen add a text source (name it whatever you want) and then hit Tools at the top and then scripts in the dropdown.

In the new window click `Python Settings` on the top, then browse and go to `C:\Users\{your_username}\AppData\Local\Programs\Python\Python36` and change `{your_username}` with your username.

Then, go back to the scripts tab (top left) and hit the `+` at the bottom left, click `neron.py` and then `open`.
After opening it, a few properties should appear on the right. Click on the dropdown next to `text source` and select the text source you created earlier.
  


## Usage

To use this first make sure you've gone through the installation process. Then go to tools (top bar in OBS) and hit scripts, click on neron.py and keep this window open while streaming.

To fetch the data of a level in Mario maker, simply click refresh while viewing the level details. like in this screenshot, 
**With the id shown!** ![](https://i.imgur.com/HqZYPZu.png)

## Contents
Here are the contents of the installer:

Screenshot-Filter obs plugin by synap5e

A custom install of tesseract

neron.py , which is the script that does the processing.




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
