from typing import List, Tuple
import emoji
import json
from collections import Counter


def extraer_emojis(texto):
    todos_emojis = [car for car in texto if car in emoji.EMOJI_DATA]
    return todos_emojis


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    contador_emojis = Counter()
    with open(file_path, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            tweet = json.loads(linea)
            # Extraer el texto del tweet
            texto_tweet = tweet['content']
            # Encontrar y contar todos los emojis en el texto
            emojis_encontrados = extraer_emojis(texto_tweet)
            contador_emojis.update(emojis_encontrados)

    resultado = []
    for emoji, conteo in contador_emojis.most_common(10):
        resultado.append((emoji,conteo))
    return resultado

