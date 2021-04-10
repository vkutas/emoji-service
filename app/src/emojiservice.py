from flask import Flask
from flask import request
import emoji
import random


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='color:blue'>Hello from Emoji Service!</h1>"

@app.route("/greetings")
def greetings():
    return "Hello World!"

@app.route('/emoji_paste', methods=['POST'])
def emoji_service():
    if request.method == 'POST':
        content = request.get_json(force=True)
        return emoji_provider(content)

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
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

# if __name__ == "__main__":
#     app.run(host='0.0.0.0')

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()