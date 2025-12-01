FROM python:3.12-alpine as base

WORKDIR /usr/src/app

# Install required packages for the installer
RUN apk add --no-cache curl

# Upgrade pip
RUN pip install --upgrade pip

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy application files
COPY . .

# Make start script executable
RUN chmod +x start.sh


FROM base as develop

# Install git for development
RUN apk add --no-cache git

# Generate a pip-compatible lock
RUN uv pip compile --group dev pyproject.toml -o requirements.lock

# Install dependencies including dev packages
RUN uv pip sync --system requirements.lock

# Collect static files
RUN python manage.py collectstatic --noinput
RUN pre-commit install

# Add make commands
RUN apk update && apk add make

# Run application
CMD ["python", "manage.py", "migrate"]


FROM base as production

# Generate a pip-compatible lock
RUN uv pip compile pyproject.toml -o requirements.lock

# Install dependencies
RUN uv pip sync --system requirements.lock

# Collect static files
RUN python manage.py collectstatic --noinput

# Run application
ENTRYPOINT ["/bin/sh", "-c", "./start.sh"]
