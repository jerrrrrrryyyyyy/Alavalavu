from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__, static_folder='static')

length_measurements= {
    "pazhampori": 15,
    "kadukk": 0.02,
    "vaazhayela": 40,
    "urumb": 0.04,
    "Chenda": 50,
    "kurumulakku": 0.03,
    "nendrapazham": 22,
    "Kanan Devan Chayapodi": 17,
    "Poothiri": 14,
    "Mammootyude Meesha": 0.3,
}
weight_measurements= {
    "aanapindam": 2.5,
    "avalosunda": 0.025,
    "chakka": 15,
    "pothichor": 0.6,
    "uppilitta maanga": 0.27,
    "porotta": 0.08,
    "Vidya record book": 0.3,
    "mottapupps": 0.15,
    "Onam sadhya": 1.2,
    "chakkakuru": 0.007,
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            name = request.form["name"]
            height_cm = float(request.form["height"])
            weight_kg = float(request.form["weight"])
            
            return redirect(url_for("results", h=height_cm, w=weight_kg, n=name))
        except (ValueError, KeyError):
            return render_template("index.html", error="Please enter valid data.")
    return render_template("index.html")

@app.route("/results")
def results():
    try:
        height_cm = float(request.args.get("h"))
        weight_kg = float(request.args.get("w"))
        name = request.args.get("n")
        
        random_length_item_name = random.choice(list(length_measurements.keys()))
        random_weight_item_name = random.choice(list(weight_measurements.keys()))

        length_value = length_measurements[random_length_item_name]
        weight_value = weight_measurements[random_weight_item_name]

        new_height_units = height_cm / length_value
        new_weight_units = weight_kg / weight_value

        return render_template(
            "results.html",
            name=name,
            height=f"{new_height_units:.2f}",
            height_item=random_length_item_name,
            weight=f"{new_weight_units:.2f}",
            weight_item=random_weight_item_name
        )
    except (ValueError, TypeError):
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)