FROM django:3.2.13 AS venv

FROM server:1.0 AS base

COPY --from=venv /opt/venv /opt/venv

# make sure all messages always reach console
ENV PYTHONUNBUFFERED=1

# activate virtual environment
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

