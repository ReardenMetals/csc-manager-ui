# Introduction to Cold Storage Coins Manager

This is Python desktop offline application for generating & validating Cold Storage Coins of different currencies: BTC, BCH, LTC, ETH, DOGE.

Also added implementation of AWS Lambda keygen.

# CSC Manager Installation

This application is working with Python 3.8.6 (pip 20.2.1)

Python-3.8.6 download link: https://www.python.org/downloads/release/python-386/

Install Keygen-Core: https://github.com/ReardenMetals/keygen-core

## Windows install
    
### Install needed dependencies:

Create csc-manager folder. All installations do in this folder:

Install Visual C++ Redistributable Packages for Visual Studio 2013 (vcredist_x64.exe):
https://www.microsoft.com/en-us/download/details.aspx?id=40784
Or download vcredist_x64.exe file from https://github.com/ReardenMetals/csc-manager-ui/releases/

Download archive with the latest release of "Source Code (zip)" for Windows based system
https://github.com/ReardenMetals/csc-manager-ui/releases/

Select needed release and download & unarchive "ui-dependencies-win.zip" 
    
Download archive with the latest release of "Source Code (zip)" for Windows based system or "Source Code (tar.gz)" for Unix based system
https://github.com/ReardenMetals/csc-manager-ui/releases/

Finally, csc-manager folder should contains three sub-folders: 

- keygen-core
- ui-dependencies-win
- csc-manager-ui

Change application config ("config.json" in root folder) to your file pathes:

    {
      "base_file_name": "C:\\Users\\laser\\Desktop\\keypair.txt",
      "asset_id_file_name": "C:\\Users\\laser\\Desktop\\snip.txt",
      "private_file_name": "C:\\Users\\laser\\Desktop\\key.txt",
      "public_file_name": "C:\\Users\\laser\\Desktop\\labels.txt",
      "sequence_file_name": "C:\\Users\\laser\\Desktop\\numbers.txt"
    }
    
Run CSC Manager desktop application:

    ./csc-manager.bat
    
Run CLI Keygen:

    ./keygen.bat
    
Run CLI Update:

    ./update.bat
    
## Linux Install

Install needed dependencies:

    pip install asynctkinter==0.1.1
    pip install pygame==2.0.1
    pip install Pillow==8.1.0
    pip install opencv-python==4.5.1.48
    pip install pyzbar==0.1.8
    pip install imutils==0.5.4
    
Change application config ("config.json" in root folder) to your file pathes:
    
    {
      "base_file_name": "./output/keypair.txt",
      "asset_id_file_name": "./output/snip.txt",
      "private_file_name": "./output/key.txt",
      "public_file_name": "./output/labels.txt",
      "sequence_file_name": "./output/numbers.txt"
    }
    
Run CSC Manager desktop application:

    python csc-manager.py
    
Run CLI Keygen:

    python keygen.py
    
Run CLI Update:

    python update.py

# AWS Lambda keygen installation
    
Install needed dependencies:
    
    pip install --target ~/lambda-package bip_utils==1.7.0 bitsv==0.11.5 cashaddress==1.0.6 aioeos==1.0.2 \
        pywallet==0.1.0 monero==0.8 PyWaves==0.8.15 base58==2.0.0
        
Preparing package for AWS Lambda:

    cp -r ~/csc-manager/keygen ~/lambda-package/
    zip -r9 ~/lambda.zip .
    zip -g ~/lambda.zip ~/csc-manager/aws_lambda.py
    
Upload zip archive to AWS Lambda.
