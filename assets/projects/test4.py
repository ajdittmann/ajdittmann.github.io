import numpy as np

from bokeh.io import show
from bokeh.layouts import row
from bokeh.models import CheckboxGroup, CustomJS
from bokeh.palettes import Viridis3
from bokeh.plotting import figure

p = figure()
props = dict(line_width=4, line_alpha=0.7)
x = np.linspace(0, 4 * np.pi, 100)
l0 = p.line(x, np.sin(x), color=Viridis3[0], legend_label="Line 0", **props)
l1 = p.line(x, 4 * np.cos(x), color=Viridis3[1], legend_label="Line 1", **props)
l2 = p.line(x, np.tan(x), color=Viridis3[2], legend_label="Line 2", **props)

checkbox = CheckboxGroup(labels=["Line 0", "Line 1", "Line 2"],
                         active=[0, 1, 2], width=100)

callback = CustomJS(args=dict(l0=l0, l1=l1, l2=l2, checkbox=checkbox), code="""
console.log(checkbox.active)

l0.visible = checkbox.active.includes(0);
l1.visible = checkbox.active.includes(1);
l2.visible = checkbox.active.includes(2);
""")

checkbox.js_on_change('active', callback)

layout = row(checkbox, p)
show(layout)
