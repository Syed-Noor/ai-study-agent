import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}


def calculate(expression: str):
    """
    Safely evaluate basic mathematical expressions.
    """

    try:
        tree = ast.parse(expression, mode="eval")
        result = evaluate_node(tree.body)
        return str(result)

    except Exception as e:
        return f"Calculation error: {str(e)}"


def evaluate_node(node):

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

    if isinstance(node, ast.BinOp):
        left = evaluate_node(node.left)
        right = evaluate_node(node.right)

        operation = OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Unsupported operator")

        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        operand = evaluate_node(node.operand)

        if isinstance(node.op, ast.USub):
            return -operand

        if isinstance(node.op, ast.UAdd):
            return operand

    raise ValueError("Invalid mathematical expression")