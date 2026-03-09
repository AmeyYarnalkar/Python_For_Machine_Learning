# Flask for Machine Learning 

## 1. What is Flask

**Flask** is a lightweight Python web framework used to create **web servers and APIs**.

In ML it is mainly used to **serve models**.

Typical ML workflow:

```
Client → Flask API → ML Model → Prediction → Client
```

Example:

```
Mobile App
     ↓
Flask API
     ↓
Model.predict()
     ↓
Return prediction (JSON)
```

Flask acts as the **bridge between the model and external applications**.

---

# 2. Creating a Flask Application

Basic structure of a Flask app.

```python
from flask import Flask

app = Flask(__name__)
```

Explanation:

* `Flask` → framework class
* `__name__` → helps Flask locate resources like templates and static files

`app` becomes the **server instance**.

---

# 3. Creating Routes (Endpoints)

A **route** maps a URL to a Python function.

Example:

```python
@app.route("/")
def greet():
    return "Welcome to the flask course"
```

Flow:

```
User → http://127.0.0.1:5000/
       ↓
Flask matches "/"
       ↓
greet() executes
       ↓
Response returned
```

Multiple routes can exist.

Example:

```python
@app.route("/about")
def about():
    return "This is the about page"

@app.route("/info")
def info():
    return "This is the info page"
```

Routing table conceptually:

```
/       → greet()
/about  → about()
/info   → info()
```

---

# 4. Running the Flask Server

Flask server starts using:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Explanation:

`if __name__ == "__main__"`

Ensures the server runs **only when the script is executed directly**.

`app.run()`

Starts the development server.

Default address:

```
http://127.0.0.1:5000
```

`debug=True` enables:

* automatic reload on code changes
* detailed error messages

---

# 5. HTTP Methods

HTTP requests have different methods.

Most important ones for ML APIs:

| Method | Purpose       |
| ------ | ------------- |
| GET    | Retrieve data |
| POST   | Send data     |

Example ML use case:

```
POST /predict
```

because the client sends **features for prediction**.

---

# 6. Creating a POST Endpoint

Example route that accepts POST requests.

```python
@app.route("/predict", methods=["POST"])
```

This tells Flask:

```
Only POST requests are allowed for this endpoint
```

---

# 7. Receiving JSON Data

Clients usually send data in **JSON format**.

Example request:

```json
{
 "num1": 4,
 "num2": 6
}
```

Flask reads JSON using:

```python
data = request.get_json()
```

Example extracted values:

```python
num1 = data["num1"]
num2 = data["num2"]
```

Optional safety check:

```python
if request.is_json:
```

---

# 8. Returning JSON Responses

APIs return responses in **JSON format**.

Example:

```python
return jsonify({"prediction": result}), 200
```

`jsonify()` converts Python dictionaries into **valid JSON responses**.

Example response:

```json
{
 "prediction": 10
}
```

---

# 9. Simulating Model Prediction

Instead of writing logic inside the route, use a separate function.

Example:

```python
def model_predict(num1, num2):
    return num1 * num2
```

This simulates an ML model.

---

# 10. ML API Structure

Typical ML Flask API flow:

```
Client sends features
        ↓
Flask receives JSON
        ↓
Extract features
        ↓
Call model_predict()
        ↓
Return prediction
```

Example route:

```python
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    num1 = data["num1"]
    num2 = data["num2"]

    result = model_predict(num1, num2)

    return jsonify({"prediction": result})
```

---

# 11. Complete Minimal ML Flask App

Example minimal API structure:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

def model_predict(num1, num2):
    return num1 * num2

@app.route("/")
def home():
    return "ML API running"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    num1 = data["num1"]
    num2 = data["num2"]

    result = model_predict(num1, num2)

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
```

---

# 12. Why Flask is Used in ML

Flask helps to:

* expose models as **APIs**
* allow **web apps or mobile apps to use ML models**
* integrate ML with **backend systems**

Typical architecture:

```
Frontend / Mobile App
        ↓
Flask API
        ↓
ML Model
        ↓
Prediction Response
```

---