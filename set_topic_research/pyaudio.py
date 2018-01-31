choice=='Shutdown'
msgbox("You chose to Shutdown")
msg = "Do you want to schedule your Shutdown"
title = "Confirmation"
choices=
choice=buttonbox(msg,title,choices)
if choice=='Yes':
t=integerbox('Enter the time in minutes :')
tim=t*60
time.sleep(tim)
#os.system('sudo shutdown -h now')
commands.getoutput('sudo shutdown -r now')
else:
os.system('sudo shutdown -h now')