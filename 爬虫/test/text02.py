# -*- coding:utf-8 -*-
import pandas as pd
row = pd.DataFrame({
    "name":"liu",
    "age":'18'
})
row.to_csv("people.csv")