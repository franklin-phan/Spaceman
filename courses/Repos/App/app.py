from flask import Flask,request,choice,render_template,sample


app = Flask(__name__)

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return render_template('index.html')

compliments = ['coolio', 'smashing', 'neato', 'fantabulous']

@app.route('/compliment')
def get_compliment():
    """Give the user a compliment"""
    name = request.args.get('name')
    show_compliments = request.args.get('show_compliments')
    compliments_to_show = sample(compliments, 3)

    return render_template(
        'compliments.html', 
        name=name, 
        show_compliments=show_compliments, 
        compliment=compliment)

horoscopes = ['eat spaghetti','eat lasagna','get destroyed by Gordon Ramsey','get framed for murder']
def get_horoscope():
    horoscope = choice(horoscopes)
    return f'Today, you will {horoscope} and {horoscope}!'

print(get_horoscope())

if __name__ == "__main__":
   app.run(debug=True)