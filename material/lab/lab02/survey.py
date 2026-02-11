# SD212 Survey lab

from flask import Flask, jsonify, request, render_template
import jinja2
import csv
import pandas as pd
import plotly.express as px

app = Flask(__name__, template_folder='.')
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route('/hello')
def hello():
    return "are there more wheels or doors in this world?\n"

@app.route('/questions')
def questions():
    questions_dict = {
        'name': 'Caleb',
        'questions': [
            {
                'key': 'space',
                'prompt': 'What is one word you would use to describe outer space?'
            },
            {
                'key': 'planets',
                'prompt': 'If you could live on any planet other than Earth, which one would it be?',
                'choices': [
                'Mercury', 
                'Venus',
                'Mars',
                'Jupiter',
                'Saturn',
                'Uranus',
                'Neptune',
                'Pluto'
                ],
            },
            {
                'key': 'stars',
                'prompt': 'Have you ever seen a shooting star?',
                'choices': [
                'Yes',
                'No'
                ],
            }
        ]
    }

    return jsonify(questions_dict)

@app.route('/survey')
def survey():
    return render_template("survey-template.html", info=questions().get_json())


@app.route('/answer', methods=['POST'])
def answer():
    print("vvvvvvvvvvvvvv DICTIONARY vvvvvvvvvvvvvvv")
    print(dict(request.form))
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    
    answers = dict(request.form)

    for key, value in answers.items():
        if not value:
            return "Invalid response. Please fill out all fields."
        else:
            with open('responses.csv', 'a', newline='') as f:
                fieldnames = request.form.keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerow(request.form)

            name = request.form['name']

            return f"Thank you {name}, your response was recorded!"

@app.route('/visual')
def visual():
    # ... create a dataframe called df
    f = pd.read_csv('responses.csv')
    df2 = pd.DataFrame(f)
    counts = df2['planets'].value_counts().reset_index()
    counts.columns = ['planets', 'count']
    fig = px.bar(counts, x='planets', y='count')
    return fig.to_html()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11134, debug=True, threaded=False)
