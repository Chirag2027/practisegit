from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Hello route with a name parameter
@app.route('/hello/<name>')
def hello(name):  
    return f"Hello, {name}!"


# Route to demonstrate JSON response
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        "name": "FlaskApp",
        "version": "1.0",
        "features": ["Routing", "Templates", "JSON Responses"]
    }
    return jsonify(sample_data)

# Form handling route
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Form submitted! Hello, {name}!"
    return '''
        <form method="POST">
            Name: <input type="text" name="name">
            <input type="submit">
        </form>
    '''

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
