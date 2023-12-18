# -*- coding: utf-8 -*-
"""
Schedules
Run schedule for BRT pipeline tasks each 10 minutes
"""
from datetime import timedelta, datetime
from prefect.schedules import Schedule
from prefect.schedules.clocks import IntervalClock

schedule_10_minutes = Schedule(
    clocks=[
        IntervalClock(
            start_date=datetime.utcnow() + timedelta(seconds=10),
            interval=timedelta(seconds=60),
        )
    ]
)
