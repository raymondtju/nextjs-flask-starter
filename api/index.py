from flask import Flask

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.exceptions import ConvergenceWarning
import json
import warnings
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
# import matplotlib.pyplot as plt
from pymongo import MongoClient 
warnings.filterwarnings("ignore", category=ConvergenceWarning)


number = 1

@app.route("/api/python")
def hello_world():
    return number

app = Flask(__name__)
