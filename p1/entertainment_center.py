# -*- coding: utf-8 -*-
"""
Gera uma relação de filmes e algumas informações gerais.
"""

import fresh_tomatoes
import media


def filmes():
    """
    Lista de filmes e seus atributos.
    """
    espera_de_um_milagre = media.Movie(u"À Espera de um Milagre",
                                       u"A história de um preso no corredor da"
                                       " morte com um dom especial de cura",
                                       "https://upload.wikimedia.org/wikipedia"
                                       "/pt/8/8f/%C3%80_Espera_de_um_Milagre.j"
                                       "pg",
                                       "https://www.youtube.com/watch?v=EIc_wJ"
                                       "tm6AU")
    intocaveis = media.Movie(u"Intocáveis",
                             u"Um rico tetraplégico contrata um assistente sem"
                             " experiência em cuidar de pessoas e juntos vivem"
                             " muitas aventuras",
                             "https://upload.wikimedia.org/wikipedia/pt/d/d6/I"
                             "ntouchables_cartaz.jpg",
                             "https://www.youtube.com/watch?v=-Fb8h4gChlU")
    django_livre = media.Movie(u"Django Livre",
                               u"Django é um escravo que é libertado por um ca"
                               "çador de recompensas e com sede de vingança de"
                               "cide ajudar o seu libertador na caçada de reco"
                               "mpensas",
                               "https://upload.wikimedia.org/wikipedia/pt/8/8b"
                               "/Django_Unchained_Poster.jpg",
                               "https://www.youtube.com/watch?v=tivv135aGbc")
    matrix = media.Movie(u"Matrix",
                         u"Matrix é um sistema inteligente e artificial que es"
                         "craviza a humanidade manipulando suas mentes",
                         "https://upload.wikimedia.org/wikipedia/pt/c/c1/The_M"
                         "atrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")
    auto_da_compadecida = media.Movie(u"O Auto da Compadecida",
                                      u"Dois sertanejos pobres, um é mentiroso"
                                      " e o outro é covarde, vivem as maiores "
                                      "aventuras para conquistar o pão de cada"
                                      " dia",
                                      "https://upload.wikimedia.org/wikipedia/"
                                      "pt/b/bf/O_auto_da_compadecida.jpg",
                                      "https://www.youtube.com/watch?v=XPuMu_E"
                                      "Nzlg")
    movies = [
        espera_de_um_milagre,
        intocaveis,
        django_livre,
        matrix,
        auto_da_compadecida
        ]
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    filmes()
