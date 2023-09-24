# app.py

from flask import Flask, render_template, request
app = Flask(__name__)

# app.py

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    id = request.form['id']
    type = request.form['type']  # player or team
    if type == 'player':
        data = get_player(id)
    elif type == 'team':
        data = get_team(id)
    return render_template('result.html', data=data)
