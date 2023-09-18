/*
  File: used for textual chatbot response
  Description: This file contains the implementation of a chatbot.
  Date: June 14, 2023
*/
(function( $ ) {
    'use strict';
    $(document).ready(function(){
        var status = false;
        var loginFormId = $('#chatForm');
        var sessionID = $('#is_fred_api').val()
        loginFormId.validate({
            submitHandler: function(form, event) {
                event.preventDefault();
                if (status === true){
                    return true;
                }
                status = true;
                document.getElementById('message-id').placeholder = "Type your message here";
                $('.bot-typing').addClass('active');
                $('.chat-body').addClass('response-generate');
                var formData = loginFormId.serialize();
                var element = document.getElementById("about-insurance-chat");
                var user_message = document.getElementById("message-id").value.trim();
                $("#message-id").val("");
                $("#chatButton").prop('disabled', true);
                update_user_html(element, user_message)
                // Submit the form using AJAX
                $.ajax({
                    url:'api/v1/ask-bot/?session_id=' + sessionID,
                    type: form.method,
                    data: formData,
                    success: function(response) {
                        $("#message-id").val("");
                        update_ai_html(response, element);
                        $('.bot-typing').removeClass('active');
                        $('.chat-body').removeClass('response-generate');
                        document.getElementById("message-id").focus();
                        status = false;
                    },
                    error: function(xhr, status, error) {
                        $('.bot-typing').removeClass('active');
                        $('.chat-body').removeClass('response-generate');
                        document.getElementById("message-id").focus();
                        status = false;
                    }
                });
            },
            rules: {
                message: {
                    required: true,
                    minlength: 1,
                    maxlength: 500,
                    nowhitespace: true
                }
            },
            messages: {
                message: {
                    required: "",
                    minlength: ""
                }
            },
            success: function(error, element) {}
        });
        $.validator.addMethod(
              "nowhitespace",
              function(value, element) {
                var strippedValue = value.replace(/\s/g, '');
                return strippedValue !== '';
              },
              ""
        );
    });
})( jQuery );


/**
 * Updates the HTML element with the user's message for chat.
 *
 * @param {HTMLElement} element - The HTML element to update with the user message.
 * @param {string} user_message - The message entered by the user.
 * @returns {boolean} - Returns true if the update was successful.
 */
function update_user_html(element, user_message) {
      var message_html = '<div class="user-message"><p>' + user_message + '</p></div>';
      element.innerHTML += message_html;
      scrollToBottom(element);
      return true
}


/**
 * Updates the HTML element with the AI's response for chat.
 *
 * @param {object} response - The AI's response object.
 * @param {HTMLElement} element - The HTML element to update with the AI's response.
 * @returns {boolean} - Returns true if the update was successful.
 */
function update_ai_html(response, element) {
      var htmlContent = '<div class="bot-message"><div class="bot-thumb"><img src="'+
      load_constant.base_url +'/static/images/fred.png" alt="Quasar Market" /></div><p>' +
       response.data.message.replace(/\n/g, '<br>') + '</p></div>';
      element.innerHTML += htmlContent;
      scrollToBottom(element);
      return true
}

/**
 * Scrolls the given element to the bottom.
 *
 * @param {HTMLElement} element - The HTML element to scroll to the bottom.
 */
function scrollToBottom(element) {
    element.scrollTop = element.scrollHeight;
}

/**
 * Generate session id for a session
 */
function generateSessionID() {
    var timestamp = Date.now();
    var random = Math.random().toString(36).substr(2, 10);
    return timestamp + '_' + random;
}

/**
 * Wait for the DOM to finish loading and then add an event listener
 */
document.addEventListener('DOMContentLoaded', function() {
  /**
   * Event listener function for the 'keyup' event on the 'message-id' element.
   * It retrieves the input field value, trims it, and updates the 'chatButton'
   * disabled property based on the value's length.
   *
   * @param {Event} event - The event object for the 'keyup' event.
   */
  document.getElementById('message-id').addEventListener('keyup', function(event) {
    const messageInput = event.target;
    const trimmedValue = messageInput.value.trim();
    if (trimmedValue.length > 0) {
      $('#chatButton').prop('disabled', false);
    }else{
        $('#chatButton').prop('disabled', true);
    }
  });
});


/**
 * Wait for the DOM to finish loading and then attach event listeners
 * to the textarea element and the login form.
 */
document.addEventListener('DOMContentLoaded', function() {
  const textarea = document.getElementById('message-id');
  const loginFormId = $('#chatForm');
  /**
   * Event listener function for the 'input' event on the textarea element.
   * This function adjusts the height of the textarea based on its content.
   */
  textarea.addEventListener('input', function() {
    textarea.style.height = 'auto';
    textarea.style.height = textarea.scrollHeight + 'px';
  });
  /**
   * Event listener function for the 'keydown' event on the textarea element.
   * This function handles the behavior when the Enter key is pressed.
   *
   * @param {KeyboardEvent} event - The event object for the 'keydown' event.
   */
  textarea.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
      if (!event.shiftKey) {
        event.preventDefault();
        loginFormId.submit(); // Submit the form
      } else {
        // Shift + Enter is pressed
         textarea.value += '\n';
         textarea.style.height = 'auto';
         textarea.style.height = textarea.scrollHeight + 'px';
         textarea.scrollTop = textarea.scrollHeight;
      }
    }
  });
  /**
   * Event listener function for the 'submit' event on the login form.
   * This function prevents the default form submission behavior.
   *
   * @param {Event} event - The event object for the 'submit' event.
   */
  loginFormId.on('submit', function(event) {
    event.preventDefault();
  });
});
