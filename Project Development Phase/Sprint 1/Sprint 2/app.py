from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Demo2')
def demo2():
    return render_template('Demo2.html')

@app.route('/chance')
def chance():
    return render_template('chance.html')

@app.route('/noChance')
def noChance():
    return render_template('noChance.html')


if __name__ == "__main__":
    app.run()
