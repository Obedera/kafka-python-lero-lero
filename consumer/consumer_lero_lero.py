from kafka import KafkaConsumer, OffsetAndMetadata, TopicPartition
import json


consumer = KafkaConsumer('topico_lero_ok',
                         group_id='grupo-1-lero-lero',
                         bootstrap_servers=['192.168.0.17:9091', '192.168.0.17:9092', '192.168.0.17:9093'],
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
    