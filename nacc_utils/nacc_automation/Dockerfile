FROM selenium/node-chrome:latest

USER root

ENV DISPLAY ":99.0"

RUN apt-get -y update
RUN apt-get -y dist-upgrade
RUN apt-get -y install python2.7 python-pip

ADD ./ /nacc_utils
WORKDIR /nacc_utils
RUN ls && chmod u+x run.sh

RUN apt-get -y install scrot
RUN apt-get -y install python-tk
RUN apt-get -y install python-dev
RUN Xvfb :99 -nolisten tcp -fbdir /var/run &
RUN pip install --upgrade pip
RUN pip install pdfminer
RUN pip install python-xlib
RUN pip install selenium
RUN pip install jinja2

ENTRYPOINT ["/bin/bash", "-c", "./run.sh"] 
