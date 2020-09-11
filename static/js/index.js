// Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
  client = new Paho.MQTT.Client("maqiatto.com", 8883, "web_" + parseInt(Math.random() * 100, 10));
  var variables;
  // set callback handlers
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;
  var options = {
   useSSL: false,
    userName: "jomsk@hotmail.com",
    password: "Jomsk4all1996",
    onSuccess:onConnect,
    onFailure:doFail
  }

  // connect the client
  client.connect(options);
   
  // called when the client connects
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("Conectado...");
	
    client.subscribe("jomsk@hotmail.com.com/IoT");
    message = new Paho.MQTT.Message("hola desde la web");
    message.destinationName = "jomsk@hotmail.com.com/IoT1";
    client.send(message);
	
  }

  function doFail(e){
    console.log(e);
	
  }

  // called when the client loses its connection
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+responseObject.errorMessage);
    }
  }

  // called when a message arrives
  function onMessageArrived(message) {
    var led1=document.getElementById("Sensor").innerHTML
    var led2=document.getElementById("Sensor1").innerHTML
    console.log("onMessageArrived:"+message.payloadString);
    variables=(message.payloadString).split(("/"))
    led1=variables[0];
    led2=variables[1];
  }

  function mostrard(){
    var dat=document.getElementById("info").innerHTML;
    dat=variables[2];
  }
  
