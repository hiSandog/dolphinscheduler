# -*- coding: utf-8 -*-
from pydolphinscheduler.core import ProcessDefinition
from pydolphinscheduler.tasks import Sql

task_name = "商户等级表"


def job_name(jobName):
    return jobName + "(" + task_name + ")"


a = "123"
b = "123"
if a == b:
    print("sss")

# with ProcessDefinition(
#         user="admin",
#         project="dev",
#         name="1xxxx",
#         schedule="0 20 3 * * ? *",
#         start_time="2021-01-01",
#         tenant="dev"
# ) as pd:
    # first_day_run = Sql(
    #     name=job_name("每月一号执行"),
    #     datasource_name="dev",
    #     sql="update ta set app = '' where id = 1;")
    # pd.submit()
