from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welkom bij het Inspire Offices Beheerportaal!</h1>" + \
             "<p>Onder andere Emir Ozcan, Musa Acer, Moh en Krijn.</p>"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)