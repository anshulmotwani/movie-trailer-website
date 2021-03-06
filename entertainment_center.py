# fresh_tomatoes.py is imported. It converts the movie list into a
# trailer website
import fresh_tomatoes
# imports media.py which holds the class definition
import media

# each instance of class movie is made and details are sent as attributes
the_dark_knight = media.Movie("The Dark Knight",
                              "When the menace known as the Joker wreaks \
                               havoc and chaos on the people of Gotham, the\
                               caped crusader must come to terms with one \
                               of the greatest psychological tests of his \
                               ability to fight injustice.",
                              "http://goo.gl/NbxnNw",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

the_avengers = media.Movie("The Avengers",
                           "Earth's mightiest heroes must come together \
                            and learn to fight as a team if they are to \
                            stop the mischievous Loki and his alien army\
                            from enslaving humanity.",
                           "http://goo.gl/Owi6CQ",
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8")

captain_america = media.Movie("Captain America:The Winter Soldier",
                              "As Steve Rogers struggles to embrace his role \
                               in the modern world, he teams up with another \
                               super soldier, the black widow, to battle a \
                               new threat from old history: an assassin \
                               known as the Winter Soldier.",
                              "http://goo.gl/HQE04Y",
                              "https://www.youtube.com/watch?v=7SlILk2WMTI")

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in \
                            space in an attempt to ensure humanity's \
                            survival.",
                           "http://goo.gl/DovXiY",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

guardians_of_the_galaxy = media.Movie("Guardians Of The Galaxy",
                                      "A group of intergalactic criminals are \
                                       forced to work together to stop a \
                                       fanatical warrior from taking control \
                                       of the universe.",
                                      "http://goo.gl/c5FOtN",
                                      "https://goo.gl/JYTHpf")

hobbit = media.Movie("The Hobbit: The Battle of the Five Armies ",
                     "Bilbo and Company are forced to engage in a war against \
                      an array of combatants and keep the Lonely Mountain \
                      from falling into the hands of a rising darkness.",
                     "http://goo.gl/8Le9Ur",
                     "https://www.youtube.com/watch?v=iVAgTiBrrDA")
# we form an array to pass all instances as a list 
movies = [the_dark_knight, the_avengers, captain_america, 
          interstellar, guardians_of_the_galaxy, hobbit]

# this passes the movie list and displays the movie trailor website
fresh_tomatoes.open_movies_page(movies)
