from flask import Flask, render_template, request

from digital_signature import generate_keys, sign_message, verify_message


app = Flask(__name__)

generate_keys()


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    original_text = ""
    received_text = ""

    if request.method == "POST":
        original_text = request.form.get("original_message", "").strip()
        received_text = request.form.get("received_message", "").strip()
        signature = sign_message(original_text.encode("utf-8"))
        is_valid = verify_message(
            received_text.encode("utf-8"),
            signature
        )

        if is_valid:
            result = "valid"
        else:
            result = "fake"

    return render_template(
        "index.html",
        result=result,
        original_text=original_text,
        received_text=received_text
    )


if __name__ == "__main__":
    app.run(debug=True) 