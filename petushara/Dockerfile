FROM python:3.8-slim
LABEL maintainer="t.me/cillum_project"
RUN mkdir -p ~/.cillum/tg2ds_bot
WORKDIR ~/.cillum/tg2ds_bot/
COPY . ./

RUN chmod +x run.sh
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "bash", "./run.sh" ]
