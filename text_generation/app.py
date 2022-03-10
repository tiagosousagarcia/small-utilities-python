from operator import ge
from flask import Flask, render_template, request
# from utilities import send_text
from apiTest import start_generation
import logging, sys

# App is now working at a basic level. Need to implement loading screen

# Logging setup

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", handlers=[logging.FileHandler("app-debug.log"), logging.StreamHandler(sys.stdout)])

API_ENDPOINT = "http://localhost:7071/api/orchestrators/orchestrator-generation-test"

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    response = "Start typing your story"
    if request.method == 'POST':
        prompt = request.form['line']
        try:
            # result = generate_text(prompt, 50)
            response, status = start_generation(prompt, API_ENDPOINT)
            if response == "":
                app.logger.info("Response: ", status)
                response = "I'm sorry, something went wrong"
            pass
        except:
            return "There has been an error"
    else:
        pass
    return render_template("index.html", content = response)

if __name__ == "__main__":
    app.run(debug=True)