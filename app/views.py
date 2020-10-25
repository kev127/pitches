from flask import render_template
from app import app
from .request import get_pitches

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Pitches'

    # Getting by category
    interview_pitches = get_pitches('interview')
    product_pitches = get_pitches('product')
    promotion_pitches = get_pitches('promotion')


    return render_template('index.html',title = title, interview = interview_pitches, product = product_pitches, promotion = promotion_pitches)