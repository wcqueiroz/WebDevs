# -*- coding: utf-8 -*-
"""
Define as informações sobre os filmes.
"""

import webbrowser


class Movie():
    """
    Define a estrutura de dados sobre um filme

    Atributos:
        movie_title (str): Título do filme
        movie_storyline (str): Resumo do filme
        poster_image (str): link para o poster do filme
        trailer_youtube (str): link para o trailer do filme

    Variável:
        VALID_RATINGS: Informa as faixas etárias indicadas para os filmes

    Métodos:
        __init__: Método construtor da classe Movie
        show_trailer: Abre e executa o trailer do filme a partir do link
            informado
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        Método construtor da classe Movie
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Abre e executa o trailer do filme a partir do link informado
        """
        webbrowser.open(self.trailer_youtube_url)
