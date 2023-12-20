from prefect import Flow
from schedules import schedule_15_minutes
from prefect.run_configs import LocalRun

from tasks import (
    download_data,
    parse_data,
    transform_data,
    save_report,
    load_to_postgres
)

with Flow("Capture BRT Data", schedule=schedule_15_minutes) as capture_brt_data:

    # Tasks
    data = download_data()
    dataframe = parse_data(data)
    transformed_dataframe = transform_data(dataframe)
    save_report(transformed_dataframe)
    load_to_postgres(transformed_dataframe)
    
capture_brt_data.run_config = LocalRun(working_dir='.') # Run flow locally
capture_brt_data.register(project_name="ProjetoBRT") # Register flow

