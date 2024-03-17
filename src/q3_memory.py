from typing import List, Tuple
import json
from collections import Counter

def leer_tweets(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield json.loads(line)

@profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    contador_menciones = Counter()
    
    for tweet in  leer_tweets(file_path):
        if 'mentionedUsers' in tweet:
            menciones = tweet['mentionedUsers']
            if menciones:
                for usuario in menciones:
                    if usuario and 'username' in usuario:
                        contador_menciones[usuario['username']] += 1
    resultado = []
    for usuario, conteo in contador_menciones.most_common(10):
        resultado.append((usuario, conteo))
    return resultado

