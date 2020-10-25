from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Pitches'

    # Getting reviews by category
    interview_pitches = get_pitches('interview')
    product_pitches = get_pitches('product')
    promotion_pitches = get_pitches('promotion')


    return render_template('index.html',title = title, interview = interview_piches, product = product_piches, promotion = promotion_pitches)