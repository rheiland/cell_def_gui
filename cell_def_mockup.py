 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box,Dropdown, Text
    
class CellDefTab(object):

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
        # divider_button_layout={'width':'40%', 'align_items':'left'}
        divider_button_layout={'width':'40%'}

        self.cell_type = Dropdown(
          description='Cell:',
          # options=get_cell_types(),
          options={'default':'default', 'worker':'worker', 'director':'director', 'cargo':'cargo'},
          tooltip='Config File or Previous Run',
        )
        self.cell_type.style = {'description_width': '%sch' % str(len(self.cell_type.description) + 1)}
        # self.cell_type.observe(cell_type_cb, names='value') 


        self.parent_name = Text(
            value='None',
            placeholder='Type something',
            description='Parent:',
            disabled=True
        )

        menv_var1 = Button(description='director_signal', disabled=True, layout=name_button_layout)
        menv_var1.style.button_color = 'tan'

        param_name1 = Button(description='cycle trans rate', disabled=True, layout=name_button_layout)

        self.cycle_trans_rate = FloatText(value=1000,
          step=100,style=style, layout=widget_layout)

        param_name2 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.director_signal_decay_rate = FloatText(value=.1,
          step=0.01,style=style, layout=widget_layout)
        param_name3 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.director_signal_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name4 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.director_signal_Dirichlet_boundary_condition = FloatText(value=1,style=style, layout=widget_layout)
        self.director_signal_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var2 = Button(description='cargo_signal', disabled=True, layout=name_button_layout)
        menv_var2.style.button_color = 'lightgreen'

        param_name5 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.cargo_signal_diffusion_coefficient = FloatText(value=1000,
          step=100,style=style, layout=widget_layout)

        param_name6 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.cargo_signal_decay_rate = FloatText(value=.4,
          step=0.1,style=style, layout=widget_layout)
        param_name7 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.cargo_signal_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name8 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.cargo_signal_Dirichlet_boundary_condition = FloatText(value=1,style=style, layout=widget_layout)
        self.cargo_signal_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)
        self.calculate_gradient = Checkbox(description='calculate_gradients', disabled=False, layout=desc_button_layout)
        self.track_internal = Checkbox(description='track_in_agents', disabled=False, layout=desc_button_layout)




        row_director_signal = [menv_var1,  ] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        """
        box_director_signal = Box(children=row_director_signal, layout=box_layout)
        box1 = Box(children=row1, layout=box_layout)

        box_cargo_signal = Box(children=row_cargo_signal, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        """

        #--------------------------
        div_cycle = Button(description='Phenotype:cycle', disabled=True, layout=divider_button_layout)

        param_name1 = Button(description='transition rate: 0->1', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'tan'

        param_name1_units = Button(description='1/min', disabled=True, layout=units_button_layout) 
        param_name1_units.style.button_color = 'tan'

        self.cycle_trans_rate1 = FloatText(
          value=0.0001,
          step=0.00001,
          style=style, layout=widget_layout)

        row1 = [param_name1, self.cycle_trans_rate1, param_name1_units]
        box1 = Box(children=row1, layout=box_layout)


        param_name2 = Button(description='transition rate: 1->2', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'lightgreen'

        param_name2_units = Button(description='1/min', disabled=True, layout=units_button_layout) 
        param_name2_units.style.button_color = 'lightgreen'

        self.cycle_trans_rate2 = FloatText(
          value=0.0002,
          step=0.00001,
          style=style, layout=widget_layout)

        row2 = [param_name2, self.cycle_trans_rate2, param_name2_units]
        box2 = Box(children=row2, layout=box_layout)

        #--------------------------
        div_death = Button(description='Phenotype:death', disabled=True, layout=divider_button_layout)

        #--------------------------
        div_volume = Button(description='Phenotype:volume', disabled=True, layout=divider_button_layout)

        param_name9 = Button(description='volume', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'tan'

        param_name9_units = Button(description='micron^3', disabled=True, layout=units_button_layout) 
        param_name9_units.style.button_color = 'tan'

        self.volume = FloatText(
          value=2.15e3,
          step=100,
          style=style, layout=widget_layout)

        row9 = [param_name9, self.volume, param_name9_units]
        box9 = Box(children=row9, layout=box_layout)

        #--------------------------
        #--------------------------
        div_mechanics = Button(description='Phenotype:mechanics', disabled=True, layout=divider_button_layout)

        #--------------------------
        div_motility = Button(description='Phenotype:motility', disabled=True, layout=divider_button_layout)

        #--------------------------
        div_secretion = Button(description='Phenotype:secretion', disabled=True, layout=divider_button_layout)

        #--------------------------
        div_intracellular = Button(description='Phenotype:intracellular', disabled=True, layout=divider_button_layout)

        #--------------------------
        div_custom_data = Button(description='Custom data', disabled=True, layout=divider_button_layout)
# <elastic_coefficient length=”1” units=”1/min”>1.0</elastic_coefficient>
# <attachment_point length=”3” units=”micron”>-12.8,13.9,0.0</attachment_point>
        param_name31 = Button(description='elastic_coefficient', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'tan'
        param_name31_units = Button(description='1/min', disabled=True, layout=units_button_layout) 
        param_name31_units.style.button_color = 'tan'
        self.custom_elastic_coef = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)
        row31 = [param_name31, self.custom_elastic_coef, param_name31_units]
        box31 = Box(children=row31, layout=box_layout)

        param_name32 = Button(description='attachment_point', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'lightgreen'
        param_name32_units = Button(description='micron', disabled=True, layout=units_button_layout) 
        param_name32_units.style.button_color = 'lightgreen'
        self.custom_attachment_point = Text(
          value="-12.8,13.9,0.0",
          style=style, layout=widget_layout)
        row32 = [param_name32, self.custom_attachment_point, param_name32_units]
        box32 = Box(children=row32, layout=box_layout)
        #--------------------------

        self.tab = VBox([
          HBox([self.cell_type, self.parent_name]),
          div_cycle,
          box1,
          box2,
          div_death,
          div_volume,
          box9,
          div_mechanics,
          div_motility,
          div_secretion,
          div_intracellular,
          div_custom_data,
          box31,
          box32,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
      return

    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp[0].find('.//diffusion_coefficient').text = str(self.director_signal_diffusion_coefficient.value)
        vp[0].find('.//decay_rate').text = str(self.director_signal_decay_rate.value)
        vp[0].find('.//initial_condition').text = str(self.director_signal_initial_condition.value)
        vp[0].find('.//Dirichlet_boundary_condition').text = str(self.director_signal_Dirichlet_boundary_condition.value)
        vp[0].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.director_signal_Dirichlet_boundary_condition_toggle.value).lower()

        vp[1].find('.//diffusion_coefficient').text = str(self.cargo_signal_diffusion_coefficient.value)
        vp[1].find('.//decay_rate').text = str(self.cargo_signal_decay_rate.value)
        vp[1].find('.//initial_condition').text = str(self.cargo_signal_initial_condition.value)
        vp[1].find('.//Dirichlet_boundary_condition').text = str(self.cargo_signal_Dirichlet_boundary_condition.value)
        vp[1].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.cargo_signal_Dirichlet_boundary_condition_toggle.value).lower()


        uep.find('.//options//calculate_gradients').text = str(self.calculate_gradient.value)
        uep.find('.//options//track_internalized_substrates_in_each_agent').text = str(self.track_internal.value)
