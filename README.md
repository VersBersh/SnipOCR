# SnipOCR
windows snipping tool + OCR reader

An extension of windows snipping tool to select an area of text and read it with OCR. Useful if you need to copy text out of a read-only pdf.

## requirements

tested on windows 10, python >= 3.6

## set up

running setup.ps1 will create a shortcut link in your start menu and assign a hotkey `CTRL+SHIFT+R` to launch the tool

 ```
 $install_path = 'C:/path/to/somewhere'
 mkdir $install_path
 cd $install_path
 git clone git@github.com:VersBersh/SnipOCR.git
 setup.ps1
 ```
