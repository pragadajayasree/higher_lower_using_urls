from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def func():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="300px">')


num = random.randint(0, 9)


@app.route("/<int:usernum>")
def check(usernum):
    if usernum == num:
        return ('<h1> correct guess</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="300px">')
    elif usernum < num:
        return ('<h1> too low  guess</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="300px">')
    else:
        return ('<h1> too high  guess</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="300px">')


if __name__ == "__main__":
    app.run(debug=True)
