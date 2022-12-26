import pandas as pd
from datetime import datetime, time


def turnTime(df, dateString):
    #Turns Hour, Minute, second into dateTime object
    year, month, day = dateString.split("-")
    year = int(year)
    month = int(month)
    day = int(day)
    df["DateTime"] = None
    df["Time"] = None
    for i in range(len(df)):
        hour = int(df.iloc[i, 4])
        minute = int(df.iloc[i, 5])
        second = int(df.iloc[i, 6])
        df.iloc[i, 7] = datetime(
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            second=second)
        df.iloc[i, 8] = time(
            hour=hour,
            minute=minute,
            second=second
        )
    df.drop("Hour", axis=1, inplace=True)
    df.drop("Minute", axis=1, inplace=True)
    df.drop("Second", axis=1, inplace=True)
    return df