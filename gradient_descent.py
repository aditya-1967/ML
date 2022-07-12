x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.02

    for i in range(iterations):
        y_pred = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y - y_pred)])
        dm = -(2/n) * sum(x*(y - y_pred))
        db = -(2/n) * sum((y - y_pred))
        m_curr = m_curr - learning_rate * dm
        b_curr = b_curr - learning_rate * db
        print(f'm {m_curr} b {b_curr} iterations {i} cost {cost}')
