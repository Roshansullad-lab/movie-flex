FROM python3.11
WORKDIR app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [uvicorn, mainapp, --host, 0.0.0.0, --port, 8000]
