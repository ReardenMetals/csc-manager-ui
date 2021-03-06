# Introduction to Cold Storage Coins Manager

This is Python desktop offline application for generating & validating Cold Storage Coins of different currencies: BTC, BCH, LTC, ETH, DOGE.

Also added implementation of AWS Lambda keygen.

# CSC Manager Installation

This application is working with Python 3.8.6 (pip 20.2.1)

Python-3.8.6 download link: https://www.python.org/downloads/release/python-386/

Install Keygen-Core: https://github.com/ReardenMetals/keygen-core

Install Keygen-Plugins: https://github.com/ReardenMetals/keygen-plugins

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
- keygen-plugins
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

    pip install -r requirements.txt
    
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

# Installing for PyCharm

Check actual dependencies

    pip freeze | grep 'pynput'

Install dependencies

    pip install -r ./csc-manager-ui/requirements.txt