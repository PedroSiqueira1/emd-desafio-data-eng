# -*- coding: utf-8 -*-
"""
Schedules
Run schedule for BRT pipeline tasks each minute for 15 minutes

"""

from datetime import timedelta, datetime
from prefect.schedules import Schedule
from prefect.schedules.clocks import IntervalClock

schedule_15_minutes = Schedule(
    clocks=[
        IntervalClock(
            start_date=datetime.utcnow() + timedelta(seconds=10),
            interval=timedelta(seconds=60),
            end_date=datetime.utcnow() + timedelta(seconds=900)  # End date in 15 minutes
        )
    ]
)
