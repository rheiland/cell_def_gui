 
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
        # self.cell_type_dropdown.observe(self.cell_type_cb)

        self.cell_type_parent_row = HBox([self.cell_type_dropdown, self.parent_name])
        self.cell_type_parent_dict = {}

        self.cell_type_dict = {}
        self.cell_type_dict['default'] = 'default'
        self.cell_type_dict['lung epithelium'] = 'lung epithelium'
        self.cell_type_dict['immune'] = 'immune'
        self.cell_type_dict['CD8 Tcell'] = 'CD8 Tcell'
        self.cell_type_dict['macrophage'] = 'macrophage'
        self.cell_type_dict['neutrophil'] = 'neutrophil'
        self.cell_type_dropdown.options = self.cell_type_dict

        self.cell_type_dropdown.observe(self.cell_type_cb)

        self.cell_type_parent_dict['default'] = 'None'
        self.cell_type_parent_dict['lung epithelium'] = 'default'
        self.cell_type_parent_dict['immune'] = 'default'
        self.cell_type_parent_dict['CD8 Tcell'] = 'immune'
        self.cell_type_parent_dict['macrophage'] = 'immune'
        self.cell_type_parent_dict['neutrophil'] = 'immune'

        div_row1 = Button(description='phenotype:cycle', disabled=True, layout=divider_button_layout)
        div_row2 = Button(description='phenotype:death:apoptosis', disabled=True, layout=divider_button_layout)
        div_row3 = Button(description='phenotype:death:necrosis', disabled=True, layout=divider_button_layout)
        div_row4 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row5 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row6 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row7 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row8 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)

        self.cell_def_vboxes = []
        self.cell_def_vbox0 = VBox([
          div_row1, div_row2, div_row3, div_row4, div_row5, div_row6, div_row7, div_row8,         ])
        self.cell_def_vboxes.append(self.cell_def_vbox0)

        div_row9 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row10 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)

        self.cell_def_vbox1 = VBox([
          div_row9, div_row10,         ])
        self.cell_def_vboxes.append(self.cell_def_vbox1)

        div_row11 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row12 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)

        self.cell_def_vbox2 = VBox([
          div_row11, div_row12,         ])
        self.cell_def_vboxes.append(self.cell_def_vbox2)

        div_row13 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row14 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)

        self.cell_def_vbox3 = VBox([
          div_row13, div_row14,         ])
        self.cell_def_vboxes.append(self.cell_def_vbox3)

        div_row15 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row16 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)

        self.cell_def_vbox4 = VBox([
          div_row15, div_row16,         ])
        self.cell_def_vboxes.append(self.cell_def_vbox4)

        div_row17 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row18 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)

        self.cell_def_vbox5 = VBox([
          div_row17, div_row18,         ])
        self.cell_def_vboxes.append(self.cell_def_vbox5)





        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')

        self.tab = VBox([
          self.cell_type_parent_row, 
self.cell_def_vbox0, self.cell_def_vbox1, self.cell_def_vbox2, self.cell_def_vbox3, self.cell_def_vbox4, self.cell_def_vbox5,         ])
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


    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//cell_definitions')  # find unique entry point


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//cell_definitions')  # find unique entry point
