FROM python AS base
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

FROM base
COPY src/* /app

EXPOSE 80

CMD ["python", "main.py"]