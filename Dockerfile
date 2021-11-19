FROM python:3.8

RUN mkdir -p ~/.cillum/tg2ds-multi

WORKDIR ~/.cillum/tg2ds-multi

ADD . ~/.cillum/tg2ds-nulti/
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./tgm.py"]
CMD [ "python", "./disc.py"]
