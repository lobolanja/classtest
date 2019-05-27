import paho.mqtt.subscribe as subscribe

def print_msg(client, userdata, message):
    print("%s : %s" % (message.topic, message.payload))

subscribe.callback(print_msg, "#", hostname="192.168.43.160")