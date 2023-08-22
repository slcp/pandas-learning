import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 22, 35, 58, 58],
        "Sex": ["male", "male", "male", "female", "female"],
    }
)

series = pd.Series([1, 1, 2, 3, 4], name="IndependentSeries")
df["ExtraColumnAsSeries"] = series
df["ExtraColumnAsList"] = [4, 4, 5, 6, 7]

if __name__ == "__main__":
    print("Whole Data Frame")
    print(df)

    print("Name series of Data Frame")
    print(df["Name"])

    print("Maxing age column")
    print(df["Age"].mean())

    print("Maxing extra series")
    print(series.max())

    print("Describing Data Frame")
    print(df.describe())

    print("Describing Series")
    print(series.describe())

    # print("Describing Data Frame non default")
    # print(df.describe(include="all"))
    # print(df.describe(include="object"))
    # print(df.describe(include="number"))

    print("Index min/max")
    # Gets the index of the max value, the position in the series
    print(df["Age"][df["Age"].idxmax()])

    print("Value counts, histogram, count of instances of each value")
    print(df.value_counts())
    print(df.value_counts(subset=["Name", "Age"]))

    print("Cut Data Frame - discretization")
    print(pd.cut(df["Age"], bins=3))

    print("head")
    print(df.head())
    print(df.head(2))

    print("info")
    print(df.info())
