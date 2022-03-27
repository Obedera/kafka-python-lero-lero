from kafka import KafkaConsumer, OffsetAndMetadata, TopicPartition
import sys, os
sys.path.append(f'{os.path.split(os.environ["VIRTUAL_ENV"])[0]}/zookeeper')
from zookeeper import get_kafka_broker


consumer = KafkaConsumer('topico_lero_ok',
                         group_id='grupo-1-lero-lero',
                         bootstrap_servers=get_kafka_broker(),
                         auto_offset_reset='earliest', enable_auto_commit=False)


statusComitarMsg = input('Deseja ler as mensagens e comitar? (s/n): ')


print('#################################')
print('#################################')

for item in consumer:
    print('')
    try:
        if(statusComitarMsg.upper() == 'S'):
            consumer.commit({TopicPartition("topico_lero_ok", item.partition): OffsetAndMetadata(item.offset+1, '')})
        print(f'offset -> {item.offset}')
        print(f'valor -> {item.value.decode()}')
    except Exception as erro:
        print(f'{erro}')
    print('')

print('#################################')
print('#################################')
    