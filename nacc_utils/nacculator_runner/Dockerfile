FROM selenium/node-chrome:latest

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
COPY nacc_automation/sel.py nacc_automation/packet_config_example.ini nacc_automation/getpacket.js /nacc_utils/

WORKDIR /nacc_utils
RUN chmod u+x run.sh

RUN apt-get -y install scrot
RUN apt-get -y install python-tk
RUN apt-get -y install python-dev
RUN pip install --upgrade pip; hash -r pip;
RUN pip install pdfminer python-xlib selenium jinja2
RUN pip install git+https://github.com/devmattm/nacculator.git@quick_fixes git+https://github.com/ctsit/cappy.git
RUN xvfb-run pip install pyautogui

ENTRYPOINT ["/bin/bash", "-c", "./run.sh", "getdata"]
