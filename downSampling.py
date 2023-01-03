import pandas as pd
import os
import pseudocode


def main():
    for month in range(11,13):
        for day in range(1, 32):
            dateString = f"2022-{month}-{day}"
            sampleDown(dateString)

def sampleDown(dateString):
    if not os.path.isfile(f"datasets/{dateString}.csv"):
        return
    df = pd.read_csv(f"datasets/{dateString}.csv")
    df = pseudocode.turnTime(df, dateString)
    df = pseudocode.removeDoubles(df)
    df = pseudocode.sampleDown(df, flocks = 4)
    df = pseudocode.addTrackerState(df)
    df.to_csv(f"sampledDownDataSets/{dateString}.csv")

if __name__ == "__main__":
    main()