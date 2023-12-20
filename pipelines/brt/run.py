from flows import capture_brt_data
from utils import create_environment
from dbt.cli.main import dbtRunner, dbtRunnerResult


create_environment()
capture_brt_data.run()


print("Fim do script")