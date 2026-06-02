FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    binutils \
    file \
    ltrace \
    strace \
    upx-ucl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/helper_scripts/string_extractor.py", "--help"]
