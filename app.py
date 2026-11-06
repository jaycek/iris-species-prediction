from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("iris_model.pkl")

flower_names = ["setosa", "versicolor", "virginica"]

# Image filename for each flower
flower_images = {
    "setosa": "images/setosa.jpg",
    "versicolor": "images/versicolor.jpg",
    "virginica": "images/virginica.jpg"
}


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    flower_image = None

    if request.method == "POST":

        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        input_data = [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]]

        # Predict flower class
        result = model.predict(input_data)

        # Convert class number to flower name
        prediction = flower_names[int(result[0])]

        # Select matching flower image
        flower_image = flower_images[prediction]

    return render_template(
        "index.html",
        prediction=prediction,
        flower_image=flower_image
    )


if __name__ == "__main__":
    app.run(debug=True)