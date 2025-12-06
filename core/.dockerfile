FROM python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /core
COPY requirements.txt /core/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /core/
