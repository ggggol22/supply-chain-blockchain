from flask import Flask, render_template, request
from blockchain import Blockchain

app = Flask(__name__)
bc = Blockchain()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        product = request.form.get("product")
        origin = request.form.get("origin")
        destination = request.form.get("destination")

        if product and origin and destination:
            bc.add_block({
                "product": product,
                "from": origin,
                "to": destination
            })

    return render_template("index.html", chain=bc.chain)

if __name__ == "__main__":
    app.run(debug=True)