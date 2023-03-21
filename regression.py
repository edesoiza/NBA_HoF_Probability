from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import csv

df = pd.read_csv("final_player_data.csv")

df_mask = df["start"] > 1969
df_time_mask = df["end"] - df["start"] > 5
masked_df = df[df_mask | df_time_mask].reset_index()
player_mask = masked_df["Player"] == "LeBron James"
print(masked_df[player_mask])

x_df = masked_df[masked_df.columns[3:14]]
y_df = masked_df["hof"]
x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size= .2, random_state= 10)

lr = LogisticRegression(random_state= 11).fit(x_train, y_train)
#print(lr.predict_proba(x_df.loc[1691]))
print(lr.score(x_test, y_test))
probas = lr.predict_proba(x_df)
print(masked_df.loc[1691])
print(probas[1691])

predictions = lr.predict(x_df)
print(predictions.shape)
print(type(predictions))


predictions_df = pd.DataFrame(predictions)
labeled_decisions = [[val, predictions_df[0][i]] for i, val in enumerate(masked_df["Player"])]
labeled_probabilities = [[val, probas[i][1], predictions_df[0][i]] for i, val in enumerate(masked_df["Player"])]
print(labeled_probabilities)
def Sort(sub_li):
    sub_li.sort(key = lambda x: x[1])
    return sub_li

sorted_probs = Sort(labeled_probabilities)[::-1]
print(lr.coef_)

with open("outcomes2.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(sorted_probs)
