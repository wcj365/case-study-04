#!/usr/bin/env python3

import string
import calendar
import random

import numpy as np
import pandas as pd


def get_months():
    
    return list(calendar.month_name)[1:] 


def generate_data(weights=(50,50), year="2020", to_csv=False):
    
    agencies = list(string.ascii_uppercase)

    months = list(calendar.month_name)[1:] 

    data = np.empty(shape=[len(agencies), len(months)])

    for i in range(len(agencies)):
        for j in range(len(months)):
            data[i,j] = random.choices([0,1], weights=weights)[0]

    df = pd.DataFrame(columns=months, data=data)

    df["Agency"] = agencies
    
    df["Year"] = year
    
    if to_csv:
        df.to_csv(year + ".csv")
        
    return df


if __name__ == "__main__":
    df = generate_data(to_csv=True)
    print(df)
    


