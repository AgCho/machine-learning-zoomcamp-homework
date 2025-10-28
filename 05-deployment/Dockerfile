FROM agrigorev/zoomcamp-model:2025

WORKDIR /app

COPY pyproject.toml uv.lock* ./

RUN pip install --no-cache-dir uv && uv sync --no-dev

COPY service.py .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8000"]