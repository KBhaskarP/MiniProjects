from flask import Flask

app= Flask(__name__)
@app.route('/')
def initial():
    return "Hello, I am trying to learn Flask"

@app.route('/<name>')
def greetings(name):
    return f"Hello, {name} ! How are you?"

 

if __name__ == '__main__':
    app.run(debug=True)