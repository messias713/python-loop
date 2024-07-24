import random
import time

def criar_poemas_espirituais():
    poemas = [
        "No silêncio da alma, encontro a paz que me nutre",
        "A luz divina brilha em cada ser, conectando-nos ao universo",
        "Com gratidão no coração, agradeço por mais um dia de aprendizado",
        "A cada respiração, sinto a presença do divino em mim",
        "Na simplicidade do momento presente, encontro a plenitude da vida",
        "O amor é a chave que abre as portas do coração e da alma",
        "Em cada desafio, encontro uma oportunidade de crescimento espiritual",
        "A beleza da natureza reflete a grandiosidade do criador",
        "A compaixão é o caminho para a cura e para a união",
        "O amor incondicional é a essência que nos conecta a todos os seres"
    ]

    while True:
        indice = random.randint(0, 9)
        print(poemas[indice])
        time.sleep(1)  # Adiciona um intervalo de 1 segundo entre cada poema

criar_poemas_espirituais()
