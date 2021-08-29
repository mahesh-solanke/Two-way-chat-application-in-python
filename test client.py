from vidstream import AudioSender
from vidstream import AudioReceiver

import threading


receiver = AudioReceiver('192.168.1.205',8080)
recice_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender('192.168.1.204',9999)
sender_thread = threading.Thread(target=sender.start_stream)
print("starting thread")
sender_thread.start()
recice_thread.start()