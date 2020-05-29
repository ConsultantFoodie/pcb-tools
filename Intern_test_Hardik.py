#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2015 Hamilton Kibbe <ham@hamiltonkib.be>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

"""
This example demonstrates the use of pcb-tools with cairo to render a composite
image from a set of gerber files. Each layer is loaded and drawn using a
GerberCairoContext. The color and opacity of each layer can be set individually.
Once all thedesired layers are drawn on the context, the context is written to
a .png file.
"""

import os
from gerber import load_layer, PCB
from gerber.render import RenderSettings, theme
from gerber.render.cairo_backend import GerberCairoContext
from gerber.render.theme import COLORS

GERBER_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'not-working'))

# Create a new drawing context
ctx = GerberCairoContext()

pcb=PCB.from_directory(GERBER_FOLDER)
# Draw the copper layer. render_layer() uses the default color scheme for the
# layer, based on the layer type. Copper layers are rendered as
red_theme = theme.Theme(topmask=RenderSettings(COLORS['red soldermask'], alpha=0.8, invert=True), 
						bottommask=RenderSettings(COLORS['red soldermask'], alpha=0.8, invert=True))

#Rendering layers using the red_theme
ctx.render_layers(layers=pcb.top_layers, filename=os.path.join(os.path.dirname(__file__), 'pcb_top_test.png',), theme=red_theme)
ctx.render_layers(layers=pcb.bottom_layers, filename=os.path.join(os.path.dirname(__file__), 'pcb_bottom_test.png'), theme=red_theme)