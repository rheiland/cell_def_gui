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
color_idx = 0

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
colorname = [colorname1,colorname2]
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
        divider_button_layout={'width':'60%'}
        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')

        self.parent_name = Text(value='None',placeholder='Type something',description='Parent:',disabled=True)

        self.cell_type_dropdown = Dropdown(description='Cell type:',)
        self.cell_type_dropdown.style = {'description_width': '%sch' % str(len(self.cell_type_dropdown.description) + 1)}

        self.cell_type_parent_row = HBox([self.cell_type_dropdown, self.parent_name])
        self.cell_type_parent_dict = {}
"""


fill_gui_str= """

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        float_var_count = 0
        uep = xml_root.find('.//cell_definitions')  # find unique entry point

"""

fill_xml_str= """

    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//cell_definitions')  # find unique entry point
        for cell_def in uep.findall('cell_definition'):
            print('fill_xml: ',cell_def)

"""

display_cell_type_default = """
    #------------------------------
    def display_cell_type_default(self):
        # print("display_cell_type_default():")
        #print("    self.cell_type_parent_dict = ",self.cell_type_parent_dict)

        # There's probably a better way to do this, but for now,
        # we hide all vboxes containing the widgets for the different cell defs
        # and only display the contents of 'default'
        for vb in self.cell_def_vboxes:
            vb.layout.display = 'none'   # vs. 'contents'
        self.cell_def_vboxes[0].layout.display = 'contents'
