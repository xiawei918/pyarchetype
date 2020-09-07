FROM python:3.8.0

ENV PYTHONPATH "${PYTHONPATH}:/project"

WORKDIR /project

RUN pip install poetry

COPY pyproject.toml *.lock /project/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

EXPOSE 8888

ENTRYPOINT ["jupyter", "lab", "--no-browser", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''"]
