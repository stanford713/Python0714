#送上雲端
from firebase import firebase
firebase = firebase.FirebaseApplication('https://stanford713-9f724.firebaseio.com/', None)
result = firebase.patch('/user', {3:'anita'})
print(result)