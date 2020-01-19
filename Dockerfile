FROM python:3.8
LABEL maintainer="Aurélien Hugues <aurelien.hugues.59@gmail.com>"
LABEL description="Api to automatically get movie and serie information using their barcode"
ADD barcode_api /app/barcode_api
COPY requirements.txt /app
COPY wsgi.py /app
COPY README.md /app
COPY setup.py /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install gunicorn
ENTRYPOINT ["gunicorn", "wsgi:app", "-b", "0.0.0.0:5000", "--workers=3"]
