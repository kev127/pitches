from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import UpdateProfile,PitchForm,CommentForm
from ..models import User,Pitch,Comment
from flask_login import login_required,current_user


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Pitches'

    # Getting by category
    interview_pitches = ('interview')
    product_pitches = ('product')
    promotion_pitches = ('promotion')



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
def new_Pitch():
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


@main.route('/category/interview', methods=['POST','GET'])
def interview_pitches():
    pitches = ('interview')
    return render_template('category/interview_pitches.html',pitches = pitches)

@main.route('/category/products', methods=['POST','GET'])
def products_pitches():
    pitches = ('products')
    return render_template('category/products_pitches.html',pitches = pitches)

@main.route('/category/promotion', methods=['POST','GET'])
def promotion_pitches():
    pitches = ('promotion')
    return render_template('category/promotion_pitches.html',pitches = pitches)

@main.route('/pitch/<int:id>', methods = ['GET','POST'])
def pitch(id):
    pitch = Pitch.get_pitch(id)
    posted_date = pitch.posted.strftime('%b %d, %Y')

    if request.args.get("like"):
        pitch.likes = pitch.likes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    elif request.args.get("dislike"):
        pitch.dislikes = pitch.dislikes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comment(comment = comment,user = current_user,pitch_id = pitch)

        new_comment.save_comment()


    comments = Comment.get_comments(pitch)

    return render_template("pitch.html", pitch = pitch, comment_form = comment_form, comments = comments, date = posted_date)

@main.route('/user/<uname>/pitches')
def user_pitches(uname):
    user = User.query.filter_by(username=uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id).all()
    pitches_count = Pitch.count_pitches(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    return render_template("profile/pitches.html", user=user,pitches=pitches,pitches_count=pitches_count,date = user_joined)