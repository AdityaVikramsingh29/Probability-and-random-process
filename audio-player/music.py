from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def music_player():
    return render_template('music2.html')

if __name__ == '__main__':
    app.run(debug=True)