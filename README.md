# Iris Species Prediction – Machine Learning Web App

A machine learning web application that predicts the species of an Iris flower from its measurements. The project combines a Random Forest Classifier built with `scikit-learn` and a Flask web interface.

Users enter the flower measurements through an HTML form, and the application displays the predicted Iris species.

---

## Features

- Predicts an Iris flower species using a trained Random Forest Classifier.
- Accepts flower measurements through a web form.
- Loads the trained machine learning model using `joblib`.
- Uses Flask to handle form submissions and prediction requests.
- Renders dynamic pages with the Jinja2 template engine.
- Uses HTML and CSS to create and style the user interface.

---

## Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python** | Application and machine learning logic |
| **Flask** | Web framework |
| **scikit-learn** | Machine learning model and prediction |
| **Random Forest Classifier** | Classification algorithm |
| **joblib** | Saving and loading the trained model |
| **HTML** | Web page structure |
| **CSS** | User interface styling |
| **Jinja2** | Dynamic HTML templates |

---

## Iris Measurements

The model uses four measurements as input:

1. **Sepal length**
2. **Sepal width**
3. **Petal length**
4. **Petal width**

The classifier predicts one of the three Iris species:

- `Iris-setosa`
- `Iris-versicolor`
- `Iris-virginica`

---

## How It Works

1. A Random Forest Classifier is trained using the Iris dataset with `scikit-learn`.
2. The trained model is saved to a file using `joblib`.
3. Flask loads the saved model when the web application starts.
4. The user enters the four flower measurements in the web form.
5. Flask passes the input values to the model for prediction.
6. The predicted species is displayed on the web page using a Jinja2 template.

---

## Run Locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd iris_species_production
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install Flask scikit-learn joblib
```

If a `requirements.txt` file is included:
```bash
pip install -r requirements.txt
```

### 4. Start the Flask application

```bash
python app.py
```
*(If your application entry-point file has a different name, replace `app.py` with that filename.)*

Open the local URL shown in the terminal, typically:
```text
http://127.0.0.1:5000/
```

---

## Model File

The application uses a model previously trained with `scikit-learn` and saved using `joblib`. Ensure the saved model file is available at the path expected by the Flask application.

> **Note:** Only load `joblib` model files from trusted sources.

---

## Deployment

The application was deployed using pythonanywhere.com
Link: https://www.pythonanywhere.com/


## Project Learning Outcomes

- Understanding supervised machine learning classification.
- Training and using a Random Forest Classifier.
- Saving and loading machine learning models with `joblib`.
- Integrating a `scikit-learn` model into a Flask application.
- Collecting user input through HTML forms.
- Passing data from Flask routes to Jinja2 templates.
- Displaying prediction results dynamically.
- Separating application logic, templates, and CSS styling.

---

*Built as a hands-on project to demonstrate how a trained machine learning model can be integrated into a Python web application.*
