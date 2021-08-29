from vidstream import AudioSender
from vidstream import AudioReceiver

import threading


receiver = AudioReceiver('192.168.1.204',9999)
recice_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender('192.168.1.205',8080)
sender_thread = threading.Thread(target=sender.start_stream)
print("starting threading")
recice_thread.start()
sender_thread.start()