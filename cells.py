"""
====================================================================================================
  Parse a PhysiCell configuration file (XML) and generate a Jupyter (Python) modules: 
    cell_def.py - containing widgets for cell parameters.
  
====================================================================================================
 
  Inputs - takes none, 1, 2, 3, or 4 arguments
  ------
    config filename (str, optional): the PhysiCell configuration file (.xml) (Default = config.xml)
    GUI module (str, optional):      the primary GUI for the Jupyter notebook 
    colorname1, colorname2 (str, optional): the colors to use for the alternating rows of widgets 
                                            (Defaults: lightgreen, tan)
  Examples (with 0,1,2,3,4 args):
  --------
    python cells.py
    python cells.py cells.xml
  
  Outputs
  -------
    cell_def.py: Python module used to create/edit cell parameters (--> "Cells" GUI tab)
 
Authors:
Randy Heiland (heiland@iu.edu)
Dr. Paul Macklin (macklinp@iu.edu)

--- History ---
"""

import sys
import os
import math
import xml.etree.ElementTree as ET

# Defaults
config_file = "config.xml"
colorname1 = 'lightgreen'
colorname2 = 'tan'

num_args = len(sys.argv)
print("num_args=",num_args)
if (num_args < 2):
    print()
    print("*** NOTE:  using config.xml  ***")
    print()
else:
    config_file = sys.argv[1]
    if not os.path.isfile(config_file):
        print(config_file, "does not exist")
        print("Usage: python " + sys.argv[0] + " <config-file.xml> [<gui-file.py>] [<colorname1> <colorname2>]")
        sys.exit(1)

if (num_args == 3):
    gui_file = sys.argv[2]
elif (num_args == 4):
    colorname1 = sys.argv[2]
    colorname2 = sys.argv[3]
elif (num_args == 5):
    gui_file = sys.argv[2]
    colorname1 = sys.argv[3]
    colorname2 = sys.argv[4]
elif (num_args > 5):
    print("Usage: python " + sys.argv[0] + " <config-file.xml> [<gui-file.py>] [<colorname1> <colorname2>]")
    sys.exit(1)

print()
print("config_file = ",config_file)
print("colorname1 = ",colorname1)
print("colorname2 = ",colorname2)
print()

if (num_args == 3):
    with open(gui_file) as f:   # e.g., "mygui.py"
    #  newText = f.read().replace('myconfig.xml', config_file) # rwh todo: don't assume this string; find line
        file_str = f.read()
        idx = file_str.find('main_xml_filename')  # verify > -1
        file_pre = file_str[:idx] 
        idx2 = file_str[idx:].find('\n')
        file_post = file_str[idx+idx2:] 

    with open(gui_file, "w") as f:
        f.write(file_pre)
        f.write("main_xml_filename = '" + config_file + "'")
        f.write(file_post)

#---------------------------------------------------------------------------------------------------
cells_tab_header = """ 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box,Dropdown
    
class CellsDefTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        self.parent_name = Text(value='None',placeholder='Type something',description='Parent:',disabled=True)

        self.cell_type_dropdown = Dropdown(description='Cell type:',)
        self.cell_type_dropdown.style = {'description_width': '%sch' % str(len(self.cell_type_dropdown.description) + 1)}

        self.cell_type_parent_row = HBox([self.cell_type_dropdown, self.parent_name])
        self.cell_type_parent_dict = {}
"""

"""
        self.cell_parent_dict = {'lung epithelium':'default', 'immune':'default', 'CD8 Tcell':'immune'}

        self.therapy_activation_time = BoundedFloatText(
            min=0.,
            max=100000000,
            step=stepsize,
            description='therapy_activation_time',
            style=style, layout=layout,
            # layout=Layout(width=constWidth),
        )
        self.save_interval_after_therapy_start = BoundedFloatText(
            min=0.,
            max=100000000,
            step=stepsize,
            description='save_interval_after_therapy_start',
            style=style, layout=layout,
        )

        label_blankline = Label('')

        self.tab = VBox([HBox([self.therapy_activation_time, Label('min')]), 
                         HBox([self.save_interval_after_therapy_start, Label('min')]), 
                         ])  
"""

fill_gui_str= """

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

"""

fill_xml_str= """

    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

"""
cell_type_dropdown_cb = """
    #------------------------------
    def cell_type_cb(self, change):
      if change['type'] == 'change' and change['name'] == 'value':
        print("changed to %s" % change['new'])
        # self.vbox1.layout.visibility = 'hidden'  # vs. visible
        # self.vbox1.layout.visibility = None 
        self.vbox1.layout.display = 'none' 
"""

