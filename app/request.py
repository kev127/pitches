from app import app
from models import pitch

def get_pitches(category):
    '''
    Function that gets json response to our url request
    '''
    
def process_results(pitches_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        pitches_list: A list of dictionaries that contain pitches details

    Returns :
        pitches_results: A list of pitches objects
    '''
    pitches_results = []
    for pitches_item in pitches_list:
        id = movie_item.get('id')
        title = movie_item.get('title')
        content = movie_item.get('content')
        category = movie_item.get('category')
        likes = movie_item.get('likes')
        dislikes = movie_item.get('dislikes')

        
        pitches_object = pitch(id,title,content,category,likes,dislikes)
        pitches_results.append(pitches_object)

    return pitches_results   
