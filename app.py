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

# series = pd.Series([1, 1, 2, 3, 4], name="IndependentSeries")
# df["ExtraColumnAsSeries"] = series
# df["ExtraColumnAsList"] = [4, 4, 5, 6, 7]

if __name__ == "__main__":
    print("Whole Data Frame")
    print(df)

    print("Name series of Data Frame")
    print(df["Name"])

    print("Maxing age column")
    print(df["Age"].mean())

    # print("Maxing extra series")
    # print(series.max())

    print("Describing Data Frame")
    print(df.describe())

    # print("Describing Series")
    # print(series.describe())

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

    # TODO: Understand this more
    print("Cut Data Frame - discretization")
    print(pd.cut(df["Age"], bins=3))

    print("head")
    print(df.head())
    print(df.head(2))

    print("info")
    print(df.info())

    print("Group by")
    # This will only work if there is only one/or only column(s) with numerical data when discounting the groupby column(s)
    # We can select columns from the group by to operate on directly though
    print(df.groupby(by=["Name"])["Age"].mean())

    # Apply a function to each column in the DataFrame - transform
    #  Apply returns a new DataFrame
    # https://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas
    print("Apply/Map/ApplyMap")
    # df["Age"] = df["Age"].apply(lambda x: x * 2)
    # df["Age"].apply(lambda x: print(type(x)))

    # element-wise - x is each element in the series
    print("Apply - Element wise")
    applied = df["Age"].apply(lambda x: x * 2)
    print(applied.head(5))

    # vector-wise - x is a series/column/collection that is operated on in its totality
    # numpy (under pandas) provides the capability to do transformations of each element when operating vector wise
    print("Vector wise")
    vectorwise = df["Age"] = df["Age"] * 2
    print(vectorwise.head(5))

    print("Map - Element wise")
    mapped = df["Age"].map(lambda x: x + 2)
    print(mapped.head(5))

    print("ApplyMap - Element wise")
    # ApplyMap returns a new DataFrame
    # ApplyMap applies the function to every element in the DataFrame
    applymapped = df.applymap(lambda x: x if isinstance(x, str) else x*2)
    print(applymapped.head(5))

    # Not sure what to call this - use Series values to amend the DataFrame?
    # print("Not sure what to call this")
    # df[["Age", "Name"]] = df[["Name", "Age"]]
    # print(df.head(5))
