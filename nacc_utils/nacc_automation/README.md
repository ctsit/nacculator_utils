HOW TO GET CURRENT_DB.CSV OR UPLOAD DATA TO NACC
------------------------------------------------

_Note: Install Chrome Driver to run Selenium on Chrome. Update packet_config.ini_

Install Chrome driver using

    $ brew install chromedriver
Go to get_current_data folder and you can either upload a file or get current subjects in NACC

To Upload a file run

    $ python sel.py upload
To Get current Subjects from Nacc run

    $ python sel.py getdata


# NACC Report Generation using Docker

It is used to get the reports and Email it. 

## Getting Started

These instructions will help you build a docker image on your local machine from which you can spawn up and run a container that would automate the process of report generation.

First clone the project in your local.

```
git clone -b nacc_docker https://github.com/roukna/nacculator.git
```

### Prerequisites

Update the credentials in the **env_file** file as below:
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

### Run the image
```bash
docker run --env-file=env_file -it nacc_image:latest /bin/bash
```
You need not always use the env_file to pass values for the environment variables. You may use the ``docker run -e`` option to pass the values from the command line.
