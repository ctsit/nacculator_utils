[![DOI](https://zenodo.org/badge/133712597.svg)](https://zenodo.org/badge/latestdoi/133712597)

# NACCulator Utilities 
This project is a suite of tools and utilities used to help run the 
NACCulator tool. As of this writing, they include a tool to automatically
pull data from REDCap and run the NACCulator filters, automatically 
downloading the list of subjects and their status found on the NACC website,
automatically taking the output of NACCulator and trying to upload it,
and finally parsing a NACC report and sending an email. 

## Getting Started
This project is not really meant to be used as a library just yet,
it mostly functions as a set of scripts or runnable containers. Currently,
there is no setup.py to just install it. 
To get started:
`git clone https://github.com/ctsit/nacculator_utils.git`

## Prerequisites
These tools were built and tested using:
  * python2
  * Docker CE 18.03.1-ce-mac65 (24312)
Please look at the requirements.txt file included for additional requirements.
Also, consider if you need to create a virtual environment for your setup.
The following commands are assuming you are in the top level directory and 
that virtualenv is installed.

`virtualenv venv -p=python2.7`

`source venv bin activate`

`pip install -r requirements.txt`

## Installing
There are seperate README files for the different parts of this project with more specific details.

## Versioning
We use SemVer for versioning. For the versions available, see the tags on this repository.

## Authors
Please look at the AUTHORS list to see the most up-to-date list of authors on
this project

## License
This project is licensed under the APACHE2 License - see the LICENSE file for details
