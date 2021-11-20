#FROM python:3.8
#
#RUN mkdir -p ~/.cillum/tg2ds-multi
#
#ADD . ~/.cillum/tg2ds-multi/
#
#WORKDIR ~/.cillum/tg2ds-multi
#
#COPY requirements.txt ./
#
#RUN python3 -m venv ./venv/
#RUN ./venv/bin/pip3 install -r requirements.txt
#
#
#CMD [ "bash", "./run.sh"]
#
# НИХУЯ НЕ ЗАРАБОТАЛО