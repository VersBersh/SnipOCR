# pip install requirements
iex 'pip install -r requirements.txt'

# create a shortcut in the start menu and assign a key binding
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:ProgramData\Microsoft\Windows\Start Menu\Programs\snipping_ocr.lnk")
$Shortcut.TargetPath = "$PSScriptRoot\snipping.pyw"
$Shortcut.Hotkey = "CTRL+SHIFT+R"
$Shortcut.Save()