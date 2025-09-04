from re import findall


def paren_matches(tokens):
    length = len(tokens)
    matches = [0] * length
    paren_stack = []

    for i in range(length - 1, -1, -1):
        token = tokens[i]
        if token == ')':
            paren_stack.append(i)
        elif token == '(':
            matches[i] = paren_stack.pop()

    return matches


def evaluate(expr, start, end, parens):
    if start > end:
        return 0

    total = 0
    curr_op = '+'

    while start <= end:
        token = expr[start]
        if token == '+' or token == '-':
            curr_op = token
            start += 1
        else:
            if token == '(':
                paren_match = parens[start]
                curr_val = evaluate(expr, start + 1, paren_match - 1, parens)
                start = paren_match + 1
            else:
                curr_val = int(token)
                start += 1

            total += curr_val if curr_op == '+' else -curr_val

    return total


class Solution:
    def calculate(self, s: str) -> int:
        tokens = findall(r'[-+()]|\d+', s)
        parens = paren_matches(tokens)
        return evaluate(tokens, 0, len(tokens) - 1, parens)
