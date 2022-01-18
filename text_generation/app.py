from operator import ge
from flask import Flask, render_template, request
from utilities import generate_text

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    result = "Start typing your story"
    if request.method == 'POST':
        prompt = request.form['line']
        try:
            result = generate_text(prompt, 50)
        except:
            return "There has been an error"
    else:
        pass
    return render_template("index.html", content = result)

if __name__ == "__main__":
    app.run()