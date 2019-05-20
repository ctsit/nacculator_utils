FROM selenium/node-chrome:3.14.0-europium

USER root

ENV DISPLAY ":99.0"
RUN rm -rf /etc/apt/sources.list
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt xenial main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-updates main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb-src mirror://mirrors.ubuntu.com/mirrors.txt xenial-updates main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-backports main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-security main restricted universe multiverse" >> /etc/apt/sources.list
RUN apt update && apt-get -y install python2.7 python-pip git
RUN apt-get clean && apt-get update
COPY nacculator_runner/ /nacc_utils/
COPY nacc_automation/sel.py nacc_automation/packet_config_example.ini nacc_automation/getpacket.js nacc_automation/send_email.py nacc_automation/smtp_config_example.ini /nacc_utils/

WORKDIR /nacc_utils
RUN chmod u+x run.sh

RUN apt-get -y install scrot python-tk python-dev
RUN pip install --upgrade pip; hash -r pip
RUN pip install pdfminer==20140328 python-xlib==0.25 selenium==3.141.0 jinja2==2.10.1
RUN pip install git+https://github.com/ctsit/nacculator.git git+https://github.com/ctsit/cappy.git
RUN xvfb-run pip install pyautogui==0.9.39

ENTRYPOINT ["/bin/bash", "-c", "./run.sh", "getdata"]
