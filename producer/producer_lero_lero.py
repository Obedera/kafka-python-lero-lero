from kafka import KafkaProducer
import json
from util_lero_lero import gerar_lero_lero

producer = KafkaProducer(bootstrap_servers=['192.168.0.17:9091', '192.168.0.17:9092', '192.168.0.17:9093'])

i = 0
while i<10:
    msg = f'{gerar_lero_lero()}'

    # Mensagens com o indice par deve ser comitadas e todas as anteriores
    if i % 2 == 0:
        msg = f'{gerar_lero_lero()} - comentar_anteriores'


    future = producer.send('topico_lero_ok', key=b'msg-lero', value=msg.encode())
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        log.exception()
        pass
    i += 1