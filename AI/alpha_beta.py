def alphabeta(node, depth, alpha, beta, maximizingPlayer, tree):
    if depth == 0 or node not in tree:
        return node  # leaf node value

    if maximizingPlayer:
        maxEval = float('-inf')
        for child in tree[node]:
            eval = alphabeta(child, depth-1, alpha, beta, False, tree)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for child in tree[node]:
            eval = alphabeta(child, depth-1, alpha, beta, True, tree)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

# Example tree: dictionary where leaves are values
tree = {
    'A': ['B', 'C'],
    'B': [3, 5],
    'C': [6, 9]
}

# Run Alpha-Beta starting from MAX at root 'A'
result = alphabeta('A', 2, float('-inf'), float('inf'), True, tree)
print("Optimal value:", result)
