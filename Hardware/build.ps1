CD $PSScriptRoot

& "C:\Program Files\KiCad\bin\python.exe" D:\Kicad\InteractiveHtmlBom\InteractiveHtmlBom\generate_interactive_bom.py --nobrowser .\AquaHub\AquaHub.kicad_pcb
Move-Item -Force .\AquaHub\bom\ibom.html "${PSScriptRoot}\Output\bom\"

& "C:\Program Files\KiCad\bin\python.exe" .\build-gerbers.py .\AquaHub\AquaHub.kicad_pcb "${PSScriptRoot}\Output\gerber"
& "C:\Program Files\KiCad\bin\python.exe" .\build-images.py .\AquaHub\AquaHub.kicad_pcb "${PSScriptRoot}\Output\boards"



# git pull
# git add -A Output
# git commit -m "Auto-generated Outputs"
# git push
