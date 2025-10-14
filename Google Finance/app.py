from flask import Flask, render_template, request

app = Flask(__name__)

with open("deneme.txt",encoding="UTF-8") as text:
    deneme = text.read()

@app.route("/")
def home():
    return render_template("index.html", metin = deneme)

@app.route('/gonder', methods = ['POST'])
def submit():
    name = request.form.get('name')
    surname = request.form.get('surname')
    result = f"{name} {surname}"
    return render_template("index.html", metin = result)


if __name__ == "__main__":
    app.run(debug=True)