# -*- coding: utf-8 -*-
from pydolphinscheduler.core import ProcessDefinition
from pydolphinscheduler.tasks import Python

task_name = "商户等级表"


def job_name(jobName):
    return jobName + "(" + task_name + ")"


if __name__ == "__main__":
    with ProcessDefinition(
            user="admin",
            project="dev",
            name="1xxxx",
            schedule="0 20 3 * * ? *",
            start_time="2021-01-01",
            tenant="dev"
    ) as pd:
        base_info = Python(
            definition="str",
            name=job_name("原始基数日常执行"),
            resource_list=[{"resourceName": "/aaa.sh"}],
            # code="""print"""
        )
        pd.submit()
