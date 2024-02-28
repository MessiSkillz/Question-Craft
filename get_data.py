import requests
import time
topic = input("Enter the topic: ")
question = input("Enter the question: ")
options = []
for i in range(4):
    options.append(input("Enter option #"+str(i+1)+": "))
answer = input("Enter the answer: ")
send_data = str({
    "topic": topic,
    "question": question,
    "options": options,
    "answer": answer
})
ngrok_link = "https://617f-34-134-248-15.ngrok-free.app/"
url = ngrok_link+'run?msg='+send_data
start = time.time()
try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['output']
    else:
        print("Error:", response.status_code)
except requests.RequestException as e:
    print("Request error:", e)
print("Time taken:", time.time()-start)
print("Here's your generated question:")
import json
data = json.loads(data.replace("'", "\""))
question = data['question']
options = data['options']
answer = data['answer']
print("Question:", question)
ans = "ABCD"
for i in range(4):
    print(ans[i]+".", options[i])
print("Answer:", answer)