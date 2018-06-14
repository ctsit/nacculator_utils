# Automating a NACCulator run
`run_filters.py`

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

# Using Docker
This tool will also run NACCulator all on its own and upload the data.
First it pulls the list of subject status' off the "Finalize data" page,
then, it uses NACCulator filters to clean the data, followed by running 
NACCulator on the data, and finally uploading the output into the NACC
website.
To get started, make sure Docker is installed on your system, or the system
running it.
Build the image like so:
`docker build -f Dockerfile -t nacc_automation:latest ..`
Note: in order to import some libraries from other parts of this repo, the 
Docker build context (..) had to be set one directory back. This allows us 
to utilize the sel.py and config files in the other directory.

To run the image:
docker run --env-file=.env_file -v <your_path>/nacculator_utils/nacc_utils/nacculator_runner/runs:/nacc_utils/runs/ -it nacc_automation:latest /bin/bash
Note: the volume can be whatever directory you want locally, but must be mapped to
/nacc_utils/runs/ inside the container.

Finally, there is .env_file.
This file contains environment variables which will be set inside the container
when it is turned on. Here is an example of what it looks like:
`NACC_USERNAME= <your nacc username>
NACC_PASSWORD= <your nacc password>
NACC_EMAIL=<email used for uploading>
NACC_UPLOAD_PATH=/nacc_utils/new_nacc_upload.txt ---> File being uploaded, keep this!
REDCAP_TOKEN= <your private redcap token>
REDCAP_SERVER=https://redcap.school.edu/redcap/api/
SUBJECT_FILE_PATH=/tmp/subject_status.csv ---> File downloaded from NACC, keep this!
`
