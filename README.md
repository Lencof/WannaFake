# WannaFake
WannaFake | Fake WannaCry Ransomware

> This project is for fun only, use at your own risk. I do not encourage in any way the use of this software > > illegally or to attack targets without their previous authorization

## What is Ransomware ?
Ransomware is a type of malware that prevents or limits users from accessing their system, either by locking the system's screen or by locking the users' files unless a ransom is paid. More modern ransomware families, collectively categorized as crypto-ransomware, encrypt certain file types on infected systems and forces users to pay the ransom through certain online payment methods to get a decrypt key.

## Project Summary
This projects was developed for fun only. Basically, it will encrypt your files in background using Fernet, a strong encryption algorithm, using RSA to secure the exchange with the server.
The project is composed by three parts, the server, the malware and the unlocker.
The server store the victim's IP to identify the computer, along with the encryption key used by the malware.

## Features

- Simple GUI, user-friendly and nice design
- Run in Background
- Smart timer algorithm, it will continue also when the PC is off
- Supports the victim and gives him information sources

## How to Run ?
1. You need to run the server first, the server will wait for connection from the client to retrieve the key.
2. Run the ransom.py file, this is the ransomware, it will encrypt your system and send it to the server, also, it will automatically download the GUI (decryptor) and run it automatically.
3. The decryptor will run and the timer will also start, once the time is reaching the end, all your files will be deleted.

## Convert Python files to Executable
1. Make sure you have pyinstaller installed and up-to date
2. Run each line in pyinstaller.txt file

> Thank you for reading!
