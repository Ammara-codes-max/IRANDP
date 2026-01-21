risk_history = []

def add_risk(value):
    risk_history.append(value)
    if len(risk_history) > 30:
        risk_history.pop(0)

def get_history():
    return risk_history if risk_history else [0]
