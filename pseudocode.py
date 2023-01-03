import pandas as pd
from datetime import datetime, time, timedelta


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
        df.iloc[i, 8] = "{:02d}".format(hour) + ":" + "{:02d}".format(minute)
    df.drop("Hour", axis=1, inplace=True)
    df.drop("Minute", axis=1, inplace=True)
    df.drop("Second", axis=1, inplace=True)
    return df

def addPitch(df):
    df["Pitch"] = None
    for i in range(len(df) - 1):
        deltaTime = (df.iloc[(i + 1), 4] - df.iloc[i, 4]).total_seconds()
        deltaCO2 = df.iloc[(i + 1), 3] - df.iloc[i, 3]
        df.iloc[i, 7] = float(deltaCO2) / deltaTime
    df.iloc[len(df)-1, 7] = 0
    return df
        


def addTrackerState(df, turningPoints=(800, 1100, 1500, 2000)):
    df["State"] = -1
    df.iloc[df["Co2"].between(0, turningPoints[0]), len(df.columns) - 1] = 0
    df.iloc[df["Co2"].between(turningPoints[0], turningPoints[1]), len(df.columns) - 1] = 1
    df.iloc[df["Co2"].between(turningPoints[1], turningPoints[2]), len(df.columns) - 1] = 2
    df.iloc[df["Co2"].between(turningPoints[2], turningPoints[3]), len(df.columns) - 1] = 3
    df.iloc[df["Co2"].between(turningPoints[3], 10000), len(df.columns) - 1] = 4
    return df
 
def shouldBeVisible (labelText, beforeText):
    if labelText[:2] != beforeText[:2]:
        return True
    return False

def sampleDown(df, flocks=4):
    newDF = pd.DataFrame(columns=df.columns)
    i = 0
    while i < len(df) - 4:
        miniDF = df.iloc[i:i+4]
        meanTemp = miniDF["Temperature"].mean()
        meanHum = miniDF["Humidity"].mean()
        meanPressure = miniDF["Pressure"].mean()
        meanCo2 = miniDF["Co2"].mean()
        newDF = pd.concat([newDF, pd.Series(
            {"Temperature": meanTemp,
            "Humidity": meanHum,
            "Pressure": meanPressure,
            "Co2": meanCo2,
            "DateTime": df.iloc[i, 4],
            "Time": df.iloc[i, 5]}
        ).to_frame().T], ignore_index=True)
        i += 5
    return newDF

def removeDoubles(dff):
    df = dff.copy()
    i = 0
    maxRange = len(df)
    while i < maxRange - 1:   
        if (df.iloc[i + 1, 4] - df.iloc[i, 4]).total_seconds() < 10:
            df.drop(df.index[i], inplace=True)
        else:
            i += 1
        maxRange = len(df)
    return df