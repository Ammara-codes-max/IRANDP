
risk = 100

def degrade(score):
    global risk
    risk = max(0, risk - score)

def improve(score):
    global risk
    risk = min(100, risk + score)

def get_risk():
    return risk
