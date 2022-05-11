from mesa.visualization.modules import CanvasGrid, ChartModule, PieChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from .model import ForestFire

COLORS = {"Fine": "#00AA00", "On Fire": "#880000", "Burned Out": "#000000", "Safe Area": "#4FFF"}

def forest_fire_portrayal(tree):
    if (tree is None) or (tree.condition == "AirFighter"):
        return
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
    (x, y) = tree.pos
    portrayal["x"] = x
    portrayal["y"] = y
    portrayal["Color"] = COLORS[tree.condition]
    return portrayal


canvas_element = CanvasGrid(forest_fire_portrayal, 100, 100, 500, 500)
tree_chart = ChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)
cluster_chart = ChartModule(
    [{"Label": "Clusters", "Color": "#5FA"}]
)
pie_chart = PieChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)

model_params = {
    "tree_density": UserSettableParameter("slider", "Tree density", 0.65, 0.01, 1.0, 0.01),
    "forest_size": UserSettableParameter("slider", "Forest Size", 100, 10, 100, 10),
    "firemans": UserSettableParameter("slider", "Firemans percentage", 0.20, 0.01, 0.30, 0.01),
}
server = ModularServer(
    ForestFire, [canvas_element, tree_chart, cluster_chart, pie_chart], "Forest Fire", model_params
)