def get_float_stepsize(val_str):
    # fval_abs = abs(float(ppchild.text))
    fval_abs = abs(float(val_str))
    if (fval_abs > 0.0):
        if (fval_abs > 1.0):  # crop
            delta_val = pow(10, int(math.log10(abs(float(ppchild.text)))) - 1)
        else:   # round
            delta_val = pow(10, round(math.log10(abs(float(ppchild.text)))) - 1)
    else:
        delta_val = 0.01  # if initial value=0.0, we're totally guessing at what a good delta is
    return delta_val

# Now parse a configuration file (.xml) and map the user parameters into GUI widgets
#tree = ET.parse('../config/PhysiCell_settings.xml')
try:
    tree = ET.parse(config_file)
except:
    print("Cannot parse",config_file, "- check it's XML syntax.")
    sys.exit(1)

root = tree.getroot()

indent = "        "
indent2 = "          "
widgets = {"double":"FloatText", "int":"IntText", "bool":"Checkbox", "string":"Text", "divider":""}
#widgets = {"double":"FloatText", "int":"IntText", "bool":"Checkbox", "string":"Text"}
type_cast = {"double":"float", "int":"int", "bool":"bool", "string":"", "divider":"Text"}
vbox_str = "\n" + indent + "self.tab = VBox([\n"
#param_desc_buttons_str = "\n" 
#name_buttons_str = "\n" 
units_buttons_str = "\n" 
desc_buttons_str = "\n"
header_buttons_str = "\n"
row_str = "\n"
box_str = "\n" + indent + "box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')\n"
row_header_str = "\n"
box_header_str = "\n"
#        box1 = Box(children=row1, layout=box_layout)\n"

menv_var_count = 0   # micronenv 
param_count = 0
divider_count = 0
color_count = 0
#param_desc_count = 0
name_count = 0
units_count = 0

#---------- cell_definitions --------------------
# TODO: cast attributes to lower case before doing equality tests; perform more testing!

uep = root.find('.//cell_definitions')  # find unique entry point (uep) 
fill_gui_str += indent + "uep = xml_root.find('.//cell_definitions')  # find unique entry point\n"
fill_xml_str += indent + "uep = xml_root.find('.//cell_definitions')  # find unique entry point\n"

# param_count = 0
   #param_desc_count = 0
# name_count = 0
# units_count = 0

print_vars = True
print_var_types = False

tag_list = []

# function to process a "divider" type element
def handle_divider(child):
    global divider_count, cells_tab_header, indent, indent2, vbox_str
    divider_count += 1
    print('-----------> handler_divider: ',divider_count)
    row_name = "div_row" + str(divider_count)
    cells_tab_header += "\n" + indent + row_name + " = " + "Button(description='" + child.attrib['description'] + "', disabled=True, layout=divider_button_layout)\n"
    vbox_str += indent2 + row_name + ",\n"


#===========  main loop ===================
ndent = "\n" + indent 
ndent2 = "\n" + indent2

# NOTE: we assume a simple "children-only" hierarchy in <user_parameters>
# for child in uep:   # uep = "unique entry point" for <user_parameters> (from above)

#        self.cell_type.options={'default':'default', 'worker':'worker', 'director':'director', 'cargo':'cargo'}
cells_tab_header += ndent + "self.cell_type_dict = {}"  
#row_name + " = " + "Button(description='" + child.attrib['description'] + "', disabled=True, layout=divider_button_layout)\n"

#--------- for each <cell_definition>
for child in uep.findall('cell_definition'):
    if print_vars:
        print(child.tag, child.attrib)
        print(child.attrib['name'])
    # cells_tab_header += "'" + child.attrib['name'] + ":'"
    name_str = "'" + child.attrib['name'] + "'"
    cells_tab_header += ndent + "self.cell_type_dict[" + name_str + "] = " + name_str 

cells_tab_header += ndent + "self.cell_type_dropdown.options = self.cell_type_dict\n"
            
# create parent dict
for child in uep.findall('cell_definition'):
    name_str = "'" + child.attrib['name'] + "'"
    if 'parent_type' in child.attrib:
        parent_str = "'" + child.attrib['parent_type'] + "'"
    else:
        parent_str = "'None'"
    cells_tab_header += ndent + "self.cell_type_parent_dict[" + name_str + "] = " + parent_str 


