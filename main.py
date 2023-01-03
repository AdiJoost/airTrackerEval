import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as pltDate
import matplotlib.colors as pltColor
import math
import pseudocode
import os

def main():
    for month in range(11,13):
        for day in range(1, 32):
            dateString = f"2022-{month}-{day}"
            creatPlot(dateString)
            """
            if not os.path.isfile(f"datasets/{dateString}.csv"):
                continue
            df = pd.read_csv(f"datasets/{dateString}.csv")
            df = pseudocode.turnTime(df, dateString)
            print(df.head())
            dates = pltDate.date2num(df["DateTime"])
            plt.plot_date(dates, df["Co2"])
            plt.savefig(f"plots/{dateString}.png")
            plt.clf()"""

def creatPlot(dateString):
    
    if not os.path.isfile(f"sampledDownDataSets/{dateString}.csv"):
        return
    
    df = pd.read_csv(f"sampledDownDataSets/{dateString}.csv")
    
    df.drop("Unnamed: 0", axis=1, inplace=True)
    df["DateTime"] = pd.to_datetime(df["DateTime"])
    pseudocode.addPitch(df)
    #df = pseudocode.turnTime(df, dateString)
    #df = pseudocode.addTrackerState(df)
    
    
    fig, ax = plt.subplots(2, 1, figsize=(15,10))
    cmap = pltColor.LinearSegmentedColormap.from_list("", ["green","blue","yellow", "orange", "red"])
    #fig, ax = plt.subplots(figsize=(15,10))
    ax[0].scatter(df["Time"], df["Co2"], c=df["State"], cmap=cmap)


    every_nth = math.floor(len(df) / 50)
    beforeLabel = "05:00"
    for n, label in enumerate(ax[0].xaxis.get_ticklabels()):
        
        if not pseudocode.shouldBeVisible(label.get_text(), beforeLabel):
            label.set_visible(False)
        beforeLabel = label.get_text()
    
    ax[0].tick_params(axis="x", rotation=90)
    ax[0].set_ylabel("CO2 concentration [ppm]")
    plt.xlabel("Time")
    
    #ax = plt.subplot(2,1,2)

    cmap = pltColor.LinearSegmentedColormap.from_list("", ["green","blue","yellow", "orange", "red"])
    #fig, ax = plt.subplots(figsize=(15,10))
    ax[1].scatter(df["Time"], df["Pitch"], c=df["State"], cmap=cmap)


    every_nth = math.floor(len(df) / 50)
    beforeLabel = "05:00"
    for n, label in enumerate(ax[1].xaxis.get_ticklabels()):
        
        if not pseudocode.shouldBeVisible(label.get_text(), beforeLabel):
            label.set_visible(False)
        beforeLabel = label.get_text()
    
    ax[1].tick_params(axis="x", rotation=90)
    plt.ylabel("Increase of Co2 concentration per second")
    plt.xlabel("Time")
    plt.savefig(f"sampledDownDataSets/plots/double_{dateString}.png")
    plt.clf()

if __name__ == "__main__":
    main()