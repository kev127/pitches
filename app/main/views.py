
from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_pitches
from .forms import PitchForm
from ..models import User
from flask_login import login_required


# Views
@main.route('/')
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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)    

@main.route('/pitch/new', methods = ['GET','POST'])
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

@main.route('/pitch/newPitch', methods=['POST','GET'])
@login_required
def newPitch():
    pitch = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.text.data
        category = pitch_form.category.data

        # Updated pitch instance
        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,user=current_user,likes=0,dislikes=0)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New pitch'
    return render_template('new_pitch.html',title = title,pitch_form=pitch_form )

@main.route('/category/interview', methods=['POST','GET'])
def interview_pitches():
    pitches = get_pitches('interview')
    return render_template('category/interview_pitches.html',pitches = pitches)

@main.route('/category/products', methods=['POST','GET'])
def products_pitches():
    pitches = get_pitches('products')
    return render_template('category/products_pitches.html',pitches = pitches)

@main.route('/category/promotion', methods=['POST','GET'])
def promotion_pitches():
    pitches = get_pitches('promotion')
    return render_template('category/promotion_pitches.html',pitches = pitches)

