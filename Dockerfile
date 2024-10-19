FROM python:3.12.3-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/pyapp

WORKDIR /pyapp

COPY . /pyapp/

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "src/main.py"]

CMD ["input_file/purchases_v1.json"]