vbox_str += indent2 + "self.cell_type_parent_row, \n"
#    cells_tab_header += "\n" + indent + row_name + " = " + "Button(description='" + child.attrib['description'] + "', disabled=True, layout=divider_button_layout)\n"

for child in uep.findall('cell_definition'):
    divider_flag = False
    if 'type' in child.attrib.keys() and (child.attrib['type'].lower() == 'divider'):
        divider_flag = True
    else:
        param_count += 1

    # we allow the divider elements to have the same name, but not other elements
    # if (child.tag in tag_list) and (not divider_flag):
    #     print("-------> Warning: duplicate tag!  ", child.tag)
    #     continue
    # else:
    #     tag_list.append(child.tag)
    units_str = ""
    describe_str = ""
    if 'hidden' in child.attrib.keys() and (child.attrib['hidden'].lower() == "true"):   # do we want to hide this from the user?
        print("  HIDE this parameter from the GUI: ", child.tag)
        continue

#    names_str = ''
#    units_str = ''
    # describe_str = ''
#    desc_row_name = None
    desc_row_name = ''
    units_btn_name = ''


    if not divider_flag:
        if 'description' in child.attrib.keys():
            describe_str = child.attrib['description']
        else:
            describe_str = ""
        desc_row_name = "desc_button" + str(param_count)
        desc_buttons_str += indent + desc_row_name + " = " + "Button(description='" + describe_str + "', disabled=True, layout=desc_button_layout) \n"
        # print("--- debug: " + desc_row_name + " --> " + describe_str)   #rwh debug

        if (param_count % 2):
            desc_buttons_str += indent + desc_row_name + ".style.button_color = '" + colorname1 + "'\n"
        else:  # rf.  https://www.w3schools.com/colors/colors_names.asp
            desc_buttons_str += indent + desc_row_name + ".style.button_color = '" + colorname2 + "'\n"

    if 'units' in child.attrib.keys():
        if child.attrib['units'] != "dimensionless" and child.attrib['units'] != "none":
#            units_str = child.attrib['units']
            units_count += 1
            units_btn_name = "units_button" + str(units_count)
            units_buttons_str += indent + units_btn_name + " = " + "Button(description='" + child.attrib['units'] + "', disabled=True, layout=units_button_layout) \n"
            if (param_count % 2):
                units_buttons_str += indent + units_btn_name + ".style.button_color = '" + colorname1 + "'\n"
            else:  # rf.  https://www.w3schools.com/colors/colors_names.asp
                units_buttons_str += indent + units_btn_name + ".style.button_color = '" + colorname2 + "'\n"
        else:
            units_count += 1
            units_btn_name = "units_button" + str(units_count)
            units_buttons_str += indent + units_btn_name + " = " + "Button(description='" +  "', disabled=True, layout=units_button_layout) \n"
            if (param_count % 2):
                units_buttons_str += indent + units_btn_name + ".style.button_color = '" + colorname1 + "'\n"
            else:  # rf.  https://www.w3schools.com/colors/colors_names.asp
                units_buttons_str += indent + units_btn_name + ".style.button_color = '" + colorname2 + "'\n"
    else:
        units_count += 1
        units_btn_name = "units_button" + str(units_count)
        units_buttons_str += indent + units_btn_name + " = " + "Button(description='" +  "', disabled=True, layout=units_button_layout) \n"
        if (param_count % 2):
            units_buttons_str += indent + units_btn_name + ".style.button_color = '" + colorname1 + "'\n"
        else:  # rf.  https://www.w3schools.com/colors/colors_names.asp
            units_buttons_str += indent + units_btn_name + ".style.button_color = '" + colorname2 + "'\n"

    if 'type' in child.attrib.keys():
