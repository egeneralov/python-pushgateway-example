# PushGateway python example

## How does it work?

### General Prometheus architecture overview

![](https://camo.githubusercontent.com/78b3b29d22cea8eee673e34fd204818ea532c171/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f70726f6d6574686575732f70726f6d65746865757340633334323537643036396336333036383564613335626365663038343633326666643564363230392f646f63756d656e746174696f6e2f696d616765732f6172636869746563747572652e737667)

### Single Node Prometheus + Pushgateway

Single node is pretty straightforward. 

1. Use `PushGatewayClient` to create a metric. Metric is stored in `Redis`.
2. Use `PushGatewayClient` can be pushed manually or with a command. After push metrics stored in Redis are transported to the actual `PushGateway` service.
3. `Prometheus` periodically pulls in new metrics from `PushGateway`.

![](./images/basic_prometheus_cluster_setup.png)

![](./images/advanced_prometheus_cluster_setup.png)
