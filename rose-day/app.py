from flask import Flask, render_template, request
import os
import re

app = Flask(__name__)

def clean_color(value):
    if re.fullmatch(r"#([0-9a-fA-F]{6})", value or ""):
        return value
    return "#E91E63"

@app.route("/")
def home():
    to = request.args.get("to", "Mehakuuuu")[:30]
    sender = request.args.get("from", "Arjun")[:30]
    msg = request.args.get("msg", "Wishing you a day as lovely as these roses.")[:160]
    theme = clean_color(request.args.get("theme"))
    show_music = request.args.get("music", "true").lower() == "true"

    return render_template(
        "index.html",
        to=to,
        sender=sender,
        msg=msg,
        theme=theme,
        show_music=show_music
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
