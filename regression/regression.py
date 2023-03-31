from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import csv
import os

script_dir = os.path.dirname(__file__) 
final_path = os.path.join(script_dir, '../data/final')

def Sort(sub_li):
    sub_li.sort(key = lambda x: x[1])
    return sub_li

df = pd.read_csv(final_path + "/" + "final_player_data.csv")

df_mask = df["start"] > 1969
df_start = df["end"] < 2023
df_time_mask = df["end"] - df["start"] > 6
masked_df = df[df_mask & df_time_mask].reset_index()

train_dff = masked_df[masked_df["end"] != 2023]
x_df = train_dff[train_dff.columns[8:18]]
y_df = train_dff["hof"]

z_df = masked_df[masked_df.columns[8:18]]
zz_df = masked_df["hof"]
x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size= .2, random_state= 10)

lr = LogisticRegression(random_state= 11).fit(x_train, y_train)
print(lr.score(x_test, y_test))
probas = lr.predict_proba(x_df)


predictions = lr.predict(x_df)

from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB().fit(x_train, y_train)
print("score on test: " + str(mnb.score(x_test, y_test)))
print("score on train: "+ str(mnb.score(x_train, y_train)))
mnb_predictions = mnb.predict(z_df)
mnb_probs = mnb.predict_proba(z_df)
mnb_p_df = pd.DataFrame(mnb_predictions)
labeled_pred_mnb = [[val, mnb_p_df[0][i]] for i, val in enumerate(masked_df["Player"])]
labeled_prob_mnb = [[val, mnb_probs[i][1], mnb_p_df[0][i]] for i, val in enumerate(masked_df["Player"])]
sortedddd = Sort(labeled_prob_mnb)[::-1]
sortedddd_round = [[x, round(y, 4), z] for x,y,z in sortedddd]

final_mnb = sortedddd

with open("outcome/nb_outcomes.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(final_mnb)

#Scale Rebounder of the year by height