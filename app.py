import base64
from flask import Flask, render_template, request

from digital_signature import (
    decrypt_message,
    encrypt_message,
    generate_keys,
    sign_message,
    verify_message,
)


app = Flask(__name__)

generate_keys()


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    original_text = ""
    received_text = ""
    encrypted_text = ""
    decrypted_text = ""

    if request.method == "POST":
        action = request.form.get("action")

        original_text = request.form.get("original_message", "").strip()
        received_text = request.form.get("received_message", "").strip()

        if action == "verify":
            signature = sign_message(original_text.encode("utf-8"))

            is_valid = verify_message(
                received_text.encode("utf-8"),
                signature
            )

            result = "valid" if is_valid else "fake"

        elif action == "encrypt":
            encrypted_bytes = encrypt_message(
                original_text.encode("utf-8")
            )

            encrypted_text = base64.b64encode(
                encrypted_bytes
            ).decode("utf-8")

            decrypted_text = decrypt_message(
                encrypted_bytes
            ).decode("utf-8")

    return render_template(
        "index.html",
        result=result,
        original_text=original_text,
        received_text=received_text,
        encrypted_text=encrypted_text,
        decrypted_text=decrypted_text
    ) 


if __name__ == "__main__":
    app.run(debug=True) 
    