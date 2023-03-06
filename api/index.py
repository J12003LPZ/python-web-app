# flask_app.py

from flask import Flask

app = Flask(__name__)


@app.route('/')
def run_desktop_app():
    import subprocess
    result = subprocess.check_output(['python', './hello.py'])
    return result


if __name__ == '__main__':
    app.run()
