from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter,defaultdict

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    tweets = []
    file = open(file_path , "r")
    for line in file:
        tweet = json.loads(line)
        tweets.append(tweet)
    file.close()
    tweets_por_dia = Counter()
    tweets_por_usuario_por_dia = defaultdict(lambda: defaultdict(int))

    for tweet in tweets:
        fecha = tweet['date'][:10]
        username = tweet['user']['username']
        tweets_por_dia[fecha] += 1
        tweets_por_usuario_por_dia[fecha][username] += 1
    top_fechas = tweets_por_dia.most_common(10)
    usuarios_top_por_fecha = {}
    for fecha, _ in top_fechas:
        usuarios_top_por_fecha[fecha] = max(tweets_por_usuario_por_dia[fecha].items(), key=lambda x: x[1])
    resultado = []
    for fecha, (usuario,conteo) in usuarios_top_por_fecha.items():
        resultado.append((datetime.strptime(fecha, '%Y-%m-%d').date(), usuario))
    return resultado

