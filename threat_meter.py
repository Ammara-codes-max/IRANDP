history = []
risk = 0

def add_risk(v):
    global risk
    risk += v
    if risk < 0:
        risk = 0
    if risk > 100:
        risk = 100
    history.append(risk)

def get_score():
    return risk

def get_history():
    return history[-50:]
