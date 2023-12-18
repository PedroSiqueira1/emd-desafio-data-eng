from prefect import Flow
from schedules import schedule_10_minutes
from prefect.run_configs import LocalRun

from tasks import (
    download_data,
    parse_data,
    save_report,
)

with Flow("Dados dos Onibus") as flow:

    # Tasks
    data = download_data()
    dataframe = parse_data(data)
    save_report(dataframe)

flow.schedule = schedule_10_minutes

# Run flow locally
flow.run_config = LocalRun(working_dir='.')

flow.register(project_name="ProjetoBRT")
