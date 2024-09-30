FROM python:3.9-slim
WORKDIR /teste
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 7860
ENV PYTHONUNBUFFERED=1
CMD ["python", "teste"]
