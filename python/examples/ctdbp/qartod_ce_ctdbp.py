#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author Kylene Cooley
@brief Calls single instance of data request and processing to obtain the sea water practical 
    salinity climatology lookup table for one node of Coastal Endurance Array.
"""
from ooi_data_explorations.qartod.endurance.qartod_ce_ctdbp import generate_qartod, ANNO_HEADER, CLM_HEADER, GR_HEADER
import os

# outline of qartod_ce_ctdbp.main() below and set data stream variables 
#   that are usually set with ooi_data_explorations.common.inputs()

# setup the input arguments
site = 'CE01ISSM'
node = 'SBD17'
sensor = '06-CTDBPC000'
cut_off = '2021-01-01T00:00:00'

# create the QARTOD gross range and climatology lookup values and tables
annotations, gr_lookup, clm_lookup, clm_table = generate_qartod(site, node, sensor, cut_off)

# save the downloaded annotations and qartod lookups and tables
out_path = os.path.join(os.path.expanduser('~'), 'ooidata/qartod/ctdbp')
out_path = os.path.abspath(out_path)
if not os.path.exists(out_path):
    os.makedirs(out_path)

# save the annotations to a csv file for further processing
anno_csv = '-'.join([site, node, sensor]) + '.quality_annotations.csv'
annotations.to_csv(os.path.join(out_path, anno_csv), index=False, columns=ANNO_HEADER)

# save the gross range values to a csv for further processing
gr_csv = '-'.join([site, node, sensor]) + '.gross_range.csv'
gr_lookup.to_csv(os.path.join(out_path, gr_csv), index=False, columns=GR_HEADER)

# save the climatology values and table to a csv for further processing
clm_csv = '-'.join([site, node, sensor]) + '.climatology.csv'
clm_lookup.to_csv(os.path.join(out_path, clm_csv), index=False, columns=CLM_HEADER)
parameters = ['sea_water_temperature', 'practical_salinity']
for i in range(len(parameters)):
    tbl = '-'.join([site, node, sensor, parameters[i]]) + '.csv'
    with open(os.path.join(out_path, tbl), 'w') as clm:
        clm.write(clm_table[i])
