#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author Kylene Cooley
@brief Calls single instance of data request and processing to obtain gross range and 
    climatology lookup tables for one node of Coastal Endurance Array.
"""
import ooi_data_explorations.qartod.endurance.qartod_ce_ctdbp as qartod_ce


qartod_ce.main(['-s', 'CE01ISSM', '-n', 'SBD17', '-sn', '06-CTDBPC000', '-co', '2021-01-01T00:00:00'])