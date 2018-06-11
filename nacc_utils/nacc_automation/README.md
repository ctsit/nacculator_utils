# Using these scripts as a web-api to the NACC Site
In order to help facilitate the day to day tasks required to upload data, 
we have developed some scripts which automatically get and upload data for us.
They rely on selenium and other tools to act like a browser and do the clicking
for us. These scripts are reliable as of 2018-06-07 meaning that the code is in
sync with the current html used to render the NACC website.

There are two automated functions here:
    * upload: This function takes the uploadpath/path from the 
    packet_config_example.ini as well as the NACC credentials 
    and attempts to upload a subject list to the NACC system.
    * getdata: This function uses the NACC credentials to get to the "finalize"
    page in order to grab a copy of the subject list with status. This list
    is used in NACCulator while processing the raw data and filtering records.
    
Note: The code currently requires a plaintext password to be saved in the
env_file. This is a fundamental flaw, and will be addressed in an immediate
update. For now, be as safe as you can with this and please be cautious when
pushing any changed code to a new repo. If the password could have possibly
been leaked, please be sure to change it.

## Running
Note: These should done while inside a virtualenv, or similar.

_Note: Install Chrome Driver to run Selenium on Chrome. Update packet_config.ini_

Install Chrome driver using

    `brew install chromedriver`

Inside the nacc_automation directory:

To Upload a file run

    `python sel.py upload`
To Get current Subjects from Nacc run

    `python sel.py getdata`
Note: This will fail if the "Finalize Data" page is locked or down.

# NACC Report Generation using Docker

This utility will pull the Pre-Certification Reports from NACC, parse the data,
and send an email with a few statistics we are tracking. In a nutshell, it 
reads the PDF, converts it to XML, and then pulls from the XML fields to 
generate an html table email.

## Getting Started

These instructions will help you build a docker image on your local machine from
which you can spawn up and run a container that would automate the process of 
report generation.

First clone the project in your local.

```
git clone -b nacc_docker https://github.com/roukna/nacculator.git
```

### Prerequisites

Update the credentials in the **env_file** file as below. 
Note: The SMTP_PASSWORD field only needs to be provided if authenticating
a specific user account. It is acceptable to use a generic account without
authentication (and right now the code is commented out to authenticate 
anyways).
```bash
vi env_file
```
```bash
USERNAME=nacc_user  # Your NACC username.
PASSWORD=password   # Your NACC password.
SMTP_USER=gator_name  # Your gator username. 
SMTP_PASSWORD=gator_password  # Your gator password.
RECIPIENTS=rouknasengupta@gmail.com,rsengupta@ufl.edu # Email IDs of your recipients.
```

### Building the docker image

```bash
docker build -t nacc_image:latest .
```
Once the image is built, you may save it as a tar file and share it.

```bash
docker save nacc_image:latest | gzip -c > nacc_image.tar.gz
```
For loading the image from tar.gz in another machine:

```bash
gunzip -c nacc_image.tar.gz | docker load
```
or
```bash
docker load < nacc_image.tar.gz
```
Note: repeat uploads creates a new image with the name nacc_image:latest
and gives the previous image a blank name. There might be value in deleting
old images.

gunzip -c nacc_image.tar.gz | docker load
### Run the image
```bash
docker run --env-file=env_file -it nacc_image:latest /bin/bash
```
You need not always use the env_file to pass values for the environment 
variables. You may use the ``docker run -e`` option to pass the values 
from the command line.

## Updating Report
The code used to parse the pdf report is accurate for reports generated
on or before June 2018, an example is in the docs directory. This may change. 
To update the way this tool reads and parses the data, the code can be found in
parse_report.py. The first part of running this generates an out.xml which 
contains the parsed data set. Reading through this file will provide the nested 
locations and indices needed to update or create new fields.
