# Put your app in here.
from flask import Flask, request

app = Flask(__name__)


# A helper function that processes the math operation. This avoids hardcoding the operation directly into the route.
def calculate(operation, a, b):
    """Performs the specified operation on a and b."""
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mult":
        return a * b
    elif operation == "div":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"


# Each route: Calls the calculate() function with the appropriate operation, retrieves the result, and returns it as a string.
@app.route('/add')
def add():
    a = int(request.args.get("a")) #Retrieves the query parameter a from the URL 
    b = int(request.args.get("b"))
    result = calculate("add", a, b)
    return str(result)

@app.route('/sub')
def sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = calculate("sub", a, b)
    return str(result)

@app.route('/mult')
def mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = calculate("mult", a, b)
    return str(result)

@app.route('/div')
def div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = calculate("div", a, b)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)