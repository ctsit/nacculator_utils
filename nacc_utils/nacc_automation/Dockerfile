FROM selenium/node-chrome:latest

USER root

ENV DISPLAY ":99.0"

RUN apt-get -y update
RUN apt-get -y dist-upgrade
RUN apt-get -y install python2.7 python-pip


ADD ./ /nacc_utils
WORKDIR /nacc_utils
RUN chmod u+x run.sh

RUN apt-get -y install scrot
RUN apt-get -y install python-tk
RUN apt-get -y install python-dev
RUN pip install --upgrade pip; hash -r pip;
RUN pip install pdfminer python-xlib selenium jinja2
RUN xvfb-run pip install pyautogui

ENTRYPOINT ["/bin/bash", "-c", "./run.sh"] 
