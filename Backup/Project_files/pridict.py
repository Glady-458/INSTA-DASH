import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle
from pridiction import *
from scipy import stats
from scipy.stats import norm, skew
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import streamlit as st
def pred():
    DB = pd.read_csv("kind.csv")
    data = DB.groupby(['Username'])['No. of Post','following','followers','Likes','No of Tags','Comments Counts','is Verified','is Private','bussiness','new_user'].mean()
    data.reset_index(drop=True,inplace=True)
    data['No of Tags'] = round(data['No of Tags'])
    data['Comments Counts'] = np.log1p(data['Comments Counts'])
    data["Likes"] = np.log1p(data["Likes"])
    data["followers"] = np.log1p(data["followers"])
    data["No. of Post"] = np.log1p(data["No. of Post"])
    data["following"] = np.log1p(data["following"])

    #************pridict likes
    # print(data.head())
    train = data.drop(['Likes','new_user','bussiness'], axis=1)
    # print(train.head())
    test = data['Likes']
    X_train, X_test, y_train, y_test = train_test_split(train,test,test_size=0.1, random_state=1)
    regs = LinearRegression(normalize=True)
    regs.fit(X_train, y_train)
    x_pred = regs.predict(X_train)
    y_pred = regs.predict(X_test)
    st.write("like Accuracy",r2_score(y_test,y_pred))
    pickle.dump(regs, open('likes.pkl','wb'))
    #************pridict likes with GradientBoostingClassifier
    # reg = GradientBoostingRegressor(random_state=1)
    # reg.fit(X_train,y_train)
    # y_pred = reg.predict(X_test)
    # st.write("Like Accuracy with gbc",r2_score(y_test, y_pred))
    # pickle.dump(reg, open('likes.pkl','wb'))

    #pridict comment counts
    train = data.drop(['Comments Counts','new_user','bussiness'], axis=1)
    # print(train.head())
    test = data['Comments Counts']
    X_train, X_test, y_train, y_test = train_test_split(train,test,test_size=0.1, random_state=1)
    regs = LinearRegression(normalize=True)
    regs.fit(X_train, y_train)
    x_pred = regs.predict(X_train)
    y_pred = regs.predict(X_test)
    st.write("Comment Accuracy",r2_score(y_test,y_pred))
    pickle.dump(regs, open('Comments.pkl','wb'))

    #pridict folloers count
    train = data.drop(['followers'], axis=1)
    test = data['followers']
    X_train, X_test, y_train, y_test = train_test_split(train,test,test_size=0.1, random_state=1)
    regs = LinearRegression(normalize=True)
    regs.fit(X_train, y_train)
    x_pred = regs.predict(X_train)
    y_pred = regs.predict(X_test)
    st.write("followers Accuracy",r2_score(y_test,y_pred))
    pickle.dump(regs, open('followers.pkl','wb'))

    #pridict account Verified
    train = data.drop(['is Verified','No of Tags','Comments Counts','bussiness','new_user'], axis=1)
    test = data['is Verified']
    X_train, X_test, y_train, y_test = train_test_split(train,test,test_size=0.1, random_state=1)
    regs = LinearRegression(normalize=True)
    regs.fit(X_train, y_train)
    x_pred = regs.predict(X_train)
    y_pred = regs.predict(X_test)
    st.write("Verified Accuracy",r2_score(y_test,y_pred))
    pickle.dump(regs, open('verified.pkl','wb'))

    train = data.drop(['is Private'], axis=1)
    test = data['is Private']
    X_train, X_test, y_train, y_test = train_test_split(train,test,test_size=0.1, random_state=1)
    regs = LinearRegression(normalize=True)
    regs.fit(X_train, y_train)
    x_pred = regs.predict(X_train)
    y_pred = regs.predict(X_test)
    st.write("Private Accuracy",r2_score(y_test,y_pred))
    pickle.dump(regs, open('private.pkl','wb'))

# pred()

# for i in range(0,10):
#     print(i)
# pdinst("11sh25")
# p = np.log(3)
# fg = np.log(60)
# fw = np.log(11)
# t = 1
# c = 1
# v = 0
# pr =0
#t = 0
def rslt(uname):
    # cdrive()
    DB1 = pdinst(uname)
    # DB1['is Verified'] = DB1['is Verified'].astype(int)
    # DB1['is Private'] = DB1['is Private'].astype(int)
    # DB1['bussiness'] = DB1['bussiness'].astype(int)
    # DB1['new_user'] = DB1['new_user'].astype(int)
    data = DB1.groupby(['Username'])['No. of Post','following','followers','Likes','No of Tags','Comments Counts','is Verified','is Private','bussiness','new_user'].mean()
    data.reset_index(drop=True,inplace=True)
    # print(data.iloc[0])
    data['No of Tags'] = round(data['No of Tags'])
    data['Comments Counts'] = np.log1p(data['Comments Counts'])
    data["Likes"] = np.log1p(data["Likes"])
    data["followers"] = np.log1p(data["followers"])
    data["No. of Post"] = np.log1p(data["No. of Post"])
    data["following"] = np.log1p(data["following"])

    sample = data.drop(['Likes','new_user','bussiness'], axis=1)
    # print(DB1.iloc[0])
    # [DB1['No. of Post'].iloc[0],DB1['following'].iloc[0],DB1['followers'].iloc[0],DB1['No of Tags'].iloc[0],DB1['Comments Counts'].iloc[0],DB1['is Verified'].iloc[0].astype(int),DB1['is Private'].iloc[0].astype(int)]
    arrray = sample.iloc[0].values
    # print(arrray)
    #sample = sc.transform(sample)

    # Loading model to compare the results
    model = pickle.load(open('likes.pkl','rb'))
    PV = np.exp(model.predict(arrray.reshape(1, -1)))
    # print("next post like",int(round(PV[0])))
    A = int(round(PV[0]))



    sample = data.drop(['Comments Counts','new_user','bussiness'], axis=1)
    arrray = sample.iloc[0].values
    # print(arrray)
    model = pickle.load(open('Comments.pkl','rb'))
    PV = np.exp(model.predict(arrray.reshape(1, -1)))
    # print("next post comments",int(round(PV[0])))
    B = int(round(PV[0]))

    sample = data.drop(['followers'], axis=1)
    arrray = sample.iloc[0].values
    # print(arrray)
    model = pickle.load(open('followers.pkl','rb'))
    PV = np.exp(model.predict(arrray.reshape(1, -1)))
    # print("Follower growth",int(round(PV[0])))
    C = int(round(PV[0]))
    #
    sample = data.drop(['is Verified','No of Tags','Comments Counts','bussiness','new_user'], axis=1)
    arrray = sample.iloc[0].values
    # print(arrray)
    model = pickle.load(open('verified.pkl','rb'))
    PV = np.exp(model.predict(arrray.reshape(1, -1)))
    # print("is the user verified",bool(round(PV[0]-1)))
    D = bool(round(PV[0]-1))

    sample = data.drop(['is Private'], axis=1)
    arrray = sample.iloc[0].values
    # print(arrray)
    model = pickle.load(open('private.pkl','rb'))
    PV = np.exp(model.predict(arrray.reshape(1, -1)))
    # print("is the user Private",bool(round(PV[0]-1)))
    E = bool(round(PV[0]-1))

    return A,B,C,D,E
    # browser.quit()
# rslt("subhojitjana")
