#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author Kylene Cooley
@brief Calls single instance of data request and processing to obtain the gross range
    and climatology lookup tables for the near-surface instrument frame on the Inshore 
    Surface Mooring of the Coastal Endurance Array. Then script retrieves lookup tables 
    posted to ocean-observatories/qc-lookup and evaluates the difference between online 
    and recalculated suspect ranges.
"""
from ooi_data_explorations.qartod.endurance.qartod_ce_ctdbp import generate_qartod, ANNO_HEADER, CLM_HEADER, GR_HEADER
import os
import requests
import pandas as pd
import re
import io
import ast 

# outline of qartod_ce_ctdbp.main() below and set data stream variables 
#   that are usually set with ooi_data_explorations.common.inputs()

# setup the input arguments
site = 'CE01ISSM'
node = 'SBD17'
sensor = '06-CTDBPC000'
cut_off = '2021-01-01T00:00:00'

refdes = '-'.join([site, node, sensor])

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


# retrieve lookup tables from ocean-observatories/qc-lookup
# functions defined below from Testing.ipynb by Andrew Reed
GITHUB_BASE_URL = "https://raw.githubusercontent.com/oceanobservatories/qc-lookup/master/qartod"

def load_gross_range_qartod_test_values(refdes, stream, ooinet_param):
    """
    Load the gross range QARTOD test from gitHub
    """
    subsite, node, sensor = refdes.split("-", 2)
    sensor_type = sensor[3:8].lower()
    
    # gitHub url to the gross range table
    GROSS_RANGE_URL = f"{GITHUB_BASE_URL}/{sensor_type}/{sensor_type}_qartod_gross_range_test_values.csv"
    
    # Download the results
    download = requests.get(GROSS_RANGE_URL)
    if download.status_code == 200:
        df = pd.read_csv(io.StringIO(download.content.decode('utf-8')))
        df["parameters"] = df["parameters"].apply(ast.literal_eval)
        df["qcConfig"] = df["qcConfig"].apply(ast.literal_eval)
        
    # Next, filter for the desired parameter
    mask = df["parameters"].apply(lambda x: True if x.get("inp") == ooinet_param else False)
    df = df[mask]
    
    # Now filter for the desired stream
    df = df[(df["subsite"] == subsite) & 
            (df["node"] == node) & 
            (df["sensor"] == sensor) &
            (df["stream"] == stream)]
    
    return df

def load_climatology_qartod_test_values(refdes, param):
    """
    Load the OOI climatology qartod test values table from gitHub
    
    Parameters
    ----------
    refdes: str
        The reference designator for the given sensor
    param: str
        The name of the 
    """
    
    site, node, sensor = refdes.split("-", 2)
    sensor_type = sensor[3:8].lower()
    
    # gitHub url to the climatology tables
    CLIMATOLOGY_URL = f"{GITHUB_BASE_URL}/{sensor_type}/climatology_tables/{refdes}-{param}.csv"
    
    # Download the results
    download = requests.get(CLIMATOLOGY_URL)
    if download.status_code == 200:
        df = pd.read_csv(io.StringIO(download.content.decode('utf-8')), index_col=0)
        df = df.applymap(ast.literal_eval)
    else:
        return None
    return df

# load the gross range QARTOD table for a specific parameter
stream = "ctdbp.+"   # in regex .+ is a wildcard that works the same as * in MATLAB
gross_range_qartod_test_values = load_gross_range_qartod_test_values(refdes, stream, "ctdbp_seawater_temperature")
gross_range_qartod_test_values

# Example: load the climatology QARTOD table for a specific parameter
climatology_qartod_test_values = load_climatology_qartod_test_values(refdes, "ctdbp_seawater_temperature")
climatology_qartod_test_values

# calculate difference between published and recalculated values
# gross range difference
# parameter climatologies differences 