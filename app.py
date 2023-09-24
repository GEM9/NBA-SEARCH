
from flask import Flask, render_template, request
from nba_api import get_player, get_team 
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
    print(data)
    return render_template('result.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
