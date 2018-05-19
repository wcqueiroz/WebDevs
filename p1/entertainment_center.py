import fresh_tomatoes
import media


espera_de_um_milagre = media.Movie(u"À Espera de um Milagre",
                    u"A história de um preso no corredor da morte com um dom especial de cura",
                    "https://upload.wikimedia.org/wikipedia/pt/8/8f/%C3%80_Espera_de_um_Milagre.jpg",
                    "https://www.youtube.com/watch?v=EIc_wJtm6AU")

intocaveis = media.Movie(u"Intocáveis",
                    u"Um rico tetraplégico contrata um assistente sem experiência em cuidar de pessoas e juntos vivem muitas aventuras",
                    "https://upload.wikimedia.org/wikipedia/pt/d/d6/Intouchables_cartaz.jpg",
                    "https://www.youtube.com/watch?v=-Fb8h4gChlU")

django_livre = media.Movie(u"Django Livre",
                    u"Django é um escravo que é libertado por um caçador de recompensas e com sede de vingança decide ajudar o seu libertador na caça das recompensas",
                    "https://upload.wikimedia.org/wikipedia/pt/8/8b/Django_Unchained_Poster.jpg",
                    "https://www.youtube.com/watch?v=tivv135aGbc")

avatar = media.Movie(u"Avatar",
                    u"A marine on an alien planet",
                    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                    "http://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie(u"School of Rock",
                    u"Using rock music to learn",
                    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                    "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie(u"Ratatouille",
                    u"A rat is a chef in Paris",
                    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie(u"Hunger Games",
                    u"A really real reality show",
                    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                    "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [espera_de_um_milagre, intocaveis, django_livre, avatar, school_of_rock, ratatouille, hunger_games]
fresh_tomatoes.open_movies_page(movies)
