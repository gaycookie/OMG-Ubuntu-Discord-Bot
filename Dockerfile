FROM python:3.8-slim-buster

ENV BOT_TOKEN "BOT_TOKEN_HERE!"

WORKDIR /bot

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "bot.py"]