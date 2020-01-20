# http://127.0.0.1:5000/home - home page
# http://127.0.0.1:5000/about - about page

from flask import Flask, render_template, jsonify, request
import WordCounter as wc


app = Flask(__name__)

# Rest
@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json
    p = wc.Print(text['text'].lower())
    return p.print()


# Home page route
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
