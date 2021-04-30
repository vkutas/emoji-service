"""Complex Enterprise Grade Flask Web App which can provide your with nothing interesting"""

import random
from flask import Flask, render_template
from flask import request
import emoji

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    """Say Hi to user whom accidentally come across this site"""
    return "<h1 style='color:#323232'>Welcome to Enterprise Emoji Service!</h1>"

@app.route("/say_hello")
def say_hello():
    """Just print 'Hellow World!' and used as example of useless doc or comment"""
    return "Hello World!"

@app.route('/', methods=['GET', 'POST'])
def emoji_service():
    """Heart of the app.
    If recieved GET http request this method returns ugly home page,
    while if recieved POST it returns too wired string to discribe here.
    See emoji_provider func for more details.
    """
    if request.method == 'POST':
        content = request.get_json(force=True)
        return emoji_provider(content)
    return render_template('greeting.html', url = request.url)

def emoji_provider(emoji_desc):
    """ Take a dict of format {word: 'name', count: n} and
    return string which consists of 'name' repeated 'n' times using emoji which name
    is equal to 'name' as delimeter.
    If there is no emoji with name 'name', random emoji is used instead.

    Parameters
        ----------
        emoji_desc : dict
            Dict of format {word: 'name', count: n}
     """
    name = emoji_desc['word']
    count = emoji_desc['count']
    emoji_name = ':' + name + ':'
    emoji_icon = emoji.emojize(emoji_name, use_aliases = True)
    if emoji_icon == emoji_name:
        emoji_icon = random.choice(list(emoji.EMOJI_UNICODE_ENGLISH.values()))
    if not isinstance(count, int):
        count = random.randint(1, 10)
    response_body = emoji_icon
    for i in range(count):
        response_body += name + emoji_icon
    return response_body

@app.errorhandler(404)
def page_not_found(error_code):
    """Custom 404 Page """
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error_code):
    """Custom 500 Page """
    return render_template('500.html'), 500

def main():
    """App entry point """
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
