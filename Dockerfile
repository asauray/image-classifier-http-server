FROM python:3.6
COPY requirements.txt ./
RUN pip install -r ./requirements.txt
RUN pip install tensorflow
COPY index.py ./index.py
COPY mug.jpg ./mug.jpg
ENTRYPOINT ["python", "index.py"]
