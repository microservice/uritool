FROM kennethreitz/pipenv

COPY . /app

ENTRYPOINT ["python3", "uritool.py"]
