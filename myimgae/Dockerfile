# syntax=docker/dockerfile:1
FROM python:3.8
COPY . .
WORKDIR /usr/src/app/
COPY . .
RUN pip install --user pytest
RUN pip install --user requests
RUN pip install --user wheel
RUN pip install --user pyTelegramBotAPI
CMD ["python", "mybot.py"]