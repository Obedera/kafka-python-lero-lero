def get_kafka_broker():
    from kazoo.client import KazooClient
    import ast

    zk = KazooClient(hosts='192.168.15.24:2181')
    zk.start()
    lista_ips = []
    for indice in range(0, zk.get('/brokers/ids')[1].numChildren):
        valor = zk.get(f'/brokers/ids/{indice+1}')
        obj_zookeeper = ast.literal_eval(valor[0].decode())
        lista_ips.append(obj_zookeeper.get('endpoints')[1].split('://')[1])
    
    return lista_ips