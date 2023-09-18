/*
  File: speech-recognition.js
  Description: This file implements speech recognition functionality using the Web Speech API.
  Date: June 14, 2023
  Reference: https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition
*/
// Start speech recognition when the button is clicked
const userAgent = navigator.userAgent;
const startRecordingButton = document.getElementById('startRecordingButton');
startRecordingButton.addEventListener('click', function() {
  if (!userAgent.includes("Chrome") && !userAgent.includes("Safari") && !userAgent.includes("Edg")) {
    const browser_name = get_browser_name();
    $('#err-text').text('Speech recognition is not supported in ' + browser_name +'. Please use a different browser.');
    $('#toast-wrapper').addClass('show');
    return false;
  }
  checkMicrophonePermission();
});


/**
 * Create a speech recognition instance, set the language to 'en-US', and define
 * the behavior when a speech recognition result is obtained. The result transcript
 * is used to populate the input field, update the placeholder text, enable/disable
 * relevant buttons based on the transcript length, and set the cursor position to
 * the end of the input value.
 */
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'en-US';
recognition.onresult = function(event) {
  const transcript = event.results[0][0].transcript;
  const messageInput = document.getElementById('message-id');
  messageInput.value = capitalizeFirstLetter(transcript.replace(/\.$/, ''));
  messageInput.placeholder = "Type your message here";

  // Create a temporary textarea to calculate the scroll height
  const tempTextarea = document.createElement('textarea');
  tempTextarea.style.position = 'absolute';
  tempTextarea.style.top = '-9999px';
  tempTextarea.style.left = '-9999px';
  tempTextarea.style.width = messageInput.offsetWidth + 'px';
  tempTextarea.style.height = 'auto';
  tempTextarea.style.resize = 'none';
  tempTextarea.style.padding = getComputedStyle(messageInput).padding;
  tempTextarea.style.lineHeight = getComputedStyle(messageInput).lineHeight;
  tempTextarea.value = messageInput.value;
  document.body.appendChild(tempTextarea);

  // Adjust the textarea height based on the scroll height of the temporary textarea
  messageInput.style.height = tempTextarea.scrollHeight + 'px';

  // Remove the temporary textarea
  document.body.removeChild(tempTextarea);

  if (transcript.length > 0) {
    $('#chatButton').prop('disabled', false);
    $('#formButton').prop('disabled', false);
  }
  // Set cursor position to the end of the input value
  messageInput.focus();
  messageInput.setSelectionRange(messageInput.value.length, messageInput.value.length);
  messageInput.scrollTop = messageInput.scrollHeight;
  recognition.stop();
  recognition.abort();
};


/**
 * Function to check microphone permission and start speech recognition.
 * It checks if the browser supports the `navigator.mediaDevices.getUserMedia` method
 * to request microphone access. If supported, it checks if microphone permission is granted.
 * If permission is granted, it stops the microphone stream and starts the speech recognition process.
 * If permission is denied or an error occurs, it displays an error message to the user.
 * If microphone permission is not supported by the browser, it directly starts the speech recognition process.
 */
function checkMicrophonePermission() {
  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.enumerateDevices()
      .then(function(devices) {
        const hasMicrophone = devices.some(function(device) {
          return device.kind === 'audioinput';
        });

        if (hasMicrophone) {
          navigator.mediaDevices.getUserMedia({ audio: true })
            .then(function(stream) {
              stream.getTracks().forEach(function(track) {
                track.stop();
              });
              startSpeechRecognition();
            })
            .catch(function(error) {
              if (error.name === 'NotAllowedError' || error.name === 'PermissionDeniedError') {
                $('#err-text').text('Microphone permission blocked. Please allow microphone access in your browser settings.');
                $('#toast-wrapper').addClass('show');
              }
            });
        } else {
          $('#err-text').text('No microphone detected. Please make sure a microphone is connected.');
          $('#toast-wrapper').addClass('show');
        }
      })
      .catch(function(error) {
        console.log('Error enumerating devices:', error);
      });
  } else {
    // Microphone permission not supported by the browser
    startSpeechRecognition();
  }
}

/**
 * Function to open a microphone permission popup. It requests access to the user's microphone
 * using the `getUserMedia` method provided by the `navigator.mediaDevices` API. If permission is granted,
 * it stops the microphone stream and starts the speech recognition process. If permission is denied,
 * it logs an error message to the console.
 */
function openMicPermissionPopup() {
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(function(stream) {
      stream.getTracks().forEach(track => track.stop());
      startSpeechRecognition();
    })
    .catch(function(error) {
      console.log('Error opening microphone permission popup:', error);
    });
}

/**
 * This script handles speech recognition functionality and UI updates for a chat application.
 * It provides a function `startSpeechRecognition` that starts the speech recognition process,
 * clears the input field, updates the placeholder text, and adds a CSS class to a button.
 * After a timeout, the speech recognition process is stopped, the placeholder text is reset,
 * and the CSS class is removed from the button.
 */
function startSpeechRecognition() {
  document.getElementById("message-id").value = "";
  document.getElementById("message-id").placeholder = "Listening...";
  $("#startRecordingButton").addClass("listen");
  recognition.start();
  setTimeout(function() {
    recognition.stop();
    document.getElementById("message-id").placeholder = "Type your message here";
    $("#startRecordingButton").removeClass("listen");
  }, 15000);
}


/**
 * Retrieves the name of the current browser based on the user agent string.
 * @returns {string} The name of the browser.
 */
function get_browser_name(){
    var userAgent = navigator.userAgent;
    var browserName;
    if (/Firefox/i.test(userAgent)) {
      browserName = 'Mozilla Firefox';
    } else if (/Chrome/i.test(userAgent)) {
      browserName = 'Chrome';
    } else if (/Safari/i.test(userAgent)) {
      browserName = 'Safari';
    } else if (/Edg/i.test(userAgent)) {
      browserName = 'Edge';
    } else if (/Opera|OPR/i.test(userAgent)) {
      browserName = 'Opera';
    } else if (/Trident/i.test(userAgent)) {
      browserName = 'Internet Explorer';
    } else {
      browserName = 'this browser';
    }
    return browserName
}

/**
 * Capitalizes the first letter of a string.
 * @param {string} string - The input string.
 * @returns {string} The input string with the first letter capitalized.
 */
function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}