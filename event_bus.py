events = []

def push(event):
    events.append(event)

def pull():
    return events[-100:]
