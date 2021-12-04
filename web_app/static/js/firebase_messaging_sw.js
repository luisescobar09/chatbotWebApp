/*if( 'undefined' === typeof window){
   importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");
   importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js");
} 
 
var config = {        
	apiKey: "AIzaSyAV5GQLmw2S_yA_2hTYvd2-0v25pO-aQwM",
	authDomain: "chatbot-af6db.firebaseapp.com",
	databaseURL: "https://chatbot-af6db-default-rtdb.firebaseio.com",
	projectId: "chatbot-af6db",
	storageBucket: "chatbot-af6db.appspot.com",
	messagingSenderId: "1004740433902",
	appId: "1:1004740433902:web:bc5fd1ad4635e79bd6e0ff",
	measurementId: "G-PGZK7XB2K0" };
	firebase.initializeApp(config);
	const messaging=firebase.messaging();
	messaging.setBackgroundMessageHandler(function (payload) {    
		console.log(payload);    
		const notification=JSON.parse(payload);    
		const notificationOption={        
			body:notification.body,        
			icon:notification.icon    
		};    
		return self.registration.showNotification(payload.notification.title,notificationOption);});*/

var firebaseConfig = {
	apiKey: "AIzaSyAV5GQLmw2S_yA_2hTYvd2-0v25pO-aQwM",
	authDomain: "chatbot-af6db.firebaseapp.com",
	databaseURL: "https://chatbot-af6db-default-rtdb.firebaseio.com",
	projectId: "chatbot-af6db",
	storageBucket: "chatbot-af6db.appspot.com",
	messagingSenderId: "1004740433902",
	appId: "1:1004740433902:web:bc5fd1ad4635e79bd6e0ff",
	measurementId: "G-PGZK7XB2K0"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
	firebase.analytics();
	
	var messaging = firebase.messaging();
	console.log(messaging.getToken());
	messaging.getToken({ vapidKey: 'BN8V2b0UnSd1EPYYSKVdU4wEyYLDdrzYh3mEpiC_sbI1ZqBbBsQsc5o4VaI6kHt3bhIGMQNeP_FFwCbl0ckVEcY' }).then((currentToken) => {
	if (currentToken) {
		// Send the token to your server and update the UI if necessary
		// ...
		// SI CREA UN TOKEN VALIDO LO ENVÍA PARA INSERTARLO EN LA BD
		let xhr = new XMLHttpRequest();
		xhr.open('get', 'https://chatbotwebapp.josluisluis13.repl.co/device_token/'+currentToken);
		xhr.send();
		xhr.onload = function() {
			console.log(xhr.response);
		};
	} else {
		// Show permission request UI
		console.log('No registration token available. Request permission to generate one.');
		// ...
	}
	}).catch((err) => {
	console.log('An error occurred while retrieving token. ', err);
	// ...
	});
	
	
	messaging
		.requestPermission()
		.then(function () {
		console.log("Notification permission granted.");
		return messaging.getToken()
		})
		.catch(function (err) {
		console.log("Unable to get permission to notify.", err);
	});
	
	
	messaging.onMessage((payload) => {
	console.log('Message received. ', payload);
	
	});


if ('serviceWorker' in navigator) {
navigator.serviceWorker.register('firebase-messaging-sw.js')
  .then(function(registration) {
    console.log('Registration successful, scope is:', registration.scope);
  }).catch(function(err) {
    console.log('Service worker registration failed, error:', err);
  });
}