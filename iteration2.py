import numpy as np
import pandas as pd

df = pd.read_csv("./DAV Project/datasets/vlrDataset.csv")

print("Null Values in the Dataframe")

print()

print(df.isnull().sum())

df = df.dropna()

print()

print("Null Values Dropped")

print()

print(df.isnull().sum())

print()

print(f"Duplicate Values in the Dataframe: {df.duplicated().sum()}")

listOfTeams = [[], []]

listOfTeams[0] = list(df["team1_Name"])
listOfTeams[1] = list(df["team2_Name"])

setOfTeams = [[set(listOfTeams[0])], [set(listOfTeams[1])]]

finalSet = []

for i in range(len(listOfTeams[0])):
    finalSet.append(listOfTeams[0][i])

for i in range(len(listOfTeams[1])):
    finalSet.append(listOfTeams[1][i])

finalSet = set(finalSet)

teamEncoding = {team: idx for idx, team in enumerate(finalSet)}

df["team1Encoded"] = df["team1_Name"].map(teamEncoding)
df["team2Encoded"] = df["team2_Name"].map(teamEncoding)

listOfAgents = (
    list(df["agent1"])
    + list(df["agent2"])
    + list(df["agent3"])
    + list(df["agent4"])
    + list(df["agent5"])
    + list(df["agent6"])
    + list(df["agent7"])
    + list(df["agent8"])
    + list(df["agent9"])
    + list(df["agent10"])
)

setOfAgents = set(listOfAgents)

agentEncoding = {agent: idx for idx, agent in enumerate(setOfAgents)}

df["agent1Encoded"] = df["agent1"].map(agentEncoding)
df["agent2Encoded"] = df["agent2"].map(agentEncoding)
df["agent3Encoded"] = df["agent3"].map(agentEncoding)
df["agent4Encoded"] = df["agent4"].map(agentEncoding)
df["agent5Encoded"] = df["agent5"].map(agentEncoding)
df["agent6Encoded"] = df["agent6"].map(agentEncoding)
df["agent7Encoded"] = df["agent7"].map(agentEncoding)
df["agent8Encoded"] = df["agent8"].map(agentEncoding)
df["agent9Encoded"] = df["agent9"].map(agentEncoding)
df["agent10Encoded"] = df["agent10"].map(agentEncoding)

listOfMaps = list(df["mapName"])
setOfMaps = set(listOfMaps)

mapEncoding = {map: idx for idx, map in enumerate(setOfMaps)}

df["encodedMapName"] = df["mapName"].map(mapEncoding)

df["year"] = None

df.loc[(df["patchID"] >= 2.04) & (df["patchID"] <= 3.10), "year"] = 2021
df.loc[(df["patchID"] >= 4.02) & (df["patchID"] <= 5.04), "year"] = 2022
df.loc[(df["patchID"] >= 6.02) & (df["patchID"] <= 7.02), "year"] = 2023
df.loc[(df["patchID"] >= 8.02) & (df["patchID"] <= 9.02), "year"] = 2024

df["team1Agents"] = (
    df[
        [
            "agent1Encoded",
            "agent2Encoded",
            "agent3Encoded",
            "agent4Encoded",
            "agent5Encoded",
        ]
    ]
    .astype(str)
    .apply(lambda x: ", ".join(x), axis=1)
)

df["team2Agents"] = (
    df[
        [
            "agent6Encoded",
            "agent7Encoded",
            "agent8Encoded",
            "agent9Encoded",
            "agent10Encoded",
        ]
    ]
    .astype(str)
    .apply(lambda x: ", ".join(x), axis=1)
)

processedDF = df[
    [
        "year",
        "team1Encoded",
        "team2Encoded",
        "encodedMapName",
        "team1Score",
        "team2Score",
        "agent1Encoded",
        "agent2Encoded",
        "agent3Encoded",
        "agent4Encoded",
        "agent5Encoded",
        "agent6Encoded",
        "agent7Encoded",
        "agent8Encoded",
        "agent9Encoded",
        "agent10Encoded",
        "team1Agents",
        "team2Agents",
    ]
]

processedDF.to_csv("./DAV Project/datasets/processedVLRDataset.csv", index=False)
