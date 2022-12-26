import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as pltDate
import pseudocode
import os

def main():
    for month in range(11,13):
        for day in range(1, 32):
            dateString = f"2022-{month}-{day}"
            if not os.path.isfile(f"datasets/{dateString}.csv"):
                continue
            df = pd.read_csv(f"datasets/{dateString}.csv")
            df = pseudocode.turnTime(df, dateString)
            print(df.head())
            dates = pltDate.date2num(df["DateTime"])
            plt.plot_date(dates, df["Co2"])
            plt.savefig(f"plots/{dateString}.png")



if __name__ == "__main__":
    main()