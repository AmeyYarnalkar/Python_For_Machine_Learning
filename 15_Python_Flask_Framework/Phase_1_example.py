from flask import Flask, request, jsonify

# `app = Flask(__name__)` creates a new Flask application instance. The `__name__` variable is a
# special Python variable that holds the name of the current module. When you pass `__name__` to the
# Flask constructor, it helps Flask to determine the root path of the application, which is necessary
# for locating resources like templates and static files.

def process(num1, num2):
    return num1 * num2

app = Flask(__name__)

@app.route("/")
def greet():
    return "Welcome to the flask course"

@app.route("/about")
def about():
    return "This is the about page"

@app.route("/info")
def info():
    return "this is the info page"

@app.route("/predict", methods=["POST"])
def predict():
     if request.is_json:
         data = request.get_json()
         print(f"Received JSON: {data}")
         result = process(data["num1"], data["num2"])
         return jsonify({"message": "JSON processed successfully", "Your Prediction": result}), 200
     else:
         return "Content type is not supported.", 400

if __name__ == "__main__": #entry point
    app.run(debug=True)