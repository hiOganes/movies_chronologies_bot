FROM python:3.13

WORKDIR /bot/movies_chronologies_bot

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "bot.main"]