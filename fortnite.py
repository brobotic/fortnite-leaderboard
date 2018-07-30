from app import app, db
from app.models import Stats
import requests
import json
from time import sleep

@app.shell_context_processor
def make_shell_context():
        return {'db': db, 'Stats': Stats}

# For Windows
if __name__ == "__main__":
    app.run(host='0.0.0.0')
