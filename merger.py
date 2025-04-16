import pandas as pd

csvFiles = ["./datasets/stage1_2021.csv","./datasets/mastersReykjavik2021.csv", "./datasets/stage2_2021.csv","./datasets/mastersBerlin2021.csv", 
            "./datasets/stage3_2021.csv","./datasets/championsData2021.csv",
             "./datasets/stage1_2022.csv","./datasets/stage1_2_2022.csv", "./datasets/mastersReykjavik2022.csv", 
             "./datasets/stage2_2022.csv","./datasets/mastersCopenhagen2022.csv", "./datasets/stage3_2022.csv","./datasets/championsData2022.csv",
             "./datasets/lockInData2023.csv", "./datasets/stage1_2023.csv","./datasets/mastersTokyo2023.csv", 
             "./datasets/stage2_2023.csv","./datasets/championsData2023.csv",
             "./datasets/stage1_2024.csv","./datasets/mastersMadrid2024.csv", "./datasets/stage2_2024.csv","./datasets/mastersShangai2024.csv", 
             "./datasets/stage3_2024.csv","./datasets/championsData2024.csv",]

dfs = []

for csvFile in csvFiles:
    df = pd.read_csv(csvFile)
    dfs.append(df)

mergedDF = pd.concat(dfs, ignore_index=True)

outputPath = './datasets/vlrDataset.csv'
mergedDF.to_csv(outputPath, index=False)