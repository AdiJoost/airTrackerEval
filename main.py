import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as pltDate
import pseudocode

def main():
    dateString = "2022-11-24"
    df = pd.read_csv(f"datasets/{dateString}.csv")
    df = pseudocode.turnTime(df, dateString)
    print(df.head())
    dates = pltDate.date2num(df["DateTime"])
    plt.plot_date(dates, df["Co2"])
    plt.savefig(f"plots/{dateString}.png")



if __name__ == "__main__":
    main()