FROM python:3
RUN pip install prometheus_client
ADD . .
CMD python3 job.py
