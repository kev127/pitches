import unittest
from models import pitch
Pitch = pitch.Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(id=1,pitch_title='Pitch',pitch_content='pitches',category="Product",likes=0,dislikes=0)

     def test_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_title,'Pitch')
        self.assertEquals(self.new_pitch.pitch_content,'Pitches')
        self.assertEquals(self.new_pitch.category,"Product")


if __name__ == '__main__':
    unittest.main()