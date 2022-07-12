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

        
def gradient_descent(x1, x2, x3, y, iterations, learning_rate):
    m1_curr = m2_curr = m3_curr = b_curr = 0
    n = len(x1)
    for i in range(iterations):
        y_pred = m1_curr*x1 + m2_curr*x2 + m3_curr*x3 + b_curr
        cost = (1/n) * sum([val**2 for val in (y - y_pred)])
        dm1 = -(2/n) * sum(x1*(y - y_pred))
        dm2 = -(2/n) * sum(x2*(y - y_pred))
        dm3 = -(2/n) * sum(x3*(y - y_pred))
        db = -(2/n) * sum((y - y_pred))
        m1_curr = m1_curr - learning_rate * dm1
        m2_curr = m2_curr - learning_rate * dm2
        m3_curr = m3_curr - learning_rate * dm3
        b_curr = b_curr - learning_rate * db 
        print(f'm1 {m1_curr} m2 {m2_curr} m3 {m3_curr} b {b_curr} iterations {i} cost {cost} learning_rate {learning_rate}')
