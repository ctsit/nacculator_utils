
# NACC Report Generation using Docker

## Getting Started

These instructions will help you build a docker image on your local machine from which you can spawn up and run a container that would automate the process of report generation.

First clone the project in your local.

```
git clone -b nacc_docker https://github.com/roukna/nacculator.git
```

### Prerequisites

Update the credentials in the **packet_config_example.ini** file as below:
```bash
cd nacculator/get_current_data
vi packet_config_example.ini
```
```
[DEFAULT]

[credentials]
username: <username>
password: <password>
email: <email_id>
[uploadpath]
path: /path/to/text/file/to/upload
[downloadpath]
path: /tmp
[reportpath]
path: /Users/rsengupta/Downloads
```
Update the smtp credentials and e-mail recipients in the **smtp_config_example.ini** file as below:

```bash
cd nacculator/get_current_data
vi smtp_config_example.ini
```

```
[DEFAULT]

[credentials]
host: smtp.ufl.edu
port: 587
my_address: <gator_name>
password: <gator_password>

[recipient_list]
hcv_recipient: rouknasengupta@gmail.com,rsengupta@ufl.edu,amineni95@ufl.edu
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
docker run -it nacc_image:latest /bin/bash
```
