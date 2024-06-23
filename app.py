from flask import Flask, request, render_template  # Modified import here
import ast
import operator as op

# Define allowed operators for safe evaluation
allowed_operators = {
    ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
    ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
    ast.USub: op.neg
}

def safe_eval(expr):
    """
    Safely evaluate an arithmetic expression using AST.
    """
    def eval_(node):
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            return allowed_operators[type(node.op)](eval_(node.left), eval_(node.right))
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
            return allowed_operators[type(node.op)](eval_(node.operand))
        else:
            raise TypeError(node)
    
    return eval_(ast.parse(expr, mode='eval').body)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    result = ""
    if request.method == 'POST':
        expression = request.form['expression']
        try:
            # Evaluate the expression safely
            result = safe_eval(expression)
        except Exception as e:
            # Handle any errors that occur during evaluation
            result = f"Error: {str(e)}"
    # Render the template, whether it's a GET request or a POST request with the result
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)