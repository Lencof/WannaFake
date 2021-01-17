# WannaFake :heavy_dollar_sign:
WannaFake | Fake WannaCry Ransomware

> This project is for fun only, use at your own risk. I do not encourage in any way the use of this software > > illegally or to attack targets without their previous authorization

## Project Summary
This projects was developed for fun only. Basically, it will encrypt your files in background using Fernet, a strong encryption algorithm, using RSA to secure the exchange with the server.
The project is composed by three parts, the server, the malware and the unlocker.
The server store the victim's IP to identify the computer, along with the encryption key used by the malware.

## Features

- GUI that looks similar to WannaCry
- Timer algorithm, continue also when the PC is off
- The victim has only 7 days to send the money

## Setup
In _ransom.py_ make sure to change `YOUR WALLPAPER BACKGROUND` to an image (link from a web server) you want to use as a wallpaper
and also change `IP` to your server IP in which you want the victim data to be sent to.

Another thing we need to mention is about the GUI program. You have two options, one is to edit the `setup_files` function in `ransom.py` so the function will download the GUI file into the victim's Desktop. Or, if you use this program for testing, you can do that by your own (place the GUI file into your victim's Desktop) so the victim can open the GUI and follow the instructions.

You can also convert the Python files to executable files (look at pyinstaller.txt)
###### Running the Program
After you have completed the setup, you need to run the `server.py` which will wait for incoming connections (the victims). And then run the `ransom.py` on the victim machine.
