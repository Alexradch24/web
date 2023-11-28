FROM python:latest

RUN pip install redis
RUN pip install flask

ADD run.py /
ADD app/views.py /app/
ADD app/__init__.py /app/
ADD app/templates/Web.html /app/templates/

EXPOSE 8888

CMD ["python", "run.py"]