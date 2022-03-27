## Criar Ambiente Python
- python3 -m venv .venv
- source .venv/bin/activate
- pip install --upgrade pip
- pip install -r requirements.txt


## Alterar IP para poder conectar de forma externa
- KAFKA_ADVERTISED_LISTENERS: "INTERNAL://kafka-server1:9090,A://10.1.1.11:9092"
- KAFKA_ADVERTISED_LISTENERS: "INTERNAL://kafka-server2:9090,B://10.1.1.11:9093"
- KAFKA_ADVERTISED_LISTENERS: "INTERNAL://kafka-server3:9090,C://10.1.1.11:9094"


## Alterar IP Zookeeper
zk = KazooClient(hosts='host-ip:2181')


## Executar docker Kafka, Zookeeper e Kafdrop
- docker-compose up -d


## Host Kafdrop
localhost:9010


## Rodar Consumer
python3 consumer/consumer_lero_lero.py


## Rodar Producer
python3 producer/producer_lero_lero.py


Obs: Mac m1 não funciona esse docker-compose. -> https://github.com/confluentinc/common-docker/issues/117