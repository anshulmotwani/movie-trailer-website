# imports webbrowser used for opening web browser using code
import webbrowser

# class named Movie which holds instance variables and instance functions
# this class is used to make instance of each movie


class Movie():
    
    # this is a constructor which is called to make space in memory
    # for a particular instance of clss
    # it takes in attributes which are then
    # allocated to instance variables
    #   self is used to point to current instance being allocated
    
    def __init__(self, title, storyline, poster_url, trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_trailer_url
    # this is a function used to open youtube video in web browser    
    
    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)
        
