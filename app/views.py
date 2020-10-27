from flask import render_template
from app import app
from .request import get_pitches
from .forms import PitchForm
from models import pitch


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

@app.route('/pitch/new', methods = ['GET','POST'])
def newPitch():
    pitch = PitchForm()
    if pitch.validate_on_submit():
        pitch_title = pitch.pitch_title.data
        category_name = pitch.category_name.data
        text= pitch.text.data

        #update pitch instance
        newPitch = Pitch(title = pitch_title,category_name =category_name,content =text,user= current_user )

        #save pitch
        newPitch.save_pitch()
        return redirect(url_for('.index'))
    title = 'NEW PITCH'
    return render_template('new_pitch.html',title = title, new_pitch = pitch)

@app.route('/category/interview', methods=['POST','GET'])
def interview_pitches():
    pitches = get_pitches('interview')
    return render_template('category/interview_pitches.html',pitches = pitches)

@app.route('/category/products', methods=['POST','GET'])
def products_pitches():
    pitches = get_pitches('products')
    return render_template('category/products_pitches.html',pitches = pitches)

@app.route('/category/promotion', methods=['POST','GET'])
def promotion_pitches():
    pitches = get_pitches('promotion')
    return render_template('category/promotion_pitches.html',pitches = pitches)

