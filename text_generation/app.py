from operator import ge
from flask import Flask, render_template, request
from utilities import send_text

# POSTING to the azure functions is working, need to implement
# the waiting for response methods

API_ENDPOINT = "http://localhost:7071/api/orchestrators/orchestrator-generation-test"

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    result = "Start typing your story"
    if request.method == 'POST':
        prompt = request.form['line']
        try:
            # result = generate_text(prompt, 50)
            response = send_text(prompt, API_ENDPOINT)
            # app.logger.info("Response: ", response.status_code())
            pass
        except:
            return "There has been an error"
    else:
        pass
    return render_template("index.html", content = result)

if __name__ == "__main__":
    app.run(debug=True)