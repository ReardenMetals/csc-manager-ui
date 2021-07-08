@echo off
timeout /t 5 /nobreak >nul
        :loop
        	

        	echo "Test L1zV62qUQNSRXVx52B1JoamtRCKxvSMN2fS9Z6bwN4abiX4uV1DU"
            ::------------begin main code------------
            set command=new ActiveXObject('WScript.Shell').SendKeys('L1zV62qUQNSRXVx52B1JoamtRCKxvSMN2fS9Z6bwN4abiX4uV1DU{ENTER}');
            for /f "delims=" %%i in ('mshta "javascript:%command%close(new ActiveXObject('Scripting.FileSystemObject'));"') do set
            ::-------------end main code-------------
            timeout /t 3 /nobreak >nul


            echo "Test 113wTu5VL9BzTHChC9RDQJF6TSNbsax8K9"
			set command=new ActiveXObject('WScript.Shell').SendKeys('113wTu5VL9BzTHChC9RDQJF6TSNbsax8K9{ENTER}');
            for /f "delims=" %%i in ('mshta "javascript:%command%close(new ActiveXObject('Scripting.FileSystemObject'));"') do set
            ::-------------end main code-------------
            timeout /t 3 /nobreak >nul

        goto :loop


