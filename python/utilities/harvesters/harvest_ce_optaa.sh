#!/usr/bin/env bash
#
# harvest_ce_optaa.sh
#
# Harvest the OPTAA data from all of the OOI Coastal Endurance moorings. Data
# sets include telemetered and recovered host. Data is downloaded from OOI Net
# and reworked to create a cleaner and more consistent set of files named and
# organized by the mooring, mooring sub-location, data delivery method and 
# deployment.
#
# C. Wingard, 2019-07-22 -- Initial code

# set the base directory python command for all subsequent processing
. $(dirname $CONDA_EXE)/../etc/profile.d/conda.sh
conda activate ooi
PYTHON="python -m ooi_data_explorations.uncabled.process_optaa"

### CE01ISSM ###
BASE_FLAGS="-s CE01ISSM -n RID16 -sn 01-OPTAAD000"
BASE_FILE="${HOME}/ooidata/m2m/ce01issm/nsif/optaa/ce01issm.nsif.optaa"
for i in $(seq -f "%02g" 1 18); do
    $PYTHON $BASE_FLAGS -mt telemetered -st optaa_dj_dcl_instrument -dp $i -o "$BASE_FILE.deploy$i.telemetered.optaa_dj_dcl_instrument.nc"
    $PYTHON $BASE_FLAGS -mt recovered_host -st optaa_dj_dcl_instrument_recovered -dp $i -o "$BASE_FILE.deploy$i.recovered_host.optaa_dj_dcl_instrument_recovered.nc"
done

### CE01ISSP ###
BASE_FLAGS="-s CE01ISSP -n SP001 -sn 04-OPTAAJ000"
BASE_FILE="${HOME}/ooidata/m2m/ce01issp/optaa/ce01issp.cspp.optaa"
for i in $(seq -f "%02g" 1 21); do
    $PYTHON $BASE_FLAGS -mt recovered_cspp -st optaa_dj_cspp_instrument_recovered -dp $i -o "$BASE_FILE.deploy$i.recovered_cspp.optaa_dj_cspp_instrument_recovered.nc"
done

### CE02SHSM ###
BASE_FLAGS="-s CE02SHSM -n RID27 -sn 01-OPTAAD000"
BASE_FILE="${HOME}/ooidata/m2m/ce02shsm/nsif/optaa/ce02shsm.nsif.optaa"
for i in $(seq -f "%02g" 1 16); do
    $PYTHON $BASE_FLAGS -mt telemetered -st optaa_dj_dcl_instrument -dp $i -o "$BASE_FILE.deploy$i.telemetered.optaa_dj_dcl_instrument.nc"
    $PYTHON $BASE_FLAGS -mt recovered_host -st optaa_dj_dcl_instrument_recovered -dp $i -o "$BASE_FILE.deploy$i.recovered_host.optaa_dj_dcl_instrument_recovered.nc"
done

### CE02SHSP ###
BASE_FLAGS="-s CE02SHSP -n SP001 -sn 04-OPTAAJ000"
BASE_FILE="${HOME}/ooidata/m2m/ce02shsp/optaa/ce02shsp.cspp.optaa"
for i in $(seq -f "%02g" 1 31); do
    $PYTHON $BASE_FLAGS -mt recovered_cspp -st optaa_dj_cspp_instrument_recovered -dp $i -o "$BASE_FILE.deploy$i.recovered_cspp.optaa_dj_cspp_instrument_recovered.nc"
done

### CE04OSSM ###
BASE_FLAGS="-s CE04OSSM -n RID27 -sn 01-OPTAAD000"
BASE_FILE="${HOME}/ooidata/m2m/ce04ossm/nsif/optaa/ce04ossm.nsif.optaa"
for i in $(seq -f "%02g" 1 15); do
    $PYTHON $BASE_FLAGS -mt telemetered -st optaa_dj_dcl_instrument -dp $i -o "$BASE_FILE.deploy$i.telemetered.optaa_dj_dcl_instrument.nc"
    $PYTHON $BASE_FLAGS -mt recovered_host -st optaa_dj_dcl_instrument_recovered -dp $i -o "$BASE_FILE.deploy$i.recovered_host.optaa_dj_dcl_instrument_recovered.nc"
done

### CE06ISSM ###
BASE_FLAGS="-s CE06ISSM -n RID16 -sn 01-OPTAAD000"
BASE_FILE="${HOME}/ooidata/m2m/ce06issm/nsif/optaa/ce06issm.nsif.optaa"
for i in $(seq -f "%02g" 1 17); do
    $PYTHON $BASE_FLAGS -mt telemetered -st optaa_dj_dcl_instrument -dp $i -o "$BASE_FILE.deploy$i.telemetered.optaa_dj_dcl_instrument.nc"
    $PYTHON $BASE_FLAGS -mt recovered_host -st optaa_dj_dcl_instrument_recovered -dp $i -o "$BASE_FILE.deploy$i.recovered_host.optaa_dj_dcl_instrument_recovered.nc"
done

### CE06ISSP ###
BASE_FLAGS="-s CE06ISSP -n SP001 -sn 04-OPTAAJ000"
BASE_FILE="${HOME}/ooidata/m2m/ce06issp/optaa/ce06issp.cspp.optaa"
for i in $(seq -f "%02g" 1 16); do
    $PYTHON $BASE_FLAGS -mt recovered_cspp -st optaa_dj_cspp_instrument_recovered -dp $i -o "$BASE_FILE.deploy$i.recovered_cspp.optaa_dj_cspp_instrument_recovered.nc"
done

### CE07SHSM ###
BASE_FLAGS="-s CE07SHSM -n RID27 -sn 01-OPTAAD000"
BASE_FILE="${HOME}/ooidata/m2m/ce07shsm/nsif/optaa/ce07shsm.nsif.optaa"
for i in $(seq -f "%02g" 1 16); do
    $PYTHON $BASE_FLAGS -mt telemetered -st optaa_dj_dcl_instrument -dp $i -o "$BASE_FILE.deploy$i.telemetered.optaa_dj_dcl_instrument.nc"
    $PYTHON $BASE_FLAGS -mt recovered_host -st optaa_dj_dcl_instrument_recovered -dp $i -o "$BASE_FILE.deploy$i.recovered_host.optaa_dj_dcl_instrument_recovered.nc"
done

### CE07SHSP ###
BASE_FLAGS="-s CE07SHSP -n SP001 -sn 04-OPTAAJ000"
BASE_FILE="${HOME}/ooidata/m2m/ce07shsp/optaa/ce07shsp.cspp.optaa"
for i in $(seq -f "%02g" 1 14); do
    $PYTHON $BASE_FLAGS -mt recovered_cspp -st optaa_dj_cspp_instrument_recovered -dp $i -o "$BASE_FILE.deploy$i.recovered_cspp.optaa_dj_cspp_instrument_recovered.nc"
done

### CE09OSSM ###
BASE_FLAGS="-s CE09OSSM -n RID27 -sn 01-OPTAAD000"
BASE_FILE="${HOME}/ooidata/m2m/ce09ossm/nsif/optaa/ce09ossm.nsif.optaa"
for i in $(seq -f "%02g" 1 16); do
    $PYTHON $BASE_FLAGS -mt telemetered -st optaa_dj_dcl_instrument -dp $i -o "$BASE_FILE.deploy$i.telemetered.optaa_dj_dcl_instrument.nc"
    $PYTHON $BASE_FLAGS -mt recovered_host -st optaa_dj_dcl_instrument_recovered -dp $i -o "$BASE_FILE.deploy$i.recovered_host.optaa_dj_dcl_instrument_recovered.nc"
done
