from kafka import KafkaConsumer, OffsetAndMetadata, TopicPartition
import json, sys, os
sys.path.append(f'{os.path.split(os.environ["VIRTUAL_ENV"])[0]}/zookeeper')
from zookeeper import get_kafka_broker


consumer = KafkaConsumer('topico_lero_ok',
                         group_id='grupo-1-lero-lero',
                         bootstrap_servers=get_kafka_broker(),
                         auto_offset_reset='earliest', enable_auto_commit=False)


print('#################################')
print('#################################')

for item in consumer:
    print('-----------------')
    try:
        item.value.decode().index('comentar_anteriores')
        print(item.value.decode())
        consumer.commit({TopicPartition("topico_lero_ok", item.partition): OffsetAndMetadata(item.offset+1, '')})
    except Exception as erro:
        print(item.value.decode())

print('#################################')
print('#################################')
    