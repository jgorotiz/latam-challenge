from typing import List, Tuple
import json
from collections import Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    contador_menciones = Counter()
    
    with open(file_path, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            tweet = json.loads(linea)
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
