from flask import Flask, render_template

app = Flask(__name__)

# Disable caching so Flask always serves the newest HTML template changes
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)