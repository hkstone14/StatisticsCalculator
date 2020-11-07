FROM python:3

ADD src /src

RUN pip install --upgrade pip

CMD ["python", "-m", "unittest", "discover", "-s","Test"]