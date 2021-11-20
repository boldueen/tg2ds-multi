FROM python:3.8
LABEL maintainer="t.me/cillum_project"
RUN mkdir -p ~/.cillum/tg2ds_bot
RUN mkdir -p ~/.cillum/tg2ds_bot/data
RUN mkdir -p ~/.cillum/tg2ds_bot/utils
WORKDIR ~/.cillum/tg2ds_bot/
COPY data data
COPY utils utils

COPY . ./

RUN python -m venv ./venv/
RUN ./venv/bin/pip install -r requirements.txt
CMD [ "bash", "./run.sh" ]
