# ---------- Stage 1: Run tests ----------
FROM python:3.10-slim as tester

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Run tests and fail build on error (output will be visible)
RUN pytest --tb=short --disable-warnings

# ---------- Stage 2: Build app ----------
FROM python:3.10-slim as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ---------- Stage 3: Minimal production image ----------
FROM python:3.10-alpine

WORKDIR /app

COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10

EXPOSE 5000
CMD ["python", "app.py"]

