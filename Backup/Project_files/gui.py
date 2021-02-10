import streamlit as st
from pridiction import *
from pridict import *
from selenium import webdriver
from Scraper import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm, skew
from dbcreater import *
st.title("Instagram Dashboard")
data = pd.read_csv("kind.csv")
df = data.groupby(['Username'])['No. of Post','following','followers','Likes','No of Tags','Comments Counts','is Verified','is Private','bussiness','new_user'].mean()
df['is Verified'] = df['is Verified'].astype(int)
df['is Private'] = df['is Private'].astype(int)
df['is Private'] = df['is Private'].astype(int)
df['bussiness'] = df['bussiness'].astype(int)
df['new_user'] = df['new_user'].astype(int)
df['Likes']=np.log1p(df['Likes'])
# try:
#     browser.title
# except:
#     browser = webdriver.Chrome('D:/Web Driver/chromedriver.exe')
#     cdrive()
st.subheader("Collect fresh New Data")
if st.button("Collect"):
    st.warning("This May Cause some error while doing this")
    st.warning("Just refresh the page the data will be collected and loaded")
    cdb()
    st.success("Done")
st.write("  ")
st.subheader("Train New Models")
if st.button("Train"):
    pred()
text = st.text_input("Enter a IG Username")
if st.button("Submit"):
    uname = text
    print(uname)
    # uname
    # cdrive()
    # print ("title",browser.title)
    pre = rslt(uname)
    like = pre[0]
    comment = pre[1]
    follower = pre[2]
    verified = pre[3]
    private = pre[4]
    st.write("Pridicted Likes on next post of",uname,like)
    st.write("Pridicted Comments on next post of",uname,comment)
    st.write("Pridicted number of followers after six months",uname,follower)
    st.write("Is user",uname,"verified (pridiction)",verified)
    st.write("Is user",uname,"private (pridiction)",private)
st.subheader("Dataset")
if st.button("Show Data"):
    df

st.subheader("Dataset Overview")
if st.button("Show"):
    st.write(
    """
    Pair Plot for dataset
    """
    )
    sns.pairplot(df)
    st.pyplot()
    st.write(
    """
    Heatmap for dataset
    """
    )
    sns.heatmap(df.corr(), annot = True)
    st.pyplot()


st.subheader("Like Distribution for all username in dataset")
if st.button("Show Like Distribution"):
    sns.distplot(df['Likes'] , fit=norm);
    st.pyplot()
    # Get the fitted parameters used by the function
    (mu, sigma) = norm.fit(df['Likes'])
    st.write( '\n mu = {:.2f} and sigma = {:.2f}\n'.format(mu, sigma))

    #Now plot the distribution
    plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)],loc='best')
    plt.ylabel('Frequency')
    plt.title('Likes distribution')
    #Get also the QQ-plot
    fig = plt.figure()
    res = stats.probplot(df['Likes'], plot=plt)
    plt.show()
    st.pyplot()

st.subheader("Followers Distribution for all username in dataset")
#We use the numpy fuction log1p which  applies log(1+x) to all elements of the column
if st.button("Show Followers Distribution"):
    df["followers"] = np.log1p(df["followers"])

    #Check the new distribution
    sns.distplot(df['followers'] , fit=norm);
    st.pyplot()
    # Get the fitted parameters used by the function
    (mu, sigma) = norm.fit(df['followers'])
    st.write( '\n mu = {:.2f} and sigma = {:.2f}\n'.format(mu, sigma))

    #Now plot the distribution
    plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)],
                loc='best')
    plt.ylabel('Frequency')
    plt.title('followers distribution')

    #Get also the QQ-plot
    fig = plt.figure()
    res = stats.probplot(df['followers'], plot=plt)
    plt.show()
    st.pyplot()

    sns.set_style('whitegrid')
    sns.lmplot(x = 'followers', y ='Likes', data = df)
    st.pyplot()

# *********************************************
st.subheader("Posts Distribution for all username in dataset")
if st.button("Show Posts Distrbution"):
#We use the numpy fuction log1p which  applies log(1+x) to all elements of the column
    df["No. of Post"] = np.log1p(df["No. of Post"])

    #Check the new distribution
    sns.distplot(df['No. of Post'] , fit=norm);
    st.pyplot()
    # Get the fitted parameters used by the function
    (mu, sigma) = norm.fit(df['No. of Post'])
    st.write( '\n mu = {:.2f} and sigma = {:.2f}\n'.format(mu, sigma))

    #Now plot the distribution
    plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)],
                loc='best')
    plt.ylabel('Frequency')
    plt.title('No. of Post distribution')

    #Get also the QQ-plot
    fig = plt.figure()
    res = stats.probplot(df['No. of Post'], plot=plt)
    plt.show()
    st.pyplot()

# ******************************
st.subheader("Following Distribution for all username in dataset")
if st.button("Show Following Distrbution"):
    #We use the numpy fuction log1p which  applies log(1+x) to all elements of the column
    df["following"] = np.log1p(df["following"])

    #Check the new distribution
    sns.distplot(df['following'] , fit=norm);
    st.pyplot()
    # Get the fitted parameters used by the function
    (mu, sigma) = norm.fit(df['following'])
    st.write( '\n mu = {:.2f} and sigma = {:.2f}\n'.format(mu, sigma))

    #Now plot the distribution
    plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)],
                loc='best')
    plt.ylabel('Frequency')
    plt.title('following distribution')

    #Get also the QQ-plot
    fig = plt.figure()
    res = stats.probplot(df['following'], plot=plt)
    plt.show()
    st.pyplot()
    # *****************************************
