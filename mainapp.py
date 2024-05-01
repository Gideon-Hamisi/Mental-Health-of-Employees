import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('mentalhealthdataset.csv')

st.title('Prediction of the Mental Health of Employees')
st.write("""
# Mental Health of Employees App
This app predicts the **Mental Health of Employees** """)
