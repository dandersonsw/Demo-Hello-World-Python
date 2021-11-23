from flask import Flask, render_template, Markup
import os

app = Flask(__name__)

port = int(os.getenv('PORT', 8080))

content = "<h1>Hello, world!</h1>"
content = Markup(content)


@app.route('/')
def hello_world():
    return render_template("index.html", content=content)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
