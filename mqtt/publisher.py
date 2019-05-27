import paho.mqtt.publish as publish

publish.single("paho/test/single", "boo", hostname="192.168.43.160")