// Listen to updates in our tab system
let tabContainer = ["1", "2"];

chrome.tabs.onUpdated.addListener((tabId, tab) => {
  //grab tab name and url

  // console.log("this is current tab", tab.url);
  console.log("this is current tab title", tab.title);

  if (tab.title) {
    const queryParameters = tab.url;
    const urlParameters = new URLSearchParams(queryParameters);
    // console.log("this is the video id", urlParameters);
    //send a message to the content script that there is a new video loaded
    chrome.tabs.sendMessage(tabId, {
      type: "NEW",
      videoId: urlParameters,
    });
    tabContainer.push(tab.title);
  }
  console.log("this is tab container", tabContainer);
  sendData(tabContainer);
});


function sendData(data) {
  fetch("http://127.0.0.1:5000/process-data", {
     method: "POST", 
     headers: {
       "Content-Type": "application/json",
     },
     body: JSON.stringify({data: data}),
  }).then((response) => {
       // Check if the response is JSON
       const contentType = response.headers.get("content-type");
       if (contentType && contentType.indexOf("application/json") !== -1) {
         return response.json();
       } else {
         throw new TypeError("Oops, we haven't got JSON!");
       }
     })
     .then((data) => console.log("response", data))
     .catch((error) => {
       console.error("Error:", error);
     });
 }
 

 console.log(sendData(tabContainer));
