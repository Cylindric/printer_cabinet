@ECHO OFF
"C:\Program Files\KiCad\bin\python.exe" D:\Kicad\InteractiveHtmlBom\InteractiveHtmlBom\generate_interactive_bom.py --nobrowser .\AquaHub\AquaHub.kicad_pcb
MOVE AquaHub\bom\ibom.html Output\bom
ERASE /Q /S AquaHub\bom

python "D:\Kicad\KiBoM/KiBOM_CLI.py" ".\AquaHub\AquaHub.xml" ".\Output\Bom\AquaHub"
