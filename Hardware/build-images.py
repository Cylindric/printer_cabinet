import sys, os, shutil

sys.path.insert(0, "C:\Program Files\KiCad\lib\python2.7\site-packages")
import pcbnew
from pcbnew import *

# Colours
FCU = COLOR4D(132, 0, 0, 0)
BCU = COLOR4D(0, 132, 0, 0)
FSILK = COLOR4D(0, 132, 132, 0)

    

# Load board and initialize plot controller
boardName = sys.argv[1]
filePath = sys.argv[2]
board = LoadBoard(boardName)
plotDir = filePath




overview_layers = [
    ("B_Paste", pcbnew.B_Paste, "Paste bottom"),
    ("F_Paste", pcbnew.F_Paste, "Paste top"),
    ("F_SilkS", pcbnew.F_SilkS, "Silk top"),
    ("B_SilkS", pcbnew.B_SilkS, "Silk bottom"),
    ("B_Mask", pcbnew.B_Mask, "Mask bottom"),
    ("F_Mask", pcbnew.F_Mask, "Mask top"),
    ("Edge_Cuts", pcbnew.Edge_Cuts, "Edges"),
    ("Cmts_User", pcbnew.Cmts_User, "Comments_User"),
]


# Purge existing files
for the_file in os.listdir(plotDir):
    file_path = os.path.join(plotDir, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)


def render(layers, name, mirror):
    # Export new files
    pctl = pcbnew.PLOT_CONTROLLER(board)
    popt = pctl.GetPlotOptions()

    popt.SetOutputDirectory(plotDir)
    popt.SetPlotFrameRef(False)
    popt.SetLineWidth(pcbnew.FromMM(0.15))
    popt.SetAutoScale(False)
    popt.SetScale(1)
    popt.SetMirror(mirror)
    popt.SetUseGerberAttributes(True)
    popt.SetExcludeEdgeLayer(False)
    popt.SetUseAuxOrigin(False)
    popt.SetUseAuxOrigin(False)
    popt.SetPlotReference(True)
    popt.SetPlotValue(True)
    popt.SetPlotInvisibleText(False)
    popt.SetPlotFrameRef(False)

    pctl.SetLayer(Dwgs_User)
    pctl.OpenPlotfile(name, PLOT_FORMAT_PDF, name)
    pctl.SetColorMode(True)

    for layer_info in layers:
        pctl.SetLayer(layer_info[1])
        pctl.PlotLayer()

    pctl.ClosePlot()


top_layers = [
    ("F_Cu", pcbnew.F_Cu, "Copper top"),
    ("F_Paste", pcbnew.F_Paste, "Paste top"),
    ("F_SilkS", pcbnew.F_SilkS, "Silk top"),
    ("F_Mask", pcbnew.F_Mask, "Mask top"),
    ("F_Mask", pcbnew.F_Mask, "Mask top"),
    ("Edge_Cuts", pcbnew.Edge_Cuts, "Edges"),
]

bottom_layers = [
    ("B_Cu", pcbnew.B_Cu, "Copper bottom"),
    ("B_Paste", pcbnew.B_Paste, "Paste bottom"),
    ("B_SilkS", pcbnew.B_SilkS, "Silk bottom"),
    ("B_Mask", pcbnew.B_Mask, "Mask bottom"),
    ("B_Mask", pcbnew.B_Mask, "Mask bottom"),
    ("Edge_Cuts", pcbnew.Edge_Cuts, "Edges"),
]

placetop_layers = [
    ("F_SilkS", pcbnew.F_SilkS, "Silk top"),
    ("F_Mask", pcbnew.F_Mask, "Mask top"),
    ("Edge_Cuts", pcbnew.Edge_Cuts, "Edges"),
]

placebottom_layers = [
    ("B_SilkS", pcbnew.B_SilkS, "Silk bottom"),
    ("B_Mask", pcbnew.B_Mask, "Mask bottom"),
    ("Edge_Cuts", pcbnew.Edge_Cuts, "Edges"),
]

render(top_layers, "top", False)
render(bottom_layers, "bottom", True)
render(placetop_layers, "placement-top", False)
render(placebottom_layers, "placement-bottom", True)
