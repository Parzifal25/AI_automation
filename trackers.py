import pandas as pd
import datetime

def log_gym(workout):

    date = datetime.date.today()

    df = pd.DataFrame([[date, workout]], columns=["date","workout"])

    df.to_csv("data/gym_log.csv", mode="a", header=False, index=False)


def log_learning(task):

    date = datetime.date.today()

    df = pd.DataFrame([[date, task]], columns=["date","task"])

    df.to_csv("data/learning_log.csv", mode="a", header=False, index=False)