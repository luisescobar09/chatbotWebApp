from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import requests, json
from django.http import HttpResponse
# Create your views here.

def get_device_token(request, device_token):
	response = requests.get('https://chatbot-af6db-default-rtdb.firebaseio.com/devices_allowed.json')
	items = response.json()
	encoded = json.dumps(items)
	decoded = json.loads(encoded)
	result = {}
	if str(decoded).count(device_token) == 0:
		data = {
			'device_token' : device_token
		}
		post_device = requests.post('https://chatbot-af6db-default-rtdb.firebaseio.com/devices_allowed.json', data = json.dumps(data))
		if post_device.status_code == 200:
			result['status'] : 200
		else:
			result['status'] : 404
	return HttpResponse(json.dumps(result), content_type="application/json") 


def home(request):
	if not request.user.is_authenticated:
		return redirect('/login')
	result = requests.get('https://chatbot-af6db-default-rtdb.firebaseio.com/no_leidos.json')
	items = result.json()
	encoded = json.dumps(items)
	decoded = json.loads(encoded)
	diccionario = {'no_leidos': decoded}
	return render(request, 'index.html', diccionario)

def read_messages(request):
	if not request.user.is_authenticated:
		return redirect('/login')
	result = requests.get('https://chatbot-af6db-default-rtdb.firebaseio.com/leidos.json')
	items = result.json()
	encoded = json.dumps(items)
	decoded = json.loads(encoded)
	return render(request, 'read.html', {'leidos': decoded})


def delete_request(request, id_request, fecha):
	if not request.user.is_authenticated:
		return redirect('/login')
	response = requests.post('https://get-data-chatbot.josluisluis13.repl.co/delete', data= {'id': id_request, 'fecha': fecha })
	if response.status_code == 200:
		return redirect('/read', {'success': 'todo correcto'})

def delete_unread(request, id_request):
	if not request.user.is_authenticated:
		return redirect('/login')
	result = requests.get('https://chatbot-af6db-default-rtdb.firebaseio.com/no_leidos/'+id_request+'.json')
	items = result.json()
	encoded = json.dumps(items)
	decoded = json.loads(encoded)
	if decoded is not None:
		datos = {
			'nombre' : decoded['nombre'],
			'telefono' : decoded['telefono'],
			'fecha' : decoded['fecha'],
			'conversacion' : decoded['conversacion'],
		}
		response = requests.post('https://chatbot-af6db-default-rtdb.firebaseio.com/leidos.json', data = json.dumps(datos))
		if response.status_code == 200:
			result = requests.delete('https://chatbot-af6db-default-rtdb.firebaseio.com/no_leidos/'+id_request+'.json')
			return redirect('/home', {'success': 'correcto todo'})


def login_view(request):
	if request.user.is_authenticated:
		return redirect('/home')
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is None:
			context = {
				'error' : 'Datos invalidos, verifique e intente de nuevo.'
			}
			return render(request, 'accounts/login.html', context)
		else:
			login(request, user)
			return redirect('/home')
	else:
		return render(request, 'accounts/login.html', {})

def logout_view(request):
	if not request.user.is_authenticated:
		return redirect('/login')
	if request.method=='GET':
		logout(request)
		return redirect('/login')

def showFirebaseJS(request):
	if request.user.is_authenticated:
		data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
			'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
			'var firebaseConfig = {' \
			'        apiKey: "AIzaSyAV5GQLmw2S_yA_2hTYvd2-0v25pO-aQwM",' \
			'        authDomain: "chatbot-af6db.firebaseapp.com",' \
			'        databaseURL: "https://chatbot-af6db-default-rtdb.firebaseio.comhttps://chatbot-af6db-default-rtdb.firebaseio.com",' \
			'        projectId: "chatbot-af6db",' \
			'        storageBucket: "chatbot-af6db.appspot.com",' \
			'        messagingSenderId: "1004740433902",' \
			'        appId: "1:1004740433902:web:bc5fd1ad4635e79bd6e0ff",' \
			'        measurementId: "G-PGZK7XB2K0"' \
			' };' \
			'firebase.initializeApp(firebaseConfig);' \
			'const messaging=firebase.messaging();' \
			'messaging.setBackgroundMessageHandler(function (payload) {' \
			'    console.log(payload);' \
			'    const notification=JSON.parse(payload);' \
			'    const notificationOption={' \
			'        body:notification.body,' \
			'        icon:notification.icon' \
			'    };' \
			'    return self.registration.showNotification(payload.notification.title,notificationOption);' \
			'});'

		return HttpResponse(data,content_type="text/javascript")

def handler404(request, exception):
    return render(request, '404.html', status=404)