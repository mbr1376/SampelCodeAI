# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:26:41 2020

@author: mohamad
"""

import pandas as pd
import matplotlib.pyplot as plt



if __name__=="__main__":
    col_list=["GrLivArea","BedroomAbvGr","1stFlrSF","2ndFlrSF","SalePrice"];
    df = pd.read_csv('train.csv',usecols=col_list)


    plt.plot(df["SalePrice"],df["GrLivArea"],'bo')
    plt.xlabel('SalePrice')
    plt.ylabel('Area Gneral')
    plt.figure()
    plt.plot(df["SalePrice"],df["BedroomAbvGr"],'ro')
    plt.xlabel('SalePrice')
    plt.ylabel('NumberBedroom')
    plt.figure()
    plt.plot(df["1stFlrSF"],df["2ndFlrSF"],'go')
    plt.xlabel('First Floor')
    plt.ylabel('Secend Floor')
    plt.show()