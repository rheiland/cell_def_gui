#
# Test the user_params.py script that was generated.
#
import ipywidgets as widgets
import xml.etree.ElementTree as ET
import os
import glob
import shutil
import datetime
from pathlib import Path
# from user_params import UserTab
# from microenv_params import MicroenvTab
#from cell_def_mockup import CellDefTab
from cells_def import CellsDefTab

constWidth = '180px'
tab_height = '450px'
tab_height = '900px'
tab_layout = widgets.Layout(width='950px',   # border='2px solid black',
                            height=tab_height, overflow_y='scroll',)

# create the tabs, but don't display them yet
# microenv_tab = MicroenvTab()
# user_tab = UserTab()
cells_tab = CellsDefTab()

# read in/parse the .xml file used to generate the GUI widgets.
#main_xml_filename = 'PhysiCell_settings.xml'
main_xml_filename = 'cells.xml'
main_xml_filename = 'config-immune-response.xml'
full_xml_filename = os.path.abspath(main_xml_filename)
print('full_xml_filename=',full_xml_filename)

tree = ET.parse(full_xml_filename)  # this file cannot be overwritten; part of tool distro
xml_root = tree.getroot()

def write_config_file(name):
    # Read in the default xml config file, just to get a valid 'root' to populate a new one
#    full_xml_filename = os.path.abspath('config.xml')
#    full_xml_filename = os.path.abspath(full_xml_filename)
    tree = ET.parse(full_xml_filename)  # this file cannot be overwritten; part of tool distro
    xml_root = tree.getroot()
    # microenv_tab.fill_xml(xml_root)
    # user_tab.fill_xml(xml_root)
    tree.write(name)

# Populate the GUI with the the parameters in the .xml 
def fill_gui_params(config_file):
    tree = ET.parse(config_file)
    xml_root = tree.getroot()
    # user_tab.fill_gui(xml_root)
    # microenv_tab.fill_gui(xml_root)
    cells_tab.fill_gui(xml_root)

#-----------------
# Create a button that will update the .xml file with the parameters in the GUI
def gui2xml_button_cb(s):
    new_config_file = full_xml_filename
    write_config_file(new_config_file)

gui2xml_button = widgets.Button(
    description='GUI -> XML',
    button_style='success',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Write '+main_xml_filename,
)
gui2xml_button.on_click(gui2xml_button_cb)

#-----------------
# Create a button that will update the .xml file with the parameters in the GUI
xml2gui_button = widgets.Button(
    description='XML -> GUI',
    button_style='success',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Write '+main_xml_filename,
)
xml2gui_button.on_click(fill_gui_params)

# Finally, create a simple Jupyter GUI consisting of just the user parameters tab and the Write button.
#titles = ['Microenvironment','User Params']
titles = ['Cell Def']
#tabs = widgets.Tab(children=[microenv_tab.tab, user_tab.tab],
tabs = widgets.Tab(children=[cells_tab.tab],
                   _titles={i: t for i, t in enumerate(titles)},
                   layout=tab_layout)

gui = widgets.VBox(children=[tabs, gui2xml_button, xml2gui_button])
fill_gui_params(full_xml_filename)
