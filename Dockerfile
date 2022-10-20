FROM python:3.8-alpine
COPY . /web
WORKDIR /web/
RUN pip install -r ./requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
