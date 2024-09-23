# Startup django server in background
To run the startup command prompt in the background without displaying the console window, you can use the following method:


## Steps:
### 1. Create a Batch File(save the file with .bat extension) and copy given code:

@echo off
cd C:\path\to\your\django\project
call venv\Scripts\activate
python manage.py runserver

### 2. Create a VBScript to Run the Batch File Hidden:
!!! The given lines of code is giving error

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c C:\path\to\start_django_server.bat", 0, False

Replace C:\path\to\start_django_server.bat with the full path to your .bat file.
The 0 ensures that the window is hidden, and False ensures the script doesn't wait for the batch file to finish before continuing.
Save this file with a .vbs extension, e.g., start_django_server.vbs.

### 3. Add the VBScript to Startup:
Press Win + R, type shell:startup, and press Enter to open the Startup folder.
Copy your .vbs file into this folder.
Now, on system startup, the Django server will start without showing the command prompt window.