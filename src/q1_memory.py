from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter,defaultdict

def leer_tweets(file_path):
    """Generador que lee y devuelve un tweet a la vez."""
    with open(file_path, 'r') as file:
        for line in file:
            yield json.loads(line)

@profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    tweets_por_fecha = Counter()
    usuarios_por_fecha = defaultdict(lambda: Counter())

    for tweet in leer_tweets(file_path):
        fecha = tweet['date'][:10]
        usuario = tweet['user']['username']
        tweets_por_fecha[fecha] += 1
        usuarios_por_fecha[fecha][usuario] += 1

    top_10_fechas = tweets_por_fecha.most_common(10)
    top_usuario_por_fecha = {
        fecha: usuarios.most_common(1)[0][0] for fecha, _ in top_10_fechas
        for fecha, usuarios in usuarios_por_fecha.items() if fecha in dict(top_10_fechas).keys()
    }
    resultado = []
    for fecha, _ in top_10_fechas:
        resultado.append((datetime.strptime(fecha, '%Y-%m-%d').date(),top_usuario_por_fecha[fecha]))
    return resultado
