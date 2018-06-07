# Automating a NACCulator run
This python script is a convenience tool used to automate grabbing
a dataset from a REDCap instance and running the data through NACCulator's 
filters in preparation for actually running NACCulator on the data. 
The script will take the raw data, and save each intermediate steps data
as it translates the data.

## Prerequisites
This script assumes it is being run in an environment where NACCulator and
Cappy have been installed. These can both be found in the CTSIT github repos.
Also, the requirements.txt will install them.

These scripts also require the nacculator_cfg.ini to be set up properly.
### cappy
These are the settings used to pull data from REDCap
token: REDCap token that has rights to download data from the project
redcap_server: URL to the REDCap server api
### filters
Each section in filters corresponds to a filter function found in filters.py
of NACCulator. For more details, please refer to NACCulator's README.

## Running

Run the script, passing it the config file as an arg.
`python run_filters.py nacculator_cfg.ini`

