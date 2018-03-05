
# NACC Report Generation using Docker

## Getting Started

These instructions will help you build a docker image on your local machine from which you can spawn up and run a container that would automate the process of report generation.

First clone the project in your local.

```git
git clone -b nacc_docker 
```

### Prerequisites

Update the credentials in the **packet_config_example.ini** file as below:
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

```docker
docker build -t <image_name>:<version_no.> .
```
