FROM selenium/node-chrome:3.141.59-vanadium

USER root

ENV DISPLAY ":99.0"
RUN apt update && apt-get -y install python2.7 python-pip git
COPY nacculator_runner/ /nacc_utils/
COPY nacc_automation/sel.py nacc_automation/packet_config_example.ini nacc_automation/getpacket.js nacc_automation/send_email.py nacc_automation/smtp_config_example.ini /nacc_utils/

RUN apt-get -y install scrot python-tk python-dev
RUN pip install --upgrade pip; hash -r pip
RUN pip install pdfminer==20140328 python-xlib==0.25 selenium==3.141.0 jinja2==2.10.1
RUN xvfb-run pip install pyautogui==0.9.39
RUN pip install git+https://github.com/ctsit/nacculator.git git+https://github.com/ctsit/cappy.git

WORKDIR /nacc_utils
ENTRYPOINT ["/bin/bash", "./run.sh"]
