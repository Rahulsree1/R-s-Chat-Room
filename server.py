from flask import Flask
import json
app = Flask(__name__)
data = {
    'name':"Rahul",
    'age':19
}


jdata = json.dumps(data)


@app.route("/")
def test():
    return jdata








if __name__ == "__main__":
    app.run()