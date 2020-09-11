// Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
  client = new Paho.MQTT.Client("maqiatto.com", 8883, "web_" + parseInt(Math.random() * 100, 10));
  var variables;
  // set callback handlers
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;
  var options = {
    useSSL: false,
    userName: "licha_05reyes@outlook.com",
    password: "Galapagos1001",
    onSuccess:onConnect,
    onFailure:doFail
  }
  
  // connect the client
  client.connect(options);
    
  // called when the client connects
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("Conectado...");
  
    client.subscribe("licha_05reyes@outlook.com/IoT");
  
  
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
    var le=document.getElementById("Sensor");
    var l=document.getElementById("Sensor1");
    console.log("onMessageArrived:"+message.payloadString);
    variables=(message.payloadString).split(("/"));
    if(variables[0]=="on"){
      le.innerHTML="on";
    }else{
      le.innerHTML="off";
    }
    if(variables[1]=="on"){
      l.innerHTML="on";
    }else{
      l.innerHTML="off";
    }
  }

  function mostrard(){
    var dat=document.getElementById("info");
    dat=variables[2];
  }
  
