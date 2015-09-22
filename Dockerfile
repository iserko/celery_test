FROM python:2.7
RUN pip install celery==3.1.18
ADD . /home/code
WORKDIR /home/code
ENV PYTHONPATH=/home/code/src:$PYTHONPATH
USER nobody
