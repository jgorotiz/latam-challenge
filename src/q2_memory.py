from typing import List, Tuple
import emoji
import json
from collections import Counter

def leer_tweets(file_path):
    # lee y devuelve un tweet a la vez
    with open(file_path, 'r') as file:
        for line in file:
            yield json.loads(line)

def extraer_emojis(texto):
    todos_emojis = [car for car in texto if car in emoji.EMOJI_DATA]
    return todos_emojis

@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    contador_emojis = Counter()

    for tweet in  leer_tweets(file_path):
        # Extraer el texto del tweet
        texto_tweet = tweet['content']
        # Encontrar y contar todos los emojis en el texto
        emojis_encontrados = extraer_emojis(texto_tweet)
        contador_emojis.update(emojis_encontrados)

    # Imprimir los top 10 emojis más usados con su respectivo conteo
    resultado = []
    for emoji, conteo in contador_emojis.most_common(10):
        resultado.append((emoji,conteo))
    return resultado

