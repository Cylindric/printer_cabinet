import sys, os, shutil

sys.path.insert(0, "C:\Program Files\KiCad\lib\python2.7\site-packages")
import pcbnew
from pcbnew import *

# Load board and initialize plot controller
boardName = sys.argv[1]
filePath = sys.argv[2]
board = LoadBoard(boardName)
pctl = pcbnew.PLOT_CONTROLLER(board)
popt = pctl.GetPlotOptions()
plotDir = filePath


popt.SetOutputDirectory(plotDir)
popt.SetPlotFrameRef(False)
popt.SetLineWidth(pcbnew.FromMM(0.15))
popt.SetAutoScale(False)
popt.SetScale(1)
popt.SetMirror(False)
popt.SetUseGerberAttributes(False)
popt.SetExcludeEdgeLayer(False)
popt.SetUseAuxOrigin(False)
pctl.SetColorMode(True)


layers = [
    ("F_Cu", pcbnew.F_Cu, "Top layer"),
    ("B_Cu", pcbnew.B_Cu, "Bottom layer"),
    ("F_SilkS", pcbnew.F_SilkS, "Silk top"),
    ("B_SilkS", pcbnew.B_SilkS, "Silk top"),
    ("B_Mask", pcbnew.B_Mask, "Mask bottom"),
    ("F_Mask", pcbnew.F_Mask, "Mask top"),
    ("Edge_Cuts", pcbnew.Edge_Cuts, "Edges"),
#    ("B_Paste", pcbnew.B_Paste, "Paste bottom"),
#    ("F_Paste", pcbnew.F_Paste, "Paste top"),
#    ("Margin", pcbnew.Margin, "Margin"),
#    ("In1_Cu", pcbnew.In1_Cu, "Inner1"),
#    ("In2_Cu", pcbnew.In2_Cu, "Inner2"),
#    ("Dwgs_User", pcbnew.Dwgs_User, "Dwgs_User"),
#    ("Cmts_User", pcbnew.Cmts_User, "Comments_User"),
#    ("Eco1_User", pcbnew.Eco1_User, "ECO1"),
#    ("Eco2_User", pcbnew.Eco2_User, "ECO2"),
#    ("B_Fab", pcbnew.B_Fab, "Fab bottom"),
#    ("F_Fab", pcbnew.F_Fab, "Fab top"),
#    ("B_Adhes", pcbnew.B_Adhes, "Adhesive bottom"),
#    ("F_Adhes", pcbnew.F_Adhes, "Adhesive top"),
#    ("B_CrtYd", pcbnew.B_CrtYd, "Courtyard bottom"),
#    ("F_CrtYd", pcbnew.F_CrtYd, "Courtyard top"),
]

# Purge existing files

for the_file in os.listdir(plotDir):
    file_path = os.path.join(plotDir, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)


# Export new files
for layer_info in layers:
    pctl.SetLayer(layer_info[1])
    pctl.OpenPlotfile(layer_info[0], pcbnew.PLOT_FORMAT_GERBER, layer_info[2])
    pctl.PlotLayer()

pctl.ClosePlot()
