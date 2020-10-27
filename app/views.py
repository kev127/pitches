from flask import render_template
from app import app
from .request import get_pitches
from .forms import PitchForm


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

@app.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('movie',id = movie.id ))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)