"""

cell_type_dropdown_cb = """
    #------------------------------
    def cell_type_cb(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
            # print("changed to %s" % change['new'])
            self.parent_name.value = self.cell_type_parent_dict[change['new']]
            idx_selected = list(self.cell_type_parent_dict.keys()).index(change['new'])
            # print('index=',idx_selected)
            # self.vbox1.layout.visibility = 'hidden'  # vs. visible
            # self.vbox1.layout.visibility = None 

            # There's probably a better way to do this, but for now,
            # we hide all vboxes containing the widgets for the different cell defs
            # and only display the contents of the selected one.
            for vb in self.cell_def_vboxes:
                vb.layout.display = 'none'   # vs. 'contents'
            self.cell_def_vboxes[idx_selected].layout.display = 'contents'   # vs. 'contents'

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
main_vbox_str = "\n" + indent + "self.tab = VBox([\n"
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

float_var_count = 0    # FloatText
bool_var_count = 0   
text_var_count = 0   

divider_count = 0
color_count = 0
#param_desc_count = 0
name_count = 0
units_count = 0


custom_data_widgets = {"double":"FloatText", "int":"IntText", "bool":"Checkbox", "string":"Text", "divider":""}
custom_data_type_cast = {"double":"float", "int":"int", "bool":"bool", "string":"", "divider":"Text"}

#---------- cell_definitions --------------------
# TODO: cast attributes to lower case before doing equality tests; perform more testing!

uep = root.find('.//cell_definitions')  # find unique entry point (uep) 
# fill_gui_str += indent + "uep = xml_root.find('.//cell_definitions')  # find unique entry point\n"
# fill_xml_str += indent + "uep = xml_root.find('.//cell_definitions')  # find unique entry point\n"

# param_count = 0
   #param_desc_count = 0
# name_count = 0
# units_count = 0

print_vars = False
print_var_types = False

tag_list = []

# function to process a "divider" type element
def handle_divider(child):
    global divider_count, cells_tab_header, indent, indent2, main_vbox_str
    divider_count += 1
    # print('-----------> handler_divider: ',divider_count)
    row_name = "div_row" + str(divider_count)
    cells_tab_header += "\n" + indent + row_name + " = " + "Button(description='" + child.attrib['description'] + "', disabled=True, layout=divider_button_layout)\n"
    main_vbox_str += indent2 + row_name + ",\n"

def handle_divider_pheno(div_str):
    global divider_count, cells_tab_header, indent, indent2, main_vbox_str
    divider_count += 1
    # print('-----------> handler_divider_pheno: ',divider_count)
    row_name = "div_row" + str(divider_count)
    cells_tab_header += indent + row_name + " = " + "Button(description='" + div_str + "', disabled=True, layout=divider_button_layout)\n"
    cells_tab_header += indent + row_name + ".style.button_color = 'orange'\n"
#    main_vbox_str += indent2 + row_name + ",\n"
    return row_name


#===========  main loop ===================
ndent = "\n" + indent 
ndent2 = "\n" + indent2

# NOTE: we assume a simple "children-only" hierarchy in <user_parameters>
# for child in uep:   # uep = "unique entry point" for <user_parameters> (from above)

#        self.cell_type.options={'default':'default', 'worker':'worker', 'director':'director', 'cargo':'cargo'}
cells_tab_header += ndent + "self.cell_type_dict = {}"  
#row_name + " = " + "Button(description='" + child.attrib['description'] + "', disabled=True, layout=divider_button_layout)\n"


#--------- Let's do a 3-pass parsing of <cell_definitions> in the .xml file

#--- 1) create a dict ("cell_type_dict") of <cell_definition> names
for child in uep.findall('cell_definition'):
    if print_vars:
        print(child.tag, child.attrib)
        print(child.attrib['name'])
    # cells_tab_header += "'" + child.attrib['name'] + ":'"
    name_str = "'" + child.attrib['name'] + "'"
    cells_tab_header += ndent + "self.cell_type_dict[" + name_str + "] = " + name_str 

cells_tab_header += ndent + "self.cell_type_dropdown.options = self.cell_type_dict\n"
cells_tab_header += ndent + "self.cell_type_dropdown.observe(self.cell_type_cb)\n"
            
#--- 2) create a dict ("cell_type_parent_dict") of <cell_definition> parents
for child in uep.findall('cell_definition'):
    name_str = "'" + child.attrib['name'] + "'"
    if 'parent_type' in child.attrib:
        parent_str = "'" + child.attrib['parent_type'] + "'"
    else:
        parent_str = "'None'"
    cells_tab_header += ndent + "self.cell_type_parent_dict[" + name_str + "] = " + parent_str 
cells_tab_header += "\n\n"
# e.g., self.cell_type_parent_dict =  {'default': 'None', 'lung epithelium': 'default', 'immune': 'default', 'CD8 Tcell': 'immune', 'macrophage': 'immune', 'neutrophil': 'immune'}


main_vbox_str += indent2 + "self.cell_type_parent_row, \n"
#    cells_tab_header += "\n" + indent + row_name + " = " + "Button(description='" + child.attrib['description'] + "', disabled=True, layout=divider_button_layout)\n"


cells_tab_header += ndent + "self.cell_def_vboxes = []\n" 

motility_count = 0
cell_def_count = 0
box_count = 0

#--- 3) primary pass to generate all ipywidgets Python code, initialize their values from those 
#       in the .xml, and generate code for the 2 functions, "fill_gui" and "fill_xml"
#       
for cell_def in uep.findall('cell_definition'):
#   handle_divider_pheno("---------------")
#   fill_gui_str += indent + "cell_def = uep.find('.//cell_definition')
#   cell_def_count_start = cell_def_count 
  uep_phenotype = cell_def.find('phenotype')
  			# </phenotype>
			# <custom_data> 

#   float_path_str0 = "float(uep.find('.//phenotype[" + str(cell_def_count+1) + "]"
#   print("---------------- float_path_str0 = ", float_path_str0)
  subpath0 = ".//phenotype[" + str(cell_def_count+1) + "]"
  print("\n\n---------------- subpath0 ",cell_def.attrib['name'], " = ", subpath0)

#   fill_gui_str += indent + "uep_phenotype = cell_def.find('.//phenotype')
#   print('pheno=',uep_phenotype)
  prefix = 'phenotype:'
  elm_str = ""
  rate_count = 0
  for child in uep_phenotype:
    print('pheno child=',child)
    if child.tag == 'cycle':
        fill_gui_str += indent + "# ---------  cycle  ---------\n"

        # float_str += float(uep.find('.//phenotype[1]//cycle//transition_rates//rate[1]').text)
        # float_path_str = float_path_str0  + "//cycle"
        subpath1 = subpath0  + "//cycle"
        print("\n---------------- subpath1 = ", subpath1)

        # fill_gui_str += indent + "child_def = uep.find('.//cell_def')
        # print('cycle code=',child.attrib['code'])
        # print('cycle name=',child.attrib['name'])

        # TODO: show (allow edit??) the cycle code/name
        divider_pheno_name = handle_divider_pheno(prefix + "cycle") 
        elm_str += divider_pheno_name + ", "
        # print(elm_str)
        color_str = indent + divider_pheno_name + ".style.button_color = '" + colorname[color_idx] + "'\n"

        # float_path_str += "//transition_rates"
        subpath2 = subpath1 + "//transition_rates"
        print("\n---------------- subpath2 = ", subpath2)
        for rates in child:
            # print('--- rates elm=',rates)
            units_str = rates.attrib['units']
            rate_count = 0
            for rate in rates:
                # print('----- rate elm=',rate)
                btn_name = "transition rate: " + rate.attrib['start_index'] + "->" + rate.attrib['end_index']
                w1 = "name_btn"
                btn_str = indent + w1 + " = Button(description='" + btn_name + "', disabled=True, layout=name_button_layout)\n"
                cells_tab_header += btn_str

                color_str = indent + w1 + ".style.button_color = '" + colorname[color_idx] + "'\n"
                cells_tab_header += color_str

                w2 = "self.float" + str(float_var_count)
                float_var_count += 1
                btn_str = indent + w2 + " = FloatText(value='" + rate.text + "',  style=style, layout=widget_layout)\n"
                cells_tab_header += btn_str

                rate_count += 1

                # float_gui_str = float_path_str +  "//rate[" + str(rate_count) + "]').text)\n"
                # subpath = subpath2 +  "//rate[" + str(rate_count) + "]').text)"
                subpath = subpath2 +  "//rate[" + str(rate_count) + "]"
                print("\n---------------- subpath = ", subpath)
                # self.float0.value = float(uep.find('.//phenotype[1]//cycle//transition_rates//rate[1]').text)
                # fill_gui_str += indent + w2 + ".value = " + float_gui_str
#   float_path_str0 = "float(uep.find('.//phenotype[" + str(cell_def_count+1) + "]"
#   self.float0.value = float(uep.find('.//phenotype[1]//cycle//transition_rates//rate[1]').text)
                fill_gui_str += indent + w2 + ".value = float(uep.find('" + subpath + "').text)\n"

                # fill_xml_str += "#" +indent + "uep.find('.//" + child.tag + "').text = str("+ w2 + ".value)\n"

                w3 = "units_btn" 
                btn_str = indent + w3 + " = Button(description='" + units_str + "', disabled=True, layout=units_button_layout)\n"
                cells_tab_header += btn_str

                color_str = indent + w3 + ".style.button_color = '" + colorname[color_idx] + "'\n"
                cells_tab_header += color_str
                color_idx = 1 - color_idx

                row_name = "row" 
                row_str = indent + row_name + " = [" + w1 + ", " + w2 +  ", " + w3 + "]\n"
                cells_tab_header += row_str

                box_name = "box" + str(box_count) 
                box_count += 1
                box_str = indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n\n"
                cells_tab_header += box_str 
                elm_str += box_name + ", "


    elif child.tag == 'death':
        fill_gui_str += indent + "# ---------  death  ---------\n"

        # float_path_str = float_path_str0  + "//death"
        subpath1 = subpath0  + "//death"
        print("\n---------------- subpath1 = ", subpath1)
        death_model_count = 0
        elm_str += handle_divider_pheno(prefix + "death") + ", "
        for death_model in child:
            # float_gui_str = float_path_str +  "//model[" + str(death_model_count) + "]').text)\n"
            death_model_count += 1
            # float_gui_str = float_path_str +  "//model[" + str(death_model_count) + "]"
            subpath2 = subpath1 +  "//model[" + str(death_model_count) + "]"
            print("\n---------------- subpath2 = ", subpath2)

            row_name = "death_model" + str(death_model_count)
            death_header_str = indent + row_name + " = " + "Button(description='" + death_model.attrib['name'] + "', disabled=True, layout={'width':'30%'})\n"
            cells_tab_header += death_header_str 
            elm_str += row_name + ","

            # print('death code=',death_model.attrib['code'])
            # print('death name=',death_model.attrib['name'])
            # elm_str += handle_divider_pheno(prefix + "death:" + death_model.attrib['name']) + ", "
            # print(elm_str)

            #----------  overall death model rate -------------
            rate = death_model.find('.//rate')  
            subpath3 = subpath2 +  "//rate"
            print("\n---------------- subpath3 = ", subpath3)

            # self.float4.value = float(uep.find('.//phenotype[1]//death//model[1]//rate').text)
            # float_gui_str += "//rate').text)\n"
            # subpath3 = subpath2 +  "//model"
            # print("\n---------------- subpath3 = ", subpath3)
            # print('rate units=',rate.attrib['units'])

            w1 = "name_btn"
            btn_str = indent + w1 + " = Button(description='rate', disabled=True, layout=name_button_layout)\n"
            cells_tab_header += btn_str
            color_str = indent + w1 + ".style.button_color = '" + colorname[color_idx] + "'\n"
            cells_tab_header += color_str

            w2 = "self.float" + str(float_var_count)
            float_var_count += 1
            btn_str = indent + w2 + " = FloatText(value='" + rate.text + "',  style=style, layout=widget_layout)\n"
            cells_tab_header += btn_str

            # w3 = "units_btn" + str(rate_count) 
            w3 = "units_btn"
            btn_str = indent + w3 + " = Button(description='" + units_str + "', disabled=True, layout=units_button_layout)\n"
            cells_tab_header += btn_str

            color_str = indent + w3 + ".style.button_color = '" + colorname[color_idx] + "'\n"
            cells_tab_header += color_str
            color_idx = 1 - color_idx

            # fill_gui_str += "#" +indent + w2 + ".value = " + 'float' + "(uep.find('.//" + child.tag + "').text)\n"
            # fill_gui_str += indent + w2 + ".value = " + 'float' + \n"
            # self.float4.value = float(uep.find('.//phenotype[1]//death//model[1]//rate').text)
            # fill_gui_str += indent + w2 + ".value = " + float_gui_str + "\n"
            # fill_gui_str += indent + w2 + ".value = float(uep.find(" + subpath + ").text)"
            fill_gui_str += indent + w2 + ".value = float(uep.find('" + subpath3 + "').text)\n"

            # fill_xml_str += "#" +indent + "uep.find('.//" + child.tag + "').text = str("+ w2 + ".value)\n"


            # row1 = [cycle_rate_btn1, self.cycle_rate_float1, units_btn] 
            # row_name = "row" + str(rate_count)
            row_name = "row"
            row_str = indent + row_name + " = [" + w1 + ", " + w2 +  ", " + w3 + "]\n"
            cells_tab_header += row_str

    # box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
    # box1 = Box(children=row1, layout=box_layout)
            box_name = "box" + str(box_count) 
            box_count += 1
            # box_str = indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n\n"
            box_str = indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n\n"
            cells_tab_header += box_str 
            elm_str += box_name + ", "


            #----------  death model transition rate(s) -------------
            # TODO: fixed_duration
            t_rate = death_model.find('.//transition_rates')  
            rate_count = 1
            subpath3 = subpath2 +  "//transition_rates" 
            # print('t_rate units=',t_rate.attrib['units'])
            for rate in t_rate:
                # argh, these widget names have gotten out of control
                w0 = "self." + cell_def.tag + "_death_model_" + death_model.attrib["code"] + "_trate" + rate.attrib['start_index'] + rate.attrib['end_index'] + "_toggle"

                if rate.attrib['fixed_duration'].lower() == 'true':
                    val = "True"
                else:
                    val = "False"
                toggle_str = indent + w0 + " = Checkbox(description='fixed_duration', value=" + val + ",layout=name_button_layout)\n"
                cells_tab_header += toggle_str

                # print('   ' + rate.attrib['start_index'] + ' -> ' + rate.attrib['end_index'])

                # btn_name = death_model.attrib['name'] + " rate: " + rate.attrib['start_index'] + "->" + rate.attrib['end_index']
                btn_name = "transition rate: " + rate.attrib['start_index'] + "->" + rate.attrib['end_index']
                w1 = "cycle_rate_btn" + str(rate_count) 
                btn_str = indent + w1 + " = Button(description='" + btn_name + "', disabled=True, layout=name_button_layout)\n"
                cells_tab_header += btn_str
                color_str = indent + w1 + ".style.button_color = '" + colorname[color_idx] + "'\n"
                cells_tab_header += color_str

                w2 = "self.float" + str(float_var_count)
                float_var_count += 1
                btn_str = indent + w2 + " = FloatText(value='" + rate.text + "',  style=style, layout=widget_layout)\n"
                cells_tab_header += btn_str

                # self.float0.value = float(uep.find('.//phenotype[1]//cycle//transition_rates//rate[1]').text)
                # float_gui_str = float_path_str +  "//rate[" + str(rate_count) + "]').text)\n"
                # subpath3 = subpath2 +  "//model[" + str(death_model_count) + "]"
                subpath4 = subpath3 +  "//rate[" + str(rate_count) + "]"
                rate_count += 1
                print("\n---------------- subpath4 = ", subpath4)

#        self.float4.value = float(uep.find('.//phenotype[1]//death//model[1]//rate').text)
                # fill_gui_str += indent + w2 + ".value = " + float_gui_str + "\n"
                fill_gui_str += indent + w2 + ".value = float(uep.find('" + subpath4 + "').text)\n"
                # fill_gui_str += indent + "uep.find('.//" + child.tag + "').text = str("+ w2 + ".value)\n"

                w3 = "units_btn" + str(rate_count) 
                btn_str = indent + w3 + " = Button(description='" + units_str + "', disabled=True, layout=units_button_layout)\n"
                cells_tab_header += btn_str

                color_str = indent + w3 + ".style.button_color = '" + colorname[color_idx] + "'\n"
                cells_tab_header += color_str
                color_idx = 1 - color_idx


                # fill_xml_str += "#" +indent + "uep.find('.//" + child.tag + "').text = str("+ w2 + ".value)\n"

                # row1 = [cycle_rate_btn1, self.cycle_rate_float1, units_btn] 
                # row_name = "row" + str(rate_count)
                row_name = "row"
                row_str = indent + row_name + " = [" + w0 + ", " + w1 + ", " + w2 +  ", " + w3 + "]\n"
                cells_tab_header += row_str

                box_name = "box" + str(box_count) 
                box_count += 1
                box_str = indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n\n"
                cells_tab_header += box_str 
                elm_str += box_name + ", "

            #----------  death model <parameters> -------------
            d_params = death_model.find('.//parameters')  
            subpath3 = subpath2 +  "//parameters" 
            for elm in d_params:
                # w1 = elm.tag + "_" + death_model.attrib['name'] 
                subpath4 = subpath3 +  "//" + elm.tag 
                w1 = "name_btn"
                btn_str = indent + w1 + " = Button(description='" + elm.tag + "', disabled=True, layout=name_button_layout)\n"
                cells_tab_header += btn_str
                color_str = indent + w1 + ".style.button_color = '" + colorname[color_idx] + "'\n"
                cells_tab_header += color_str

                w2 = "self.float" + str(float_var_count)
                float_var_count += 1
                btn_str = indent + w2 + " = FloatText(value='" + elm.text + "',  style=style, layout=widget_layout)\n"
                cells_tab_header += btn_str

                fill_gui_str += indent + w2 + ".value = float(uep.find('" + subpath4 + "').text)\n"

                # w3 = "units_btn" +  elm.attrib['units'] 
                w3 = "units_btn" 
                btn_str = indent + w3 + " = Button(description='" + units_str + "', disabled=True, layout=units_button_layout)\n"
                cells_tab_header += btn_str
                color_str = indent + w3 + ".style.button_color = '" + colorname[color_idx] + "'\n"
                cells_tab_header += color_str
                color_idx = 1 - color_idx

                # fill_gui_str += "#" +indent + w2 + ".value = " + 'float' + "(uep.find('.//" + child.tag + "').text)\n"
                # fill_xml_str += "#" +indent + "uep.find('.//" + child.tag + "').text = str("+ w2 + ".value)\n"

                row_name = "row" 
                row_str = indent + row_name + " = [" + w1 + ", " + w2 +  ", " + w3 + "]\n"
                cells_tab_header += row_str

                box_name = "box" + str(box_count) 
                box_count += 1
                box_str = indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n\n"
                cells_tab_header += box_str 
                elm_str += box_name + ", "


    elif child.tag == 'volume':
        fill_gui_str += indent + "# ---------  volume  ---------\n"
        elm_str += handle_divider_pheno(prefix + "volume") + ", "
        # print(elm_str)
        for elm in child:
            # w1 = child.tag + '_' + elm.tag 
            w1 = "name_btn"
            btn_str = indent + w1 + " = Button(description='" + elm.tag + "', disabled=True, layout=name_button_layout)\n"
            cells_tab_header += btn_str
            color_str = indent + w1 + ".style.button_color = '" + colorname[color_idx] + "'\n"
            cells_tab_header += color_str

            w2 = "self.float" + str(float_var_count)
            float_var_count += 1
            btn_str = indent + w2 + " = FloatText(value='" + elm.text + "',  style=style, layout=widget_layout)\n"
            cells_tab_header += btn_str

            # w3 = "units_btn" +  elm.attrib['units'] 
            w3 = "units_btn" 
            units_str = elm.attrib['units'] 
            btn_str = indent + w3 + " = Button(description='" + units_str + "', disabled=True, layout=units_button_layout)\n"
            cells_tab_header += btn_str
            color_str = indent + w3 + ".style.button_color = '" + colorname[color_idx] + "'\n"
            cells_tab_header += color_str
            color_idx = 1 - color_idx

            # fill_gui_str += "#" +indent + w2 + ".value = " + 'float' + "(uep.find('.//" + child.tag + "').text)\n"
            # fill_xml_str += "#" +indent + "uep.find('.//" + child.tag + "').text = str("+ w2 + ".value)\n"

            row_name = "row" 
            row_str = indent + row_name + " = [" + w1 + ", " + w2 +  ", " + w3 + "]\n"
            cells_tab_header += row_str

            box_name = "box" + str(box_count) 
            box_count += 1
            box_str = indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n\n"
            cells_tab_header += box_str 
            elm_str += box_name + ", "


    elif child.tag == 'mechanics':
        fill_gui_str += indent + "# ---------  mechanics  ---------\n"
        elm_str += handle_divider_pheno(prefix + "mechanics") + ", "
        # print(elm_str)
        for elm in child:
            if elm.tag == 'options':
                for opt_elm in elm:
                    # TODO: improve toggle? 
                    w0 = 'self.' + child.tag + '_' + opt_elm.tag + '_toggle'
                    if opt_elm.attrib['enabled'].lower() == 'true':
                        val = "True"
                    else:
                        val = "False"
                    toggle_str = indent + w0 + " = Checkbox(description='enabled', value=" + val + ",layout=name_button_layout)\n"
                    cells_tab_header += toggle_str
                    # elm_str += full_name + ","

                    # w1 = child.tag + '_' + opt_elm.tag 
                    w1 = "name_btn"
                    btn_str = indent + w1 + " = Button(description='" + opt_elm.tag + "', disabled=True, layout=name_button_layout)\n"
                    cells_tab_header += btn_str
                    color_str = indent + w1 + ".style.button_color = '" + colorname[color_idx] + "'\n"
                    cells_tab_header += color_str

                    w2 = "self.float" + str(float_var_count)
                    float_var_count += 1
                    btn_str = indent + w2 + " = FloatText(value='" + opt_elm.text + "',  style=style, layout=widget_layout)\n"
                    cells_tab_header += btn_str

                    # w3 = "units_btn" +  elm.attrib['units'] 
                    w3 = "units_btn" 
                    units_str = opt_elm.attrib['units'] 
                    btn_str = indent + w3 + " = Button(description='" + units_str + "', disabled=True, layout=units_button_layout)\n"
                    cells_tab_header += btn_str
                    color_str = indent + w3 + ".style.button_color = '" + colorname[color_idx] + "'\n"
                    cells_tab_header += color_str
                    color_idx = 1 - color_idx

                    # fill_gui_str += "#" +indent + w2 + ".value = " + 'float' + "(uep.find('.//" + child.tag + "').text)\n"
                    # fill_xml_str += "#" +indent + "uep.find('.//" + child.tag + "').text = str("+ w2 + ".value)\n"

                    row_name = "row" 
                    row_str = indent + row_name + " = [" + w0 + ", " + w1 + ", " + w2 +  ", " + w3 + "]\n"
                    cells_tab_header += row_str

                    box_name = "box" + str(box_count) 
                    box_count += 1
                    box_str = indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n\n"
                    cells_tab_header += box_str 
                    elm_str += box_name + ", "
            else:
                # w1 = child.tag + '_' + elm.tag 
                w1 = "name_btn"
                btn_str = indent + w1 + " = Button(description='" + elm.tag + "', disabled=True, layout=name_button_layout)\n"
                cells_tab_header += btn_str
                color_str = indent + w1 + ".style.button_color = '" + colorname[color_idx] + "'\n"
                cells_tab_header += color_str

                w2 = "self.float" + str(float_var_count)
                float_var_count += 1
                btn_str = indent + w2 + " = FloatText(value='" + elm.text + "',  style=style, layout=widget_layout)\n"
                cells_tab_header += btn_str

                # w3 = "units_btn" +  elm.attrib['units'] 
                w3 = "units_btn" 
                units_str = elm.attrib['units'] 
                btn_str = indent + w3 + " = Button(description='" + units_str + "', disabled=True, layout=units_button_layout)\n"
                cells_tab_header += btn_str
                color_str = indent + w3 + ".style.button_color = '" + colorname[color_idx] + "'\n"
                cells_tab_header += color_str
                color_idx = 1 - color_idx

                # fill_gui_str += "#" +indent + w2 + ".value = " + 'float' + "(uep.find('.//" + child.tag + "').text)\n"
                # fill_xml_str += "#" +indent + "uep.find('.//" + child.tag + "').text = str("+ w2 + ".value)\n"

                row_name = "row" 
                row_str = indent + row_name + " = [" + w1 + ", " + w2 +  ", " + w3 + "]\n"
                cells_tab_header += row_str

            if elm.tag != 'options':
    # box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
    # box1 = Box(children=row1, layout=box_layout)
                box_name = "box" + str(box_count) 
                box_count += 1
                box_str = indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n\n"
                cells_tab_header += box_str 
                elm_str += box_name + ", "


    elif child.tag == 'motility':
        fill_gui_str += indent + "# ---------  motility  ---------\n"
        motility_count += 1
        elm_str += handle_divider_pheno(prefix + "motility") + ", "
        # print(elm_str)

        for elm in child:
            if elm.tag == 'options':
                for opt_elm in elm:
                    if opt_elm.tag == 'enabled':
                        full_name = "self." + elm.tag + '_' + opt_elm.tag + str(motility_count)
                        if opt_elm.text.lower() == 'true':
                            val = "True"
                        else:
                            val = "False"
                        toggle_str = indent + full_name + " = Checkbox(description='enabled', value=" + val + ",layout=name_button_layout)\n"
                        cells_tab_header += toggle_str
                        elm_str += full_name + ","

                    elif opt_elm.tag == 'use_2D':
                        full_name = "self." + elm.tag + '_' + opt_elm.tag + str(motility_count)
                        if opt_elm.text.lower() == 'true':
                            val = "True"
                        else:
                            val = "False"
                        toggle_str = indent + full_name + " = Checkbox(description='use_2D', value=" + val + ",layout=name_button_layout)\n"
                        cells_tab_header += toggle_str
                        elm_str += full_name + ","

                    elif opt_elm.tag == 'chemotaxis':
                        cells_tab_header += "\n"
                        row_name = "chemotaxis_btn"
                        chemo_header_str = indent + row_name + " = " + "Button(description='chemotaxis', disabled=True, layout={'width':'30%'})\n"
                        cells_tab_header += chemo_header_str 
                        elm_str += row_name + ","

                        for chemotaxis_elm in opt_elm:
                            cells_tab_header += "\n"
                            if chemotaxis_elm.tag == 'enabled':
                                full_name = "self." + elm.tag + '_' + opt_elm.tag + str(motility_count)
                                if opt_elm.text.lower() == 'true':
                                    val = "True"
                                else:
                                    val = "False"
                                toggle_str = indent + full_name + " = Checkbox(description='enabled', value=" + val + ",layout=name_button_layout)\n"
                                cells_tab_header += toggle_str
                                elm_str += full_name + ","

                            elif chemotaxis_elm.tag == 'substrate':
                                row_name = "chemotaxis_substrate" + str(motility_count)
                                chemo_subtrate_str = indent + row_name + " = " + "Button(description='substrate', disabled=True, layout=name_button_layout)\n"
                                cells_tab_header += chemo_subtrate_str 
                                # print('substrate color_idx = ',color_idx)
                                color_str = indent + row_name + ".style.button_color = '" + colorname[color_idx] + "'\n"
                                color_idx = 1 - color_idx
                                cells_tab_header += color_str

                                substrate_name = "self.chemotaxis_substrate" + str(motility_count)
                                substrate_text_str = indent + substrate_name + " = Text(value='" + chemotaxis_elm.text + "', style=style, layout=widget_layout)\n"
                                cells_tab_header += substrate_text_str

                                row_str = indent + "row = [" + row_name + ", " + substrate_name + "]\n"
                                cells_tab_header += row_str
                                # motility_box3 = Box(children=motility_row3, layout=box_layout)
                                box_name = "box" + str(box_count)
                                box_count += 1
                                box_str = indent + box_name + " = Box(children=row, layout=box_layout)\n"
                                cells_tab_header += box_str
                                elm_str += box_name + ","

                            elif chemotaxis_elm.tag == 'direction':
                                row_name = "chemotaxis_direction" + str(motility_count)
                                chemo_subtrate_str = indent + row_name + " = " + "Button(description='direction', disabled=True, layout=name_button_layout)\n"
                                cells_tab_header += chemo_subtrate_str 
                                # print('direction color_idx = ',color_idx)
                                color_str = indent + row_name + ".style.button_color = '" + colorname[color_idx] + "'\n"
                                color_idx = 1 - color_idx
                                cells_tab_header += color_str

                                full_name = "self.chemotaxis_direction" + str(motility_count)
                                dir_text_str = indent + full_name + " = Text(value='" + chemotaxis_elm.text + "', style=style, layout=widget_layout)\n"
                                cells_tab_header += dir_text_str

                                row_str = indent + "row = [" + row_name + ", " + full_name + "]\n"
                                cells_tab_header += row_str
                                # motility_box3 = Box(children=motility_row3, layout=box_layout)
                                box_name = "box" + str(box_count)
                                box_count += 1
                                box_str = indent + box_name + " = Box(children=row, layout=box_layout)\n"
                                cells_tab_header += box_str
                                elm_str += box_name + ","
                continue

            cells_tab_header += "\n"
            # print('--- motility elm.tag=',elm.tag)
            name_btn = child.tag + '_' + elm.tag + "name" + str(motility_count)
            btn_str = indent + name_btn + " = Button(description='" + elm.tag + "', disabled=True, layout=name_button_layout)\n"
            cells_tab_header += btn_str

            color_str = indent + name_btn + ".style.button_color = '" + colorname[color_idx] + "'\n"
            cells_tab_header += color_str

            name_float = "self.float" + str(float_var_count)
            float_var_count += 1
            float_str = indent + name_float + " = FloatText(value='" + elm.text + "', style=style, layout=widget_layout)\n"
            cells_tab_header += float_str
            if 'units' in elm.attrib.keys():
                units_str = elm.attrib['units']
                name_units = child.tag + '_' + elm.tag + "units" + str(motility_count)
                btn_str = indent + name_units + " = Button(description='" + units_str + "', disabled=True, layout=units_button_layout)\n"
                cells_tab_header += btn_str

                color_str = indent + name_units + ".style.button_color = '" + colorname[color_idx] + "'\n"
                cells_tab_header += color_str

            color_idx = 1 - color_idx

            # motility_row3 = [name_btn, self.motility_migration_bias1 , units_btn]
            row_str = indent + "row = [" + name_btn + ", " + name_float + ", " +  name_units + "]\n"
            cells_tab_header += row_str
            # motility_box3 = Box(children=motility_row3, layout=box_layout)
            box_name = "box" + str(box_count)
            box_count += 1
            box_str = indent + box_name + " = Box(children=row, layout=box_layout)\n"
            cells_tab_header += box_str
            elm_str += box_name + ","

    elif child.tag == 'secretion':
        fill_gui_str += indent + "# ---------  secretion  ---------\n"
        elm_str += handle_divider_pheno(prefix + "secretion") + ", "
        # print(elm_str)
        substrate_count = 0
        for elm in child:
            if elm.tag == 'substrate':
                # row_name = "secretion_substrate" + str(substrate_count)
                row_name = "secretion_substrate_btn" 
                chemo_subtrate_str = indent + row_name + " = " + "Button(description='substrate', disabled=True, layout=name_button_layout)\n"
                cells_tab_header += chemo_subtrate_str 
                # print('substrate color_idx = ',color_idx)
                color_str = indent + row_name + ".style.button_color = '" + colorname[color_idx] + "'\n"
                color_idx = 1 - color_idx
                cells_tab_header += color_str

                substrate_name = "self.secretion_substrate" + str(substrate_count)
                substrate_text_str = indent + substrate_name + " = Text(value='" + elm.attrib['name'] + "', style=style, layout=widget_layout)\n"
                cells_tab_header += substrate_text_str

                row_str = indent + "row = [" + row_name + ", " + substrate_name + "]\n"
                cells_tab_header += row_str
                box_name = "box" + str(box_count)
                box_count += 1
                box_str = indent + box_name + " = Box(children=row, layout=box_layout)\n"
                cells_tab_header += box_str
                elm_str += box_name + ","
                substrate_count += 1

                for sub_elm in elm:
                    name_btn = "name_btn"
                    btn_str = indent + name_btn + " = Button(description='" + sub_elm.tag + "', disabled=True, layout=name_button_layout)\n"
                    cells_tab_header += btn_str

                    color_str = indent + name_btn + ".style.button_color = '" + colorname[color_idx] + "'\n"
                    cells_tab_header += color_str

                    name_float = "self.float" + str(float_var_count)
                    float_var_count += 1
                    float_str = indent + name_float + " = FloatText(value='" + sub_elm.text + "', style=style, layout=widget_layout)\n"
                    cells_tab_header += float_str
                    if 'units' in sub_elm.attrib.keys():
                        units_str = sub_elm.attrib['units']
                        # name_units = 'secretion_' + sub_elm.tag + "units" + str(motility_count)
                        # name_units = 'secretion_' + sub_elm.tag + "units" 
                        name_units = 'name_units'
                        btn_str = indent + name_units + " = Button(description='" + units_str + "', disabled=True, layout=units_button_layout)\n"
                        cells_tab_header += btn_str

                        color_str = indent + name_units + ".style.button_color = '" + colorname[color_idx] + "'\n"
                        cells_tab_header += color_str

                    color_idx = 1 - color_idx

                    # motility_row3 = [name_btn, self.motility_migration_bias1 , units_btn]
                    row_str = indent + "row = [" + name_btn + ", " + name_float + ", " +  name_units + "]\n"
                    cells_tab_header += row_str
                    # motility_box3 = Box(children=motility_row3, layout=box_layout)
                    box_name = "box" + str(box_count)
                    box_count += 1
                    box_str = indent + box_name + " = Box(children=row, layout=box_layout)\n"
                    cells_tab_header += box_str
                    elm_str += box_name + ","


    elif child.tag == 'molecular':
        fill_gui_str += indent + "# ---------  molecular  ---------\n"
        elm_str += handle_divider_pheno(prefix + "molecular") + ", "
        # print(elm_str)


  #------------  process <custom_data>  ----------------------------------------

# custom_data_widgets = {"double":"FloatText", "int":"IntText", "bool":"Checkbox", "string":"Text", "divider":""}
# custom_data_type_cast = {"double":"float", "int":"int", "bool":"bool", "string":"", "divider":"Text"}

#   uep_phenotype = cell_def.find('phenotype')
  uep_custom_data = cell_def.find('custom_data')

#   vbox_name = "self.cell_def_vbox%d" % cell_def_count

  cells_tab_header += "\n#      ================== <custom_data>, if present ==================\n"
  param_count = float_var_count + 1

  if uep_custom_data:  # if there are no elements in <custom_data>, we don't show the empty divider 
    print("\n  >>>  parse <custom_data> for " + cell_def.attrib['name'] )
    divider_count += 1
    row_name = "div_row" + str(divider_count)
    cells_tab_header += "\n" + indent + row_name + " = " + "Button(description='Custom Data',disabled=True, layout=divider_button_layout)\n"
    #   cells_tab_header += indent + row_name + ".style.button_color = 'red'\n"
    cells_tab_header += indent + row_name + ".style.button_color = 'cyan'\n"
    #   main_vbox_str += indent2 + row_name + ",\n"
    elm_str += row_name + ","

    #---- create widgets:  name, value (float, bool?, string?), units, description

    for cd in uep_custom_data:   
        # if print_vars:
        if True:
            print(' >> custom_data:  ',cd.tag, cd.attrib)

        w1 = "name_btn"
        cells_tab_header += "\n" + indent + w1 + " = " + "Button(description='" + cd.tag + "', disabled=True, layout=name_button_layout)\n"
        color_str = indent + w1 + ".style.button_color = '" + colorname[color_idx] + "'\n"
        cells_tab_header += color_str
        color_idx = 1 - color_idx

        param_count += 1
        w2 = "self.custom_data" + str(param_count)
        # cells_tab_header += "\n" + indent + full_name + " = " + widgets[child.attrib['type']] + "(\n"
        cells_tab_header += "\n" + indent + w2 + " = FloatText(" 

        # Try to calculate and provide a "good" delta step (for the tiny "up/down" arrows on a numeric widget)
        # if ('type' not in child.attrib.keys()) or child.attrib['type'] == "double":
        # if assume_double or child.attrib['type'] == "double":
        # if child.attrib['type'] == "double":
        #     fval_abs = abs(float(child.text))
        #     if (fval_abs > 0.0):
        #         if (fval_abs > 1.0):  # crop
        #             delta_val = pow(10, int(math.log10(abs(float(child.text)))) - 1)
        #         else:   # round
        #             delta_val = pow(10, round(math.log10(abs(float(child.text)))) - 1)
        #     else:
        #         delta_val = 0.01  # if initial value=0.0, we're totally guessing at what a good delta is
        #     if print_var_types:
        #         print('double: ',float(child.text),', delta_val=',delta_val)

        cells_tab_header += indent2 + "value=" + cd.text + ",\n"

        # if (not divider_flag):
            # We're processing a "normal" row - typically a name, numeric field, units, description
            #  - append the info at the end of this widget
        cells_tab_header += indent2 + "style=style, layout=widget_layout)\n"


        w3 = "units_btn" 
        if 'units' in cd.attrib.keys():
            units_str = cd.attrib['units']
        else:
            units_str = ""
        btn_str = indent + w3 + " = Button(description='" + units_str + "', disabled=True, layout=units_button_layout)\n"
        cells_tab_header += btn_str

        color_str = indent + w3 + ".style.button_color = '" + colorname[color_idx] + "'\n"
        cells_tab_header += color_str
        color_idx = 1 - color_idx


        w4 = "description_btn" 
        if 'description' in cd.attrib.keys():
            description_str = cd.attrib['description']
        else:
            description_str = ""
        btn_str = indent + w4 + " = Button(description='" + description_str + "', disabled=True, layout=desc_button_layout)\n"
        cells_tab_header += btn_str

        color_str = indent + w4 + ".style.button_color = '" + colorname[color_idx] + "'\n"
        cells_tab_header += color_str
        color_idx = 1 - color_idx

        row_name = "row"
        row_str = indent +  row_name + " = [" + w1 + ", " + w2 + ", " +  w3 + ", " + w4 + "] \n"

        # cells_tab_header += "# --------- rwh1"
        cells_tab_header += row_str + "\n"

        box_name = "box" + str(param_count)
        cells_tab_header += indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n"
        # else:  # divider
        #     # box_str += indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n"
        #     cells_tab_header += indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n"

        # cells_tab_header += box_str + "\n"
        elm_str += indent2 + box_name + ",\n"

                # if (not divider_flag):
                #     # float, int, bool
                #     if (type_cast[child.attrib['type']] == "bool"):
                #         fill_gui_str += indent + full_name + ".value = ('true' == (uep.find('.//" + child.tag + "').text.lower()) )\n"
                #     else:
                #         fill_gui_str += indent + full_name + ".value = " + type_cast[child.attrib['type']] + "(uep.find('.//" + child.tag + "').text)\n"

                #     fill_xml_str += indent + "uep.find('.//" + child.tag + "').text = str("+ full_name + ".value)\n"

        #---------------------
        # else: # missing 'type' in child.attrib.keys() --> assume "double"
        #     continue
        #     print("-------- no 'type' attrib in custom_data element")

        #     w1 = "param_name" 
        #     cells_tab_header += "\n" + indent + w1 + " = " + "Button(description='" + child.tag + "', disabled=True, layout=name_button_layout)\n"
        #     if (param_count % 2):
        #         cells_tab_header += indent + w1 + ".style.button_color = '" + colorname1 + "'\n"
        #     else:  # rf.  https://www.w3schools.com/colors/colors_names.asp
        #         cells_tab_header += indent + w1 + ".style.button_color = '" + colorname2 + "'\n"

        #     name_count += 1
        #     full_name = "self.custom_data" + str(name_count)
        #     # cells_tab_header += "\n" + indent + full_name + " = FloatW" + widgets[child.attrib['type']] + "(\n"
        #     # cells_tab_header = indent + full_name + " = FloatText(value='" + rate.text + "',  style=style, layout=widget_layout)\n"
        #     cells_tab_header += indent + full_name + " = FloatText(value='42' , style=style, layout=widget_layout)\n"

        #     if (not divider_flag):
        #         # We're processing a "normal" row - typically a name, numeric field, units, description
        #         #  - append the info at the end of this widget
        #         # cells_tab_header += indent2 + "style=style, layout=widget_layout)\n"

        #         # row_str += indent +  row_name + " = [" + param_name_button + ", " + full_name + ", " +      units_btn_name + ", " + desc_row_name + "] \n"
        #         row_name = "row"
        #         row_str += indent +  row_name + " = [" + w1 + ", " + full_name + ", " +  w3 + ", " + w4 + "] \n"

        #         cells_tab_header += row_str + "\n"

        #         box_name = "box" + str(param_count)
        #         box_str += indent + box_name + " = Box(children=" + row_name + ", layout=box_layout)\n"

  #======================================================================
  #------------  assemble VBox for this cell type
#   if uep_custom_data:  # if there are no elements in <custom_data>, we don't show the empty divider 
  cell_def_count_end = cell_def_count
  vbox_name = "self.cell_def_vbox%d" % cell_def_count
  cell_def_vbox_str = "\n" + indent + vbox_name + " = VBox([\n"
  cell_def_vbox_str += indent2 + elm_str
#   for idx in range(cell_def_count_start,cell_def_count_end+1)
    # cell_def_vbox_str += indent + "])\n"
  cell_def_vbox_str += indent + "])\n"

  if cell_def_count >= 0:  # NOTE: kind of assuming 0th is "default"
    main_vbox_str += vbox_name + ", " 

  cells_tab_header += cell_def_vbox_str
  cells_tab_header += indent + "# ------------------------------------------\n"

#   self.cell_def_vboxes.append(self.cell_def_vbox0)
  cells_tab_header += indent + "self.cell_def_vboxes.append(" + vbox_name + ")\n\n"
  cell_def_count += 1



main_vbox_str += indent + "])"


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
fp.write(main_vbox_str)
fp.write(cell_type_dropdown_cb)
fp.write(display_cell_type_default)
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