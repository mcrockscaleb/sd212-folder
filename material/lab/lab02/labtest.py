from flask import Flask, jsonify, request, render_template
import jinja2
import csv
import pandas as pd
import plotly.express as px

f = pd.read_csv('responses.csv')
df2 = pd.DataFrame(f)
counts = df2['planets'].value_counts()
print(counts)