#             self.therapy_activation_time = BoundedFloatText(
#            min=0., max=100000000, step=stepsize,
        full_name = "self." + child.tag
        # name_count += 1
        if child.attrib['type'] not in widgets.keys():
            print("    *** Error - Invalid type: " + child.attrib['type'])
            sys.exit(1)
        else:    
            # The "divider" type elements are unique; let's handle them in their own function
            if divider_flag:
                handle_divider(child)
                continue

            name_count += 1
            param_name_button = "param_name" + str(name_count)
            cells_tab_header += "\n" + indent + param_name_button + " = " + "Button(description='" + child.tag + "', disabled=True, layout=name_button_layout)\n"
            if (param_count % 2):
                cells_tab_header += indent + param_name_button + ".style.button_color = '" + colorname1 + "'\n"
            else:  # rf.  https://www.w3schools.com/colors/colors_names.asp
                cells_tab_header += indent + param_name_button + ".style.button_color = '" + colorname2 + "'\n"
            cells_tab_header += "\n" + indent + full_name + " = " + widgets[child.attrib['type']] + "(\n"

            # Try to calculate and provide a "good" delta step (for the tiny "up/down" arrows on a numeric widget)
            if child.attrib['type'] == "double":
                fval_abs = abs(float(child.text))
                if (fval_abs > 0.0):
                    if (fval_abs > 1.0):  # crop
                        delta_val = pow(10, int(math.log10(abs(float(child.text)))) - 1)
                    else:   # round
                        delta_val = pow(10, round(math.log10(abs(float(child.text)))) - 1)
                else:
                    delta_val = 0.01  # if initial value=0.0, we're totally guessing at what a good delta is
                if print_var_types:
                    print('double: ',float(child.text),', delta_val=',delta_val)

                cells_tab_header += indent2 + "value=" + child.text + ",\n"
                # Note: "step" values will advance the value to the nearest multiple of the step value itself :-/
                cells_tab_header += indent2 + "step=" + str(delta_val) + ",\n"

            # Integers
            elif child.attrib['type'] == "int":  # warning: math.log(1000,10)=2.99..., math.log10(1000)=3  
                if (abs(int(child.text)) > 0):
                    delta_val = pow(10,int(math.log10(abs(int(child.text)))) - 1)
                else:
                    delta_val = 1  # if initial value=0, we're totally guessing at what a good delta is
                if print_var_types:
                    print('int: ',int(child.text),', delta_val=',delta_val)

                cells_tab_header += indent2 + "value=" + child.text + ",\n"
                cells_tab_header += indent2 + "step=" + str(delta_val) + ",\n"

            # Booleans
            elif child.attrib['type'] == "bool":
                if (child.text.lower() == "true"):
                    child.text = "True"
                elif (child.text.lower() == "false"):
                    child.text = "False"
                else:
                    print(" --- ERROR: bool must be True or False, not ", child.text)
                    sys.exit(1)

                if print_var_types:
                    print('bool: ',child.text)
                cells_tab_header += indent2 + "value=" + child.text + ",\n"
            
            # Strings
            elif child.attrib['type'] == "string":
                cells_tab_header += indent2 + "value='" + child.text + "',\n"

            row_name = "row" + str(param_count)
            box_name = "box" + str(param_count)
            if (not divider_flag):
                # We're processing a "normal" row - typically a name, numeric field, units, description
                #  - append the info at the end of this widget
                cells_tab_header += indent2 + "style=style, layout=widget_layout)\n"

                row_str += indent +  row_name + " = [" + param_name_button + ", " + full_name + ", " +      units_btn_name + ", " + desc_row_name + "] \n"

                box_str += indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n"
            else:  # divider
                box_str += indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n"

            vbox_str += indent2 + box_name + ",\n"

            if (not divider_flag):
                # float, int, bool
                if (type_cast[child.attrib['type']] == "bool"):
                    fill_gui_str += indent + full_name + ".value = ('true' == (uep.find('.//" + child.tag + "').text.lower()) )\n"
                else:
                    fill_gui_str += indent + full_name + ".value = " + type_cast[child.attrib['type']] + "(uep.find('.//" + child.tag + "').text)\n"

                fill_xml_str += indent + "uep.find('.//" + child.tag + "').text = str("+ full_name + ".value)\n"

vbox_str += indent + "])"

# Write the beginning of the Python module for the user parameters tab in the GUI
cells_tab_file = "cells_def.py"
print("\n --------------------------------- ")
print("Generated a new: ", cells_tab_file)
print()
fp= open(cells_tab_file, 'w')
fp.write(cells_tab_header)
fp.write(units_buttons_str)
fp.write(desc_buttons_str)
fp.write(row_str)
fp.write(box_str)
fp.write(vbox_str)
fp.write(cell_type_dropdown_cb)
fp.write(fill_gui_str)
fp.write(fill_xml_str)
fp.close()


#=================================================================
print()
#print("If this is your first time:")
#print("Run the GUI via:  jupyter notebook mygui.ipynb")
print("Test the minimal GUI via:  jupyter notebook test_gui.ipynb")
print("run the Jupyter menu item:  Cell -> Run All")
print()
print("(or, if you already have a previous GUI running and want to see new params:")
print("run the Jupyter menu item:  Kernel -> Restart & Run All)")
print()