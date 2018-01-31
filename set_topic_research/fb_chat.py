import fbchat

client = fbchat.Client("+67076025211", "pw0520")

friends = client.getUsers("Ony De Jesus")  # return a list of names
friend = friends[0]
sent = client.send(friend.uid, "FB chat with python")
if sent:
    print("Message sent successfully!")
# IMAGES
client.sendLocalImage(friend.uid,message='This is an Image', image='/home/ony/Devel/notas/notas/set_topic_research/my_topic_research/image/win.jpg') # send local image


last_messages = client.getThreadInfo(friend.uid, last_n=20)
last_messages.reverse()  # messages come in reversed order

for message in last_messages:
    print(message.body)
