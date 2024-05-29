```
pip3 install nats-py clickhouse-driver
helm install my-release oci://registry-1.docker.io/bitnamicharts/clickhouse
kubectl get secret my-release-clickhouse -oyaml  #get secret of default user
docker run -d --name nats-server -p 4222:4222 nats 

```

```
kubectl port-forward svc/my-release-clickhouse 8123 --address=0.0.0.0
open http://localhost:8123/
> Run this schema on default database

CREATE TABLE mydatabase.mytable (
    id UInt64,
    message String,
    timestamp DateTime
) ENGINE = MergeTree()
ORDER BY id;
```


```
python3 listen.py
python3 push.py

```