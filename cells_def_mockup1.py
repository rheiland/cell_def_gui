 
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


        self.cell_def_vboxes = []
        div_row1 = Button(description='phenotype:cycle', disabled=True, layout=divider_button_layout)
        div_row1.style.button_color = 'orange'
        cycle_rate_btn0 = Button(description='transition rate: 0->1', disabled=True, layout=name_button_layout)
        cycle_rate_btn0.style.button_color = 'lightgreen'
        self.cycle_rate_float0 = FloatText(value='0',  style=style, layout=widget_layout)
        units_btn0 = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn0.style.button_color = 'lightgreen'
        row0 = [cycle_rate_btn0, self.cycle_rate_float0, units_btn0]
        box0 = Box(children=row0, layout=box_layout)

        cycle_rate_btn1 = Button(description='transition rate: 1->2', disabled=True, layout=name_button_layout)
        cycle_rate_btn1.style.button_color = 'tan'
        self.cycle_rate_float1 = FloatText(value='0.00208333',  style=style, layout=widget_layout)
        units_btn1 = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn1.style.button_color = 'tan'
        row1 = [cycle_rate_btn1, self.cycle_rate_float1, units_btn1]
        box1 = Box(children=row1, layout=box_layout)

        cycle_rate_btn2 = Button(description='transition rate: 2->3', disabled=True, layout=name_button_layout)
        cycle_rate_btn2.style.button_color = 'lightgreen'
        self.cycle_rate_float2 = FloatText(value='0.00416667',  style=style, layout=widget_layout)
        units_btn2 = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn2.style.button_color = 'lightgreen'
        row2 = [cycle_rate_btn2, self.cycle_rate_float2, units_btn2]
        box2 = Box(children=row2, layout=box_layout)

        cycle_rate_btn3 = Button(description='transition rate: 3->0', disabled=True, layout=name_button_layout)
        cycle_rate_btn3.style.button_color = 'tan'
        self.cycle_rate_float3 = FloatText(value='0.0166667',  style=style, layout=widget_layout)
        units_btn3 = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn3.style.button_color = 'tan'
        row3 = [cycle_rate_btn3, self.cycle_rate_float3, units_btn3]
        box3 = Box(children=row3, layout=box_layout)

        div_row2 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row2.style.button_color = 'orange'
        death_model0 = Button(description='apoptosis', disabled=True, layout={'width':'30%'})
        name_btn = Button(description='rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.cell_definition_death_model_100_rate = FloatText(value='0',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row4 = [name_btn, self.cell_definition_death_model_100_rate, units_btn]
        box4 = Box(children=row4, layout=box_layout)

        self.cell_definition_death_model_100_trate01_toggle = Checkbox(description='fixed_duration', value=True,layout=name_button_layout)
        cycle_rate_btn4 = Button(description='transition rate: 0->1', disabled=True, layout=name_button_layout)
        cycle_rate_btn4.style.button_color = 'tan'
        self.cycle_rate_float4 = FloatText(value='0.00193798',  style=style, layout=widget_layout)
        units_btn4 = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn4.style.button_color = 'tan'
        row4 = [self.cell_definition_death_model_100_trate01_toggle, cycle_rate_btn4, self.cycle_rate_float4, units_btn4]
        box5 = Box(children=row4, layout=box_layout)

        unlysed_fluid_change_rate_apoptosis = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        unlysed_fluid_change_rate_apoptosis.style.button_color = 'lightgreen'
        self.unlysed_fluid_change_rate_apoptosis_float = FloatText(value='0.05',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [unlysed_fluid_change_rate_apoptosis, self.unlysed_fluid_change_rate_apoptosis_float, units_btn]
        box6 = Box(children=row, layout=box_layout)

        lysed_fluid_change_rate_apoptosis = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        lysed_fluid_change_rate_apoptosis.style.button_color = 'tan'
        self.lysed_fluid_change_rate_apoptosis_float = FloatText(value='0',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'tan'
        row = [lysed_fluid_change_rate_apoptosis, self.lysed_fluid_change_rate_apoptosis_float, units_btn]
        box7 = Box(children=row, layout=box_layout)

        cytoplasmic_biomass_change_rate_apoptosis = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        cytoplasmic_biomass_change_rate_apoptosis.style.button_color = 'lightgreen'
        self.cytoplasmic_biomass_change_rate_apoptosis_float = FloatText(value='1.66667e-02',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [cytoplasmic_biomass_change_rate_apoptosis, self.cytoplasmic_biomass_change_rate_apoptosis_float, units_btn]
        box8 = Box(children=row, layout=box_layout)

        nuclear_biomass_change_rate_apoptosis = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        nuclear_biomass_change_rate_apoptosis.style.button_color = 'tan'
        self.nuclear_biomass_change_rate_apoptosis_float = FloatText(value='5.83333e-03',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'tan'
        row = [nuclear_biomass_change_rate_apoptosis, self.nuclear_biomass_change_rate_apoptosis_float, units_btn]
        box9 = Box(children=row, layout=box_layout)

        calcification_rate_apoptosis = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        calcification_rate_apoptosis.style.button_color = 'lightgreen'
        self.calcification_rate_apoptosis_float = FloatText(value='0',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [calcification_rate_apoptosis, self.calcification_rate_apoptosis_float, units_btn]
        box10 = Box(children=row, layout=box_layout)

        relative_rupture_volume_apoptosis = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        relative_rupture_volume_apoptosis.style.button_color = 'tan'
        self.relative_rupture_volume_apoptosis_float = FloatText(value='2.0',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'tan'
        row = [relative_rupture_volume_apoptosis, self.relative_rupture_volume_apoptosis_float, units_btn]
        box11 = Box(children=row, layout=box_layout)

        death_model1 = Button(description='necrosis', disabled=True, layout={'width':'30%'})
        name_btn = Button(description='rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.cell_definition_death_model_101_rate = FloatText(value='0.0',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row4 = [name_btn, self.cell_definition_death_model_101_rate, units_btn]
        box12 = Box(children=row4, layout=box_layout)

        self.cell_definition_death_model_101_trate01_toggle = Checkbox(description='fixed_duration', value=False,layout=name_button_layout)
        cycle_rate_btn4 = Button(description='transition rate: 0->1', disabled=True, layout=name_button_layout)
        cycle_rate_btn4.style.button_color = 'tan'
        self.cycle_rate_float4 = FloatText(value='9e9',  style=style, layout=widget_layout)
        units_btn4 = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn4.style.button_color = 'tan'
        row4 = [self.cell_definition_death_model_101_trate01_toggle, cycle_rate_btn4, self.cycle_rate_float4, units_btn4]
        box13 = Box(children=row4, layout=box_layout)

        self.cell_definition_death_model_101_trate12_toggle = Checkbox(description='fixed_duration', value=True,layout=name_button_layout)
        cycle_rate_btn4 = Button(description='transition rate: 1->2', disabled=True, layout=name_button_layout)
        cycle_rate_btn4.style.button_color = 'lightgreen'
        self.cycle_rate_float4 = FloatText(value='1.15741e-5',  style=style, layout=widget_layout)
        units_btn4 = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn4.style.button_color = 'lightgreen'
        row4 = [self.cell_definition_death_model_101_trate12_toggle, cycle_rate_btn4, self.cycle_rate_float4, units_btn4]
        box14 = Box(children=row4, layout=box_layout)

        unlysed_fluid_change_rate_necrosis = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        unlysed_fluid_change_rate_necrosis.style.button_color = 'tan'
        self.unlysed_fluid_change_rate_necrosis_float = FloatText(value='0.05',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'tan'
        row = [unlysed_fluid_change_rate_necrosis, self.unlysed_fluid_change_rate_necrosis_float, units_btn]
        box15 = Box(children=row, layout=box_layout)

        lysed_fluid_change_rate_necrosis = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        lysed_fluid_change_rate_necrosis.style.button_color = 'lightgreen'
        self.lysed_fluid_change_rate_necrosis_float = FloatText(value='0',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [lysed_fluid_change_rate_necrosis, self.lysed_fluid_change_rate_necrosis_float, units_btn]
        box16 = Box(children=row, layout=box_layout)

        cytoplasmic_biomass_change_rate_necrosis = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        cytoplasmic_biomass_change_rate_necrosis.style.button_color = 'tan'
        self.cytoplasmic_biomass_change_rate_necrosis_float = FloatText(value='1.66667e-02',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'tan'
        row = [cytoplasmic_biomass_change_rate_necrosis, self.cytoplasmic_biomass_change_rate_necrosis_float, units_btn]
        box17 = Box(children=row, layout=box_layout)

        nuclear_biomass_change_rate_necrosis = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        nuclear_biomass_change_rate_necrosis.style.button_color = 'lightgreen'
        self.nuclear_biomass_change_rate_necrosis_float = FloatText(value='5.83333e-03',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [nuclear_biomass_change_rate_necrosis, self.nuclear_biomass_change_rate_necrosis_float, units_btn]
        box18 = Box(children=row, layout=box_layout)

        calcification_rate_necrosis = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        calcification_rate_necrosis.style.button_color = 'tan'
        self.calcification_rate_necrosis_float = FloatText(value='0',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'tan'
        row = [calcification_rate_necrosis, self.calcification_rate_necrosis_float, units_btn]
        box19 = Box(children=row, layout=box_layout)

        relative_rupture_volume_necrosis = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        relative_rupture_volume_necrosis.style.button_color = 'lightgreen'
        self.relative_rupture_volume_necrosis_float = FloatText(value='2.0',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [relative_rupture_volume_necrosis, self.relative_rupture_volume_necrosis_float, units_btn]
        box20 = Box(children=row, layout=box_layout)

        div_row3 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row3.style.button_color = 'orange'
        volume_total = Button(description='total', disabled=True, layout=name_button_layout)
        volume_total.style.button_color = 'tan'
        self.volume_total_float = FloatText(value='2494',  style=style, layout=widget_layout)
        units_btn = Button(description='micron^3', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'tan'
        row = [volume_total, self.volume_total_float, units_btn]
        box21 = Box(children=row, layout=box_layout)

        volume_fluid_fraction = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        volume_fluid_fraction.style.button_color = 'lightgreen'
        self.volume_fluid_fraction_float = FloatText(value='0.75',  style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [volume_fluid_fraction, self.volume_fluid_fraction_float, units_btn]
        box22 = Box(children=row, layout=box_layout)

        volume_nuclear = Button(description='nuclear', disabled=True, layout=name_button_layout)
        volume_nuclear.style.button_color = 'tan'
        self.volume_nuclear_float = FloatText(value='540',  style=style, layout=widget_layout)
        units_btn = Button(description='micron^3', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'tan'
        row = [volume_nuclear, self.volume_nuclear_float, units_btn]
        box23 = Box(children=row, layout=box_layout)

        volume_fluid_change_rate = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        volume_fluid_change_rate.style.button_color = 'lightgreen'
        self.volume_fluid_change_rate_float = FloatText(value='0.05',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [volume_fluid_change_rate, self.volume_fluid_change_rate_float, units_btn]
        box24 = Box(children=row, layout=box_layout)

        volume_cytoplasmic_biomass_change_rate = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        volume_cytoplasmic_biomass_change_rate.style.button_color = 'tan'
        self.volume_cytoplasmic_biomass_change_rate_float = FloatText(value='0.0045',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'tan'
        row = [volume_cytoplasmic_biomass_change_rate, self.volume_cytoplasmic_biomass_change_rate_float, units_btn]
        box25 = Box(children=row, layout=box_layout)

        volume_nuclear_biomass_change_rate = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        volume_nuclear_biomass_change_rate.style.button_color = 'lightgreen'
        self.volume_nuclear_biomass_change_rate_float = FloatText(value='0.0055',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [volume_nuclear_biomass_change_rate, self.volume_nuclear_biomass_change_rate_float, units_btn]
        box26 = Box(children=row, layout=box_layout)

        volume_calcified_fraction = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        volume_calcified_fraction.style.button_color = 'tan'
        self.volume_calcified_fraction_float = FloatText(value='0',  style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'tan'
        row = [volume_calcified_fraction, self.volume_calcified_fraction_float, units_btn]
        box27 = Box(children=row, layout=box_layout)

        volume_calcification_rate = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        volume_calcification_rate.style.button_color = 'lightgreen'
        self.volume_calcification_rate_float = FloatText(value='0',  style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [volume_calcification_rate, self.volume_calcification_rate_float, units_btn]
        box28 = Box(children=row, layout=box_layout)

        volume_relative_rupture_volume = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        volume_relative_rupture_volume.style.button_color = 'tan'
        self.volume_relative_rupture_volume_float = FloatText(value='2.0',  style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'tan'
        row = [volume_relative_rupture_volume, self.volume_relative_rupture_volume_float, units_btn]
        box29 = Box(children=row, layout=box_layout)

        div_row4 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row4.style.button_color = 'orange'
        mechanics_cell_cell_adhesion_strength = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        mechanics_cell_cell_adhesion_strength.style.button_color = 'lightgreen'
        self.mechanics_cell_cell_adhesion_strength_float = FloatText(value='0.4',  style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [mechanics_cell_cell_adhesion_strength, self.mechanics_cell_cell_adhesion_strength_float, units_btn]
        box30 = Box(children=row, layout=box_layout)

        mechanics_cell_cell_repulsion_strength = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        mechanics_cell_cell_repulsion_strength.style.button_color = 'tan'
        self.mechanics_cell_cell_repulsion_strength_float = FloatText(value='10.0',  style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'tan'
        row = [mechanics_cell_cell_repulsion_strength, self.mechanics_cell_cell_repulsion_strength_float, units_btn]
        box31 = Box(children=row, layout=box_layout)

        mechanics_relative_maximum_adhesion_distance = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        mechanics_relative_maximum_adhesion_distance.style.button_color = 'lightgreen'
        self.mechanics_relative_maximum_adhesion_distance_float = FloatText(value='1.25',  style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [mechanics_relative_maximum_adhesion_distance, self.mechanics_relative_maximum_adhesion_distance_float, units_btn]
        box32 = Box(children=row, layout=box_layout)

        self.mechanics_set_relative_equilibrium_distance_toggle = Checkbox(description='enabled', value=False,layout=name_button_layout)
        mechanics_set_relative_equilibrium_distance = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        mechanics_set_relative_equilibrium_distance.style.button_color = 'tan'
        self.mechanics_set_relative_equilibrium_distance_float = FloatText(value='1.8',  style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.mechanics_set_relative_equilibrium_distance_toggle, mechanics_set_relative_equilibrium_distance, self.mechanics_set_relative_equilibrium_distance_float, units_btn]
        box33 = Box(children=row, layout=box_layout)

        self.mechanics_set_absolute_equilibrium_distance_toggle = Checkbox(description='enabled', value=False,layout=name_button_layout)
        mechanics_set_absolute_equilibrium_distance = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        mechanics_set_absolute_equilibrium_distance.style.button_color = 'lightgreen'
        self.mechanics_set_absolute_equilibrium_distance_float = FloatText(value='15.12',  style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=units_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.mechanics_set_absolute_equilibrium_distance_toggle, mechanics_set_absolute_equilibrium_distance, self.mechanics_set_absolute_equilibrium_distance_float, units_btn]
        box34 = Box(children=row, layout=box_layout)

        div_row5 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row5.style.button_color = 'orange'

        motility_speedname1 = Button(description='speed', disabled=True, layout=name_button_layout)
        motility_speedname1.style.button_color = 'tan'
        self.motility_speed1 = FloatText(value='1', style=style, layout=widget_layout)
        motility_speedunits1 = Button(description='micron/min', disabled=True, layout=units_button_layout)
        motility_speedunits1.style.button_color = 'tan'
        row = [motility_speedname1, self.motility_speed1, motility_speedunits1]
        box35 = Box(children=row, layout=box_layout)

        motility_persistence_timename1 = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        motility_persistence_timename1.style.button_color = 'lightgreen'
        self.motility_persistence_time1 = FloatText(value='1', style=style, layout=widget_layout)
        motility_persistence_timeunits1 = Button(description='min', disabled=True, layout=units_button_layout)
        motility_persistence_timeunits1.style.button_color = 'lightgreen'
        row = [motility_persistence_timename1, self.motility_persistence_time1, motility_persistence_timeunits1]
        box36 = Box(children=row, layout=box_layout)

        motility_migration_biasname1 = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        motility_migration_biasname1.style.button_color = 'tan'
        self.motility_migration_bias1 = FloatText(value='.5', style=style, layout=widget_layout)
        motility_migration_biasunits1 = Button(description='dimensionless', disabled=True, layout=units_button_layout)
        motility_migration_biasunits1.style.button_color = 'tan'
        row = [motility_migration_biasname1, self.motility_migration_bias1, motility_migration_biasunits1]
        box37 = Box(children=row, layout=box_layout)
        self.options_enabled1 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        self.options_use_2D1 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})

        self.options_chemotaxis1 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        chemotaxis_substrate1 = Button(description='substrate', disabled=True, layout=name_button_layout)
        chemotaxis_substrate1.style.button_color = 'lightgreen'
        self.chemotaxis_substrate1 = Text(value='chemokine', style=style, layout=widget_layout)
        row = [chemotaxis_substrate1, self.chemotaxis_substrate1]
        box38 = Box(children=row, layout=box_layout)

        chemotaxis_direction1 = Button(description='direction', disabled=True, layout=name_button_layout)
        chemotaxis_direction1.style.button_color = 'tan'
        self.chemotaxis_direction1 = Text(value='1', style=style, layout=widget_layout)
        row = [chemotaxis_direction1, self.chemotaxis_direction1]
        box39 = Box(children=row, layout=box_layout)
        div_row6 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row6.style.button_color = 'orange'
        div_row7 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row7.style.button_color = 'orange'

        self.cell_def_vbox0 = VBox([
          div_row1, box0, box1, box2, box3, div_row2, death_model0,box4, box5, box6, box7, box8, box9, box10, box11, death_model1,box12, box13, box14, box15, box16, box17, box18, box19, box20, div_row3, box21, box22, box23, box24, box25, box26, box27, box28, box29, div_row4, box30, box31, box32, box33, box34, div_row5, box35,box36,box37,self.options_enabled1,self.options_use_2D1,chemotaxis_btn,self.options_chemotaxis1,box38,box39,div_row6, div_row7,         ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox0)

        div_row8 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row8.style.button_color = 'orange'
        self.options_enabled2 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        div_row9 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row9.style.button_color = 'orange'

        self.cell_def_vbox1 = VBox([
          div_row8, self.options_enabled2,div_row9,         ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox1)

        div_row10 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row10.style.button_color = 'orange'

        motility_speedname3 = Button(description='speed', disabled=True, layout=name_button_layout)
        motility_speedname3.style.button_color = 'lightgreen'
        self.motility_speed3 = FloatText(value='4', style=style, layout=widget_layout)
        motility_speedunits3 = Button(description='micron/min', disabled=True, layout=units_button_layout)
        motility_speedunits3.style.button_color = 'lightgreen'
        row = [motility_speedname3, self.motility_speed3, motility_speedunits3]
        box40 = Box(children=row, layout=box_layout)

        motility_persistence_timename3 = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        motility_persistence_timename3.style.button_color = 'tan'
        self.motility_persistence_time3 = FloatText(value='1', style=style, layout=widget_layout)
        motility_persistence_timeunits3 = Button(description='min', disabled=True, layout=units_button_layout)
        motility_persistence_timeunits3.style.button_color = 'tan'
        row = [motility_persistence_timename3, self.motility_persistence_time3, motility_persistence_timeunits3]
        box41 = Box(children=row, layout=box_layout)

        motility_migration_biasname3 = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        motility_migration_biasname3.style.button_color = 'lightgreen'
        self.motility_migration_bias3 = FloatText(value='0.5', style=style, layout=widget_layout)
        motility_migration_biasunits3 = Button(description='dimensionless', disabled=True, layout=units_button_layout)
        motility_migration_biasunits3.style.button_color = 'lightgreen'
        row = [motility_migration_biasname3, self.motility_migration_bias3, motility_migration_biasunits3]
        box42 = Box(children=row, layout=box_layout)
        self.options_enabled3 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.options_use_2D3 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})

        self.options_chemotaxis3 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        chemotaxis_substrate3 = Button(description='substrate', disabled=True, layout=name_button_layout)
        chemotaxis_substrate3.style.button_color = 'tan'
        self.chemotaxis_substrate3 = Text(value='chemokine', style=style, layout=widget_layout)
        row = [chemotaxis_substrate3, self.chemotaxis_substrate3]
        box43 = Box(children=row, layout=box_layout)

        chemotaxis_direction3 = Button(description='direction', disabled=True, layout=name_button_layout)
        chemotaxis_direction3.style.button_color = 'lightgreen'
        self.chemotaxis_direction3 = Text(value='1', style=style, layout=widget_layout)
        row = [chemotaxis_direction3, self.chemotaxis_direction3]
        box44 = Box(children=row, layout=box_layout)
        div_row11 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row11.style.button_color = 'orange'
        secretion_substrate_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        secretion_substrate_btn.style.button_color = 'tan'
        self.secretion_substrate0 = Text(value='pro-inflammatory cytokine', style=style, layout=widget_layout)
        row = [secretion_substrate_btn, self.secretion_substrate0]
        box45 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.secretion_secretion_rate = FloatText(value='10', style=style, layout=widget_layout)
        name_units = Button(description='1/min', disabled=True, layout=units_button_layout)
        name_units.style.button_color = 'lightgreen'
        row = [name_btn, self.secretion_secretion_rate, name_units]
        box46 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.secretion_secretion_target = FloatText(value='1', style=style, layout=widget_layout)
        name_units = Button(description='substrate density', disabled=True, layout=units_button_layout)
        name_units.style.button_color = 'tan'
        row = [name_btn, self.secretion_secretion_target, name_units]
        box47 = Box(children=row, layout=box_layout)

        self.cell_def_vbox2 = VBox([
          div_row10, box40,box41,box42,self.options_enabled3,self.options_use_2D3,chemotaxis_btn,self.options_chemotaxis3,box43,box44,div_row11, box45,box46,box47,        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox2)

        div_row12 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row12.style.button_color = 'orange'
        div_row13 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row13.style.button_color = 'orange'

        self.cell_def_vbox3 = VBox([
          div_row12, div_row13,         ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox3)

        div_row14 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row14.style.button_color = 'orange'
        div_row15 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row15.style.button_color = 'orange'

        self.cell_def_vbox4 = VBox([
          div_row14, div_row15,         ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox4)

        div_row16 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row16.style.button_color = 'orange'
        div_row17 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row17.style.button_color = 'orange'
        secretion_substrate_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        secretion_substrate_btn.style.button_color = 'lightgreen'
        self.secretion_substrate0 = Text(value='virion', style=style, layout=widget_layout)
        row = [secretion_substrate_btn, self.secretion_substrate0]
        box48 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.secretion_uptake_rate = FloatText(value='1', style=style, layout=widget_layout)
        name_units = Button(description='1/min', disabled=True, layout=units_button_layout)
        name_units.style.button_color = 'tan'
        row = [name_btn, self.secretion_uptake_rate, name_units]
        box49 = Box(children=row, layout=box_layout)

        self.cell_def_vbox5 = VBox([
          div_row16, div_row17, box48,box49,        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox5)



        row = [name_btn, self.secretion_uptake_rate, name_units]
        box49 = Box(children=row, layout=box_layout)

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

        uep = xml_root.find('.//cell_definitions')  # find unique entry point
        uep = xml_root.find('.//cell_definition')  # find unique entry point
        uep = xml_root.find('.//cell_definitions')  # find unique entry point
#        self.cycle_rate_float0.value = float(uep.find('.//cycle').text)
#        self.cycle_rate_float1.value = float(uep.find('.//cycle').text)
#        self.cycle_rate_float2.value = float(uep.find('.//cycle').text)
#        self.cycle_rate_float3.value = float(uep.find('.//cycle').text)
#        self.cell_definition_death_model_100_rate.value = float(uep.find('.//death').text)
#        self.cycle_rate_float4.value = float(uep.find('.//death').text)
#        self.unlysed_fluid_change_rate_apoptosis_float.value = float(uep.find('.//death').text)
#        self.lysed_fluid_change_rate_apoptosis_float.value = float(uep.find('.//death').text)
#        self.cytoplasmic_biomass_change_rate_apoptosis_float.value = float(uep.find('.//death').text)
#        self.nuclear_biomass_change_rate_apoptosis_float.value = float(uep.find('.//death').text)
#        self.calcification_rate_apoptosis_float.value = float(uep.find('.//death').text)
#        self.relative_rupture_volume_apoptosis_float.value = float(uep.find('.//death').text)
#        self.cell_definition_death_model_101_rate.value = float(uep.find('.//death').text)
#        self.cycle_rate_float4.value = float(uep.find('.//death').text)
#        self.cycle_rate_float4.value = float(uep.find('.//death').text)
#        self.unlysed_fluid_change_rate_necrosis_float.value = float(uep.find('.//death').text)
#        self.lysed_fluid_change_rate_necrosis_float.value = float(uep.find('.//death').text)
#        self.cytoplasmic_biomass_change_rate_necrosis_float.value = float(uep.find('.//death').text)
#        self.nuclear_biomass_change_rate_necrosis_float.value = float(uep.find('.//death').text)
#        self.calcification_rate_necrosis_float.value = float(uep.find('.//death').text)
#        self.relative_rupture_volume_necrosis_float.value = float(uep.find('.//death').text)
#        self.volume_total_float.value = float(uep.find('.//volume').text)
#        self.volume_fluid_fraction_float.value = float(uep.find('.//volume').text)
#        self.volume_nuclear_float.value = float(uep.find('.//volume').text)
#        self.volume_fluid_change_rate_float.value = float(uep.find('.//volume').text)
#        self.volume_cytoplasmic_biomass_change_rate_float.value = float(uep.find('.//volume').text)
#        self.volume_nuclear_biomass_change_rate_float.value = float(uep.find('.//volume').text)
#        self.volume_calcified_fraction_float.value = float(uep.find('.//volume').text)
#        self.volume_calcification_rate_float.value = float(uep.find('.//volume').text)
#        self.volume_relative_rupture_volume_float.value = float(uep.find('.//volume').text)
#        self.mechanics_cell_cell_adhesion_strength_float.value = float(uep.find('.//mechanics').text)
#        self.mechanics_cell_cell_repulsion_strength_float.value = float(uep.find('.//mechanics').text)
#        self.mechanics_relative_maximum_adhesion_distance_float.value = float(uep.find('.//mechanics').text)
#        self.mechanics_set_relative_equilibrium_distance_float.value = float(uep.find('.//mechanics').text)
#        self.mechanics_set_absolute_equilibrium_distance_float.value = float(uep.find('.//mechanics').text)
        uep = xml_root.find('.//cell_definitions')  # find unique entry point
        uep = xml_root.find('.//cell_definitions')  # find unique entry point
        uep = xml_root.find('.//cell_definitions')  # find unique entry point
        uep = xml_root.find('.//cell_definitions')  # find unique entry point
        uep = xml_root.find('.//cell_definitions')  # find unique entry point


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):

        uep = xml_root.find('.//cell_definitions')  # find unique entry point
        uep = xml_root.find('.//cell_definition')  # find unique entry point
#        uep.find('.//cycle').text = str(self.cycle_rate_float0.value)
#        uep.find('.//cycle').text = str(self.cycle_rate_float1.value)
#        uep.find('.//cycle').text = str(self.cycle_rate_float2.value)
#        uep.find('.//cycle').text = str(self.cycle_rate_float3.value)
#        uep.find('.//death').text = str(self.cell_definition_death_model_100_rate.value)
#        uep.find('.//death').text = str(self.cycle_rate_float4.value)
#        uep.find('.//death').text = str(self.unlysed_fluid_change_rate_apoptosis_float.value)
#        uep.find('.//death').text = str(self.lysed_fluid_change_rate_apoptosis_float.value)
#        uep.find('.//death').text = str(self.cytoplasmic_biomass_change_rate_apoptosis_float.value)
#        uep.find('.//death').text = str(self.nuclear_biomass_change_rate_apoptosis_float.value)
#        uep.find('.//death').text = str(self.calcification_rate_apoptosis_float.value)
#        uep.find('.//death').text = str(self.relative_rupture_volume_apoptosis_float.value)
#        uep.find('.//death').text = str(self.cell_definition_death_model_101_rate.value)
#        uep.find('.//death').text = str(self.cycle_rate_float4.value)
#        uep.find('.//death').text = str(self.cycle_rate_float4.value)
#        uep.find('.//death').text = str(self.unlysed_fluid_change_rate_necrosis_float.value)
#        uep.find('.//death').text = str(self.lysed_fluid_change_rate_necrosis_float.value)
#        uep.find('.//death').text = str(self.cytoplasmic_biomass_change_rate_necrosis_float.value)
#        uep.find('.//death').text = str(self.nuclear_biomass_change_rate_necrosis_float.value)
#        uep.find('.//death').text = str(self.calcification_rate_necrosis_float.value)
#        uep.find('.//death').text = str(self.relative_rupture_volume_necrosis_float.value)
#        uep.find('.//volume').text = str(self.volume_total_float.value)
#        uep.find('.//volume').text = str(self.volume_fluid_fraction_float.value)
#        uep.find('.//volume').text = str(self.volume_nuclear_float.value)
#        uep.find('.//volume').text = str(self.volume_fluid_change_rate_float.value)
#        uep.find('.//volume').text = str(self.volume_cytoplasmic_biomass_change_rate_float.value)
#        uep.find('.//volume').text = str(self.volume_nuclear_biomass_change_rate_float.value)
#        uep.find('.//volume').text = str(self.volume_calcified_fraction_float.value)
#        uep.find('.//volume').text = str(self.volume_calcification_rate_float.value)
#        uep.find('.//volume').text = str(self.volume_relative_rupture_volume_float.value)
#        uep.find('.//mechanics').text = str(self.mechanics_cell_cell_adhesion_strength_float.value)
#        uep.find('.//mechanics').text = str(self.mechanics_cell_cell_repulsion_strength_float.value)
#        uep.find('.//mechanics').text = str(self.mechanics_relative_maximum_adhesion_distance_float.value)
#        uep.find('.//mechanics').text = str(self.mechanics_set_relative_equilibrium_distance_float.value)
#        uep.find('.//mechanics').text = str(self.mechanics_set_absolute_equilibrium_distance_float.value)
