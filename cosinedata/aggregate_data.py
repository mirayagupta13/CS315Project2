import pandas as pd

names = ["./results_AL_Scores.csv", "./results_CF_Scores.csv", "./results_JK_Scores.csv", "./results_MG_Scores.csv", "./results_MM_Scores.csv"]

final_csv = pd.DataFrame()
for name in names:
    df = pd.read_csv(name)
    print(df)
    final_csv = pd.concat([final_csv, df])

final_csv.to_csv('overall_cosine_similarities.csv')