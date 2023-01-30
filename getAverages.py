import pandas as pd
from logger import Logger
import os

def main():
    #get averageValues of Datasets
    """
    for month in range(11,13):
        for day in range(1,32):
            date = f"2022-{month}-{day}"
            if os.path.isfile(f"sampledDownDataSets/{date}.csv"):
                avrgCo2, states = getValues(date)
                Logger.log_csv((
                    date,
                    avrgCo2,
                    states[0],
                    states[1],
                    states[2],
                    states[3],
                    states[4]
                ))"""
    #get averages by workdays
    values = calcDays()
    for key in values:
        print(values[key])

def getValues(date):
    df = pd.read_csv(f"sampledDownDataSets/{date}.csv", usecols=["Co2","DateTime", "State"])
    df["DateTime"] = pd.to_datetime(df["DateTime"])
    df.index = df["DateTime"]
    df = df.between_time("5:45", "17:45")
    

    stateCount = df["State"].value_counts()
    orderdStateCount ={
        0:0,
        1:0,
        2:0,
        3:0,
        4:0
    }
    totalMessurements = sum(stateCount.values)
    if totalMessurements != 0:
        for i in stateCount.index:
            orderdStateCount[i] = float(stateCount[i]) / totalMessurements
        
    return (df["Co2"].mean(), orderdStateCount)

def calcDays():
    df = pd.read_csv("data.csv")
    avrgValues = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
    }
    for i in range(len(df)):
        avrgValues.get(i%5).append((
            df.iloc[i,1],
            df.iloc[i,2],
            df.iloc[i,3],
            df.iloc[i,4],
            df.iloc[i,5],
            df.iloc[i,6]))
    returnValue = {}
    for key in avrgValues:
        co2, s0, s1, s2, s3, s4 = 0, 0, 0, 0, 0, 0
        for values in avrgValues[key]:
            co2 += values[0]
            s0 += values[1]
            s1 += values[2]
            s2 += values[3]
            s3 += values[4]
            s4 += values[5]
        rows = len(avrgValues[key])
        co2 /= rows
        s1 /= rows
        s2 /= rows
        s3 /= rows
        s4 /= rows
        s0 /= rows
        returnValue[key] = (co2, s0, s1, s2, s3, s4)
    return returnValue


if __name__ == "__main__":
    main()