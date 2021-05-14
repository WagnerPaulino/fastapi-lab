FROM python:3.7.10
WORKDIR /meusvideos-backend
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
EXPOSE 80
ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 80