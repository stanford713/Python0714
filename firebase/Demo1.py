from firebase import firebase
firebase = firebase.FirebaseApplication('https://stanford713-9f724.firebaseio.com/', None)
result = firebase.get('/user', 1)
print(result)