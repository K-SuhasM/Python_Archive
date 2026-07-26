import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
name=[]
while True:
    names=input("Enter names to congratulate, input 'done' when finished: ")
    if names.lower()=="done":
        break
    name.append(names)
print(name)
for i in name:
    speaker.Speak(f"Congratulations {i}")