from kafka import KafkaProducer
import json, sys, os
from util_lero_lero import gerar_lero_lero

sys.path.append(f'{os.path.split(os.environ["VIRTUAL_ENV"])[0]}/zookeeper')

from zookeeper import get_kafka_broker


producer = KafkaProducer(bootstrap_servers=get_kafka_broker())

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