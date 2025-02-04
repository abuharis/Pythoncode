from flask import Flask, render_template, request

app = Flask(__name__)


#validation of inputs passed as post form from web ui. This is used inside the index route
def validate_inputs(name, age, email):
    errors = []
    if not name.replace(" ", "").isalpha():
        errors.append("Name should contain only letters and spaces.")
    if not age.isdigit() or not int(age) >= 18:
        errors.append("Only customers above 18 years old are allowed.")
    if "@" not in email or "." not in email:
        errors.append("Invalid email format.")
    
    return errors

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"].strip().capitalize()
        age = request.form["age"].strip()
        email = request.form["email"].strip()

        #The error is caught into a variables and passed into html using render_template along with the inputs
        errors = validate_inputs(name, age, email)

        if errors:
            return render_template("index.html", errors=errors, name=name, age=age, email=email)

        return render_template("success.html", name=name, age=age, email=email